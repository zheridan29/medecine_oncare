"""
Performance Testing Suite for ON-CARE Medicine Ordering System
"""

import time
import threading
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
import statistics
import logging
from typing import List, Dict, Any
import psutil
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PerformanceTestSuite:
    """
    Comprehensive performance testing suite for ON-CARE system
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.results = {}
        self.auth_token = None
        self.session = requests.Session()
        
    def authenticate(self, username: str, password: str) -> bool:
        """
        Authenticate and get session token
        """
        try:
            login_data = {
                'username': username,
                'password': password,
            }
            
            response = self.session.post(
                f"{self.base_url}/accounts/login/",
                data=login_data,
                timeout=10
            )
            
            if response.status_code == 200:
                # Extract CSRF token
                csrf_token = response.cookies.get('csrftoken')
                if csrf_token:
                    self.session.headers.update({'X-CSRFToken': csrf_token})
                
                logger.info("Authentication successful")
                return True
            else:
                logger.error(f"Authentication failed: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return False
    
    def single_request_test(self, endpoint: str, method: str = 'GET', 
                          data: Dict = None, headers: Dict = None) -> Dict[str, Any]:
        """
        Perform a single request and measure performance
        """
        start_time = time.time()
        
        try:
            if method.upper() == 'GET':
                response = self.session.get(
                    f"{self.base_url}{endpoint}",
                    headers=headers,
                    timeout=30
                )
            elif method.upper() == 'POST':
                response = self.session.post(
                    f"{self.base_url}{endpoint}",
                    json=data,
                    headers=headers,
                    timeout=30
                )
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            end_time = time.time()
            response_time = end_time - start_time
            
            return {
                'endpoint': endpoint,
                'method': method,
                'status_code': response.status_code,
                'response_time': response_time,
                'success': response.status_code < 400,
                'content_length': len(response.content),
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            end_time = time.time()
            return {
                'endpoint': endpoint,
                'method': method,
                'status_code': 0,
                'response_time': end_time - start_time,
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def load_test(self, endpoint: str, concurrent_users: int, 
                 duration_seconds: int, method: str = 'GET', 
                 data: Dict = None) -> Dict[str, Any]:
        """
        Perform load testing with concurrent users
        """
        logger.info(f"Starting load test: {concurrent_users} users for {duration_seconds} seconds")
        
        results = []
        start_time = time.time()
        end_time = start_time + duration_seconds
        
        def worker():
            worker_results = []
            while time.time() < end_time:
                result = self.single_request_test(endpoint, method, data)
                worker_results.append(result)
                time.sleep(0.1)  # Small delay between requests
            return worker_results
        
        # Execute concurrent workers
        with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            futures = [executor.submit(worker) for _ in range(concurrent_users)]
            
            for future in as_completed(futures):
                worker_results = future.result()
                results.extend(worker_results)
        
        return self.analyze_load_test_results(results)
    
    def stress_test(self, endpoint: str, max_users: int, 
                   step_users: int, duration_per_step: int) -> Dict[str, Any]:
        """
        Perform stress testing by gradually increasing load
        """
        logger.info(f"Starting stress test: up to {max_users} users")
        
        stress_results = []
        
        for users in range(step_users, max_users + 1, step_users):
            logger.info(f"Testing with {users} concurrent users")
            
            result = self.load_test(endpoint, users, duration_per_step)
            result['concurrent_users'] = users
            stress_results.append(result)
            
            # Check if system is still responsive
            if result['error_rate'] > 0.1:  # 10% error rate threshold
                logger.warning(f"High error rate detected at {users} users: {result['error_rate']:.2%}")
            
            if result['avg_response_time'] > 5.0:  # 5 second response time threshold
                logger.warning(f"High response time detected at {users} users: {result['avg_response_time']:.2f}s")
        
        return self.analyze_stress_test_results(stress_results)
    
    def analyze_load_test_results(self, results: List[Dict]) -> Dict[str, Any]:
        """
        Analyze load test results and calculate metrics
        """
        if not results:
            return {'error': 'No results to analyze'}
        
        successful_requests = [r for r in results if r['success']]
        failed_requests = [r for r in results if not r['success']]
        
        response_times = [r['response_time'] for r in successful_requests]
        
        if response_times:
            avg_response_time = statistics.mean(response_times)
            min_response_time = min(response_times)
            max_response_time = max(response_times)
            median_response_time = statistics.median(response_times)
            p95_response_time = self.percentile(response_times, 95)
            p99_response_time = self.percentile(response_times, 99)
        else:
            avg_response_time = min_response_time = max_response_time = 0
            median_response_time = p95_response_time = p99_response_time = 0
        
        total_requests = len(results)
        successful_requests_count = len(successful_requests)
        failed_requests_count = len(failed_requests)
        error_rate = failed_requests_count / total_requests if total_requests > 0 else 0
        
        # Calculate throughput (requests per second)
        if results:
            first_request_time = min(r['timestamp'] for r in results)
            last_request_time = max(r['timestamp'] for r in results)
            
            # Parse timestamps
            start_time = datetime.fromisoformat(first_request_time.replace('Z', '+00:00'))
            end_time = datetime.fromisoformat(last_request_time.replace('Z', '+00:00'))
            
            duration = (end_time - start_time).total_seconds()
            throughput = total_requests / duration if duration > 0 else 0
        else:
            throughput = 0
        
        return {
            'total_requests': total_requests,
            'successful_requests': successful_requests_count,
            'failed_requests': failed_requests_count,
            'error_rate': error_rate,
            'throughput_rps': throughput,
            'avg_response_time': avg_response_time,
            'min_response_time': min_response_time,
            'max_response_time': max_response_time,
            'median_response_time': median_response_time,
            'p95_response_time': p95_response_time,
            'p99_response_time': p99_response_time,
            'results': results
        }
    
    def analyze_stress_test_results(self, results: List[Dict]) -> Dict[str, Any]:
        """
        Analyze stress test results across different load levels
        """
        breakdown_point = None
        max_throughput = 0
        optimal_users = 0
        
        for result in results:
            if result['throughput_rps'] > max_throughput:
                max_throughput = result['throughput_rps']
                optimal_users = result['concurrent_users']
            
            if result['error_rate'] > 0.05 and breakdown_point is None:  # 5% error rate threshold
                breakdown_point = result['concurrent_users']
        
        return {
            'stress_results': results,
            'max_throughput': max_throughput,
            'optimal_users': optimal_users,
            'breakdown_point': breakdown_point,
            'performance_analysis': self.generate_performance_analysis(results)
        }
    
    def generate_performance_analysis(self, results: List[Dict]) -> str:
        """
        Generate human-readable performance analysis
        """
        analysis = []
        
        if not results:
            return "No data available for analysis"
        
        # Find optimal performance point
        max_throughput_result = max(results, key=lambda x: x['throughput_rps'])
        analysis.append(f"Maximum throughput: {max_throughput_result['throughput_rps']:.2f} RPS at {max_throughput_result['concurrent_users']} users")
        
        # Find breakdown point
        breakdown_point = None
        for result in results:
            if result['error_rate'] > 0.05:
                breakdown_point = result['concurrent_users']
                break
        
        if breakdown_point:
            analysis.append(f"System breakdown point: {breakdown_point} concurrent users")
        else:
            analysis.append("System remained stable throughout the test")
        
        # Performance trends
        response_times = [r['avg_response_time'] for r in results]
        if response_times:
            if max(response_times) / min(response_times) > 2:
                analysis.append("Response time degradation observed under high load")
            else:
                analysis.append("Response time remained relatively stable")
        
        return "\n".join(analysis)
    
    def percentile(self, data: List[float], percentile: int) -> float:
        """
        Calculate percentile value
        """
        if not data:
            return 0
        
        sorted_data = sorted(data)
        index = int(len(sorted_data) * percentile / 100)
        if index >= len(sorted_data):
            index = len(sorted_data) - 1
        
        return sorted_data[index]
    
    def system_resource_monitoring(self, duration_seconds: int) -> Dict[str, Any]:
        """
        Monitor system resources during testing
        """
        logger.info(f"Monitoring system resources for {duration_seconds} seconds")
        
        start_time = time.time()
        end_time = start_time + duration_seconds
        
        cpu_usage = []
        memory_usage = []
        disk_usage = []
        
        while time.time() < end_time:
            cpu_usage.append(psutil.cpu_percent())
            memory_usage.append(psutil.virtual_memory().percent)
            disk_usage.append(psutil.disk_usage('/').percent)
            
            time.sleep(1)  # Sample every second
        
        return {
            'duration_seconds': duration_seconds,
            'avg_cpu_usage': statistics.mean(cpu_usage),
            'max_cpu_usage': max(cpu_usage),
            'avg_memory_usage': statistics.mean(memory_usage),
            'max_memory_usage': max(memory_usage),
            'avg_disk_usage': statistics.mean(disk_usage),
            'max_disk_usage': max(disk_usage),
            'cpu_samples': cpu_usage,
            'memory_samples': memory_usage,
            'disk_samples': disk_usage
        }
    
    def comprehensive_performance_test(self) -> Dict[str, Any]:
        """
        Run comprehensive performance tests on all major endpoints
        """
        logger.info("Starting comprehensive performance test suite")
        
        test_endpoints = [
            {'endpoint': '/', 'method': 'GET', 'name': 'Home Page'},
            {'endpoint': '/accounts/login/', 'method': 'GET', 'name': 'Login Page'},
            {'endpoint': '/inventory/medicines/', 'method': 'GET', 'name': 'Medicine Catalog'},
            {'endpoint': '/orders/cart/', 'method': 'GET', 'name': 'Shopping Cart'},
            {'endpoint': '/analytics/dashboard/', 'method': 'GET', 'name': 'Analytics Dashboard'},
            {'endpoint': '/api/medicines/', 'method': 'GET', 'name': 'Medicines API'},
            {'endpoint': '/api/orders/', 'method': 'GET', 'name': 'Orders API'},
        ]
        
        comprehensive_results = {}
        
        # Test each endpoint
        for test_config in test_endpoints:
            endpoint = test_config['endpoint']
            method = test_config['method']
            name = test_config['name']
            
            logger.info(f"Testing {name} ({endpoint})")
            
            # Single request test
            single_result = self.single_request_test(endpoint, method)
            
            # Load test (10 concurrent users for 30 seconds)
            load_result = self.load_test(endpoint, 10, 30, method)
            
            # Stress test (up to 50 users in steps of 10)
            stress_result = self.stress_test(endpoint, 50, 10, 20)
            
            comprehensive_results[name] = {
                'single_request': single_result,
                'load_test': load_result,
                'stress_test': stress_result
            }
        
        return comprehensive_results
    
    def generate_performance_report(self, results: Dict[str, Any]) -> str:
        """
        Generate comprehensive performance report
        """
        report = []
        report.append("=" * 80)
        report.append("ON-CARE MEDICINE ORDERING SYSTEM - PERFORMANCE TEST REPORT")
        report.append("=" * 80)
        report.append(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        for endpoint_name, endpoint_results in results.items():
            report.append(f"ENDPOINT: {endpoint_name}")
            report.append("-" * 50)
            
            # Single request results
            single = endpoint_results['single_request']
            if single['success']:
                report.append(f"Single Request Response Time: {single['response_time']:.3f}s")
            else:
                report.append(f"Single Request Failed: {single.get('error', 'Unknown error')}")
            
            # Load test results
            load = endpoint_results['load_test']
            report.append(f"Load Test (10 users, 30s):")
            report.append(f"  - Total Requests: {load['total_requests']}")
            report.append(f"  - Success Rate: {(1-load['error_rate'])*100:.1f}%")
            report.append(f"  - Average Response Time: {load['avg_response_time']:.3f}s")
            report.append(f"  - Throughput: {load['throughput_rps']:.2f} RPS")
            report.append(f"  - 95th Percentile: {load['p95_response_time']:.3f}s")
            
            # Stress test results
            stress = endpoint_results['stress_test']
            if 'max_throughput' in stress:
                report.append(f"Stress Test Results:")
                report.append(f"  - Maximum Throughput: {stress['max_throughput']:.2f} RPS")
                report.append(f"  - Optimal Users: {stress['optimal_users']}")
                if stress['breakdown_point']:
                    report.append(f"  - Breakdown Point: {stress['breakdown_point']} users")
                
                report.append(f"  - Performance Analysis:")
                for line in stress['performance_analysis'].split('\n'):
                    report.append(f"    {line}")
            
            report.append("")
        
        # Overall system assessment
        report.append("OVERALL SYSTEM ASSESSMENT")
        report.append("-" * 50)
        
        all_avg_times = []
        all_error_rates = []
        all_throughputs = []
        
        for endpoint_results in results.values():
            load = endpoint_results['load_test']
            all_avg_times.append(load['avg_response_time'])
            all_error_rates.append(load['error_rate'])
            all_throughputs.append(load['throughput_rps'])
        
        if all_avg_times:
            overall_avg_time = statistics.mean(all_avg_times)
            overall_error_rate = statistics.mean(all_error_rates)
            overall_throughput = sum(all_throughputs)
            
            report.append(f"Average Response Time: {overall_avg_time:.3f}s")
            report.append(f"Overall Error Rate: {overall_error_rate*100:.1f}%")
            report.append(f"Total System Throughput: {overall_throughput:.2f} RPS")
            
            # Performance rating
            if overall_avg_time < 1.0 and overall_error_rate < 0.01:
                rating = "EXCELLENT"
            elif overall_avg_time < 2.0 and overall_error_rate < 0.05:
                rating = "GOOD"
            elif overall_avg_time < 5.0 and overall_error_rate < 0.1:
                rating = "ACCEPTABLE"
            else:
                rating = "NEEDS IMPROVEMENT"
            
            report.append(f"Performance Rating: {rating}")
        
        report.append("")
        report.append("RECOMMENDATIONS")
        report.append("-" * 50)
        
        # Generate recommendations based on results
        recommendations = []
        
        if any(r['load_test']['avg_response_time'] > 2.0 for r in results.values()):
            recommendations.append("- Optimize database queries and add caching")
        
        if any(r['load_test']['error_rate'] > 0.05 for r in results.values()):
            recommendations.append("- Investigate and fix error-causing endpoints")
        
        if any(r['stress_test'].get('breakdown_point', 0) < 20 for r in results.values()):
            recommendations.append("- Consider horizontal scaling for high-load scenarios")
        
        if not recommendations:
            recommendations.append("- System performance is within acceptable limits")
        
        for rec in recommendations:
            report.append(rec)
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)


def main():
    """
    Main function to run performance tests
    """
    # Initialize test suite
    test_suite = PerformanceTestSuite()
    
    # Authenticate (optional - some endpoints may require auth)
    # test_suite.authenticate("admin", "password")
    
    # Run comprehensive performance tests
    logger.info("Running comprehensive performance test suite...")
    results = test_suite.comprehensive_performance_test()
    
    # Generate and save report
    report = test_suite.generate_performance_report(results)
    
    # Save report to file
    with open('performance_test_report.txt', 'w') as f:
        f.write(report)
    
    logger.info("Performance test completed. Report saved to performance_test_report.txt")
    print(report)


if __name__ == "__main__":
    main()

