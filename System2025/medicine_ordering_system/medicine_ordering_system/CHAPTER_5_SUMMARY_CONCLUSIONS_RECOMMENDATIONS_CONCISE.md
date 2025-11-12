# CHAPTER 5
## SUMMARY, CONCLUSIONS, AND RECOMMENDATIONS

**ON-CARE: A Web-Based Ordering System with Customer-Centric Supply Chain Analytics for Neo Care Philippines**

**Student:** Ace Zheridan Gutierrez  
**Degree:** Master in Information and Technology  
**Institution:** Technological Institute of the Philippines  
**Date:** January 2025

---

## 5.1 SUMMARY 

This research developed and evaluated ON-CARE, a web-based medicine ordering system integrated with Auto-ARIMA forecasting capabilities for Neo Care Philippines. The study addressed the company's operational challenges in pharmaceutical distribution management, including reliance on manual processes, lack of digital presence, and absence of predictive analytics for strategic decision-making.

The system was developed using Django 4.2 framework with a 3-tier architecture consisting of eight integrated applications: accounts (user management), inventory (medicine catalog), orders (order processing), analytics (ARIMA forecasting), transactions (payment processing), audits (security logging), common (shared utilities), and oncare_admin (administrative functions). The database design incorporated 47+ tables supporting multi-role user management for Sales Representatives, Pharmacists/Admins, and System Administrators.

The Auto-ARIMA forecasting module was implemented using PMDARIMA library, processing 10 years of historical transactional data (2015-2024) containing 58,124 records for essential medications including Amoxicillin 250mg, Metformin 500mg, Paracetamol 500mg, Ibuprofen 400mg, and Vitamin C 1000mg. The module automatically selected optimal ARIMA parameters (p, d, q) and seasonal components (P, D, Q, s) through systematic grid search, achieving forecasting accuracy of 5.69% MAPE (85% accuracy), significantly exceeding the target objective.

The forecasting model evaluation utilized statistical criteria (AIC, BIC) and accuracy metrics (RMSE, MAE, MAPE). Results demonstrated excellent model performance with average AIC of 245.67, BIC of 267.89, RMSE of 129.34 units, MAE of 111.95 units, and MAPE of 5.69%. The system generated forecasts for multiple time periods (daily, weekly, monthly) with confidence intervals, enabling proactive inventory planning and strategic decision-making.

Interactive data visualization dashboards were developed using Plotly and Chart.js, displaying forecasted demand trends, historical patterns, seasonal variations, and inventory optimization recommendations. The dashboards enabled managers to access real-time analytics with average load times of 2.1 seconds, supporting informed decision-making for product imports and distribution strategies.

The system underwent comprehensive testing including unit testing (150+ test methods), integration testing, and user acceptance testing. Performance evaluation demonstrated system reliability with 99.7% uptime, average API response time of 180ms, and support for 500+ concurrent users. The implementation successfully transformed manual pharmaceutical distribution processes into an efficient digital platform, achieving measurable operational improvements including 30% inventory cost reduction, 35% waste reduction, and estimated annual savings of ₱600,000 per pharmacy.

---

## 5.2 CONCLUSIONS

Based on the research findings, the following conclusions are drawn, corresponding directly to each specific objective:

### Conclusion 1: Web-Based Ordering System Development

**The web-based ordering system for Neo Care Philippines was successfully developed using the Django framework, fully supporting product ordering, data management, and analytics capabilities.** The system implements comprehensive functionality through eight integrated Django applications, enabling complete order lifecycle management from cart creation to delivery confirmation. The architecture supports multi-role user management (Sales Representatives, Pharmacists/Admins, System Administrators) with role-based access control, ensuring secure and appropriate functionality access. Real-time inventory tracking with automatic stock updates, digital prescription upload and verification workflows, and payment processing integration were successfully implemented. The system achieved 99.7% uptime during operational testing and supports concurrent access for 500+ simultaneous users, exceeding the operational requirements. The database design with 47+ tables provides robust data management capabilities, enabling efficient storage and retrieval of medicine catalogs, order transactions, inventory records, and user information. This conclusion directly addresses Specific Objective 1, confirming successful development of a comprehensive web-based ordering system that transforms Neo Care Philippines' manual processes into an efficient digital platform.

### Conclusion 2: Auto-ARIMA Forecasting Module Implementation

**The Auto-ARIMA-based forecasting module was successfully implemented with automatic parameter selection, utilizing ACF and PACF analysis for optimal time series model identification.** The module, implemented using PMDARIMA library, automatically selected optimal ARIMA parameters (p, d, q) and seasonal components (P, D, Q, s) through systematic grid search across 29 parameter combinations. The implementation processes 10 years of historical transactional data (58,124 records from 2015-2024) for essential medications, applying stationarity testing using Augmented Dickey-Fuller (ADF) test, seasonal decomposition to identify trends and patterns, and automatic model selection based on AIC and BIC criteria. The Auto-ARIMA algorithm successfully eliminates manual parameter tuning, achieving model selection within 2.3 seconds per item, significantly faster than manual configuration approaches. The module generates forecasts for multiple time periods (daily, weekly, monthly) with confidence intervals, enabling proactive inventory planning. The automatic parameter selection mechanism successfully identifies optimal models such as ARIMA(0,1,2)(1,0,0)[12], demonstrating effective seasonal pattern capture with seasonal coefficient of 0.9348. This conclusion directly addresses Specific Objective 2, confirming successful implementation of automatic parameter selection that eliminates subjective manual tuning and supports the research requirement for automated forecasting capabilities.

### Conclusion 3: Forecasting Model Evaluation

**The forecasting model was comprehensively evaluated using statistical model selection criteria (AIC, BIC) and accuracy metrics (RMSE, MAE, MAPE), demonstrating excellent performance that exceeds research targets.** The evaluation results show average AIC of 245.67 (Excellent category: <1000), BIC of 267.89 (Excellent category: <1000), RMSE of 129.34 units (low relative to demand levels), MAE of 111.95 units (average error small compared to typical demand), and MAPE of 5.69% (Excellent category: <10%). The MAPE of 5.69% represents 85% forecasting accuracy, significantly exceeding the target objective and falling within the 'Excellent' performance category according to forecasting literature benchmarks. The statistical evaluation confirms model quality, with 65% of medicine items achieving Excellent model classification (MAPE <5%, AIC/BIC <1000), 25% achieving Good classification (MAPE 5-15%, AIC/BIC 1000-2000), and only 10% requiring further optimization. The directional accuracy of 73.1% indicates the model correctly predicts demand direction (increase/decrease) in approximately three-quarters of cases, providing additional confidence for inventory management decisions. The comprehensive evaluation framework, utilizing both model selection criteria (AIC, BIC) and accuracy metrics (RMSE, MAE, MAPE), establishes baseline performance benchmarks and enables comparison of model quality across different medicine categories. This conclusion directly addresses Specific Objective 3, confirming successful evaluation using the specified statistical and accuracy criteria, with results demonstrating model reliability suitable for operational inventory planning and strategic decision-making.

### Conclusion 4: Demand Trend Visualization

**Forecasted demand trends were successfully visualized through interactive data visualization dashboards, enabling managerial decision-making through intuitive data presentation and real-time analytics access.** The visualization system, implemented using Plotly and Chart.js, displays forecasted demand trends with multiple chart types including line charts for time series forecasts, bar charts for inventory comparisons, heatmaps for seasonal pattern analysis, and trend analysis visualizations. The dashboards present historical patterns and seasonal variations, enabling managers to identify demand cycles, peak periods, and trend patterns across different medicine categories. Interactive features allow users to explore forecast data through zooming, panning, and filtering capabilities, facilitating detailed analysis of specific time periods or medicine categories. The visualization system integrates forecasted demand with inventory optimization recommendations, presenting actionable insights for procurement planning and distribution strategies. Dashboard performance metrics demonstrate average load times of 2.1 seconds, meeting the operational requirement for real-time decision support. The visualization capabilities directly support managerial decision-making by presenting complex forecasting data in accessible formats, enabling informed strategic decisions regarding product imports, distribution allocation, and inventory optimization. The dashboards are accessible to Pharmacists/Admins and System Administrators through role-based interfaces, ensuring appropriate access to forecasting analytics while maintaining data security. This conclusion directly addresses Specific Objective 4, confirming successful development of visualization capabilities that enable managers to make informed decisions based on forecasted demand trends and supply chain analytics.

---

## 5.3 RECOMMENDATIONS

Based on the research findings and system implementation, the following recommendations are provided:

### 5.3.1 Recommendations for Neo Care Philippines

**Immediate Deployment:** The system demonstrates exceptional technical quality, comprehensive functionality, and strong business value (30% inventory cost reduction, 300% ROI). The recommendation is to proceed with production deployment, implementing a phased rollout approach starting with core team validation, followed by expansion to all user roles, and culminating in full system deployment with external system integrations.

**User Training and Adoption:** Maintain the comprehensive training program with role-specific modules for each user type, focusing particularly on advanced analytics training for managers and administrators. Establish systematic feedback collection mechanisms including regular user satisfaction surveys, feature request tracking, and usability testing sessions to guide continuous improvement.

**Performance Monitoring:** Implement comprehensive system monitoring including real-time performance metrics (response times, throughput, error rates), forecasting accuracy tracking with automated alerting, user activity monitoring, and system health monitoring with automated alerts. Conduct regular performance reviews and optimization to ensure sustained system performance.

**Feature Enhancements:** Based on user feedback and business needs, prioritize enhancements including enhanced mobile responsiveness and mobile application development for sales representatives, additional reporting and analytics features, expanded forecasting horizons and scenarios, integration with external supplier systems, and advanced inventory optimization algorithms.

### 5.3.2 Recommendations for Future Research

**Advanced Forecasting Methods:** While ARIMA demonstrated excellent performance (5.69% MAPE), future research should explore multivariate ARIMA models incorporating external factors (seasonality, promotions, market trends), machine learning approaches (LSTM, Prophet, ensemble methods) for comparison, hybrid models combining ARIMA with machine learning, and real-time forecasting with adaptive model updates.

**Extended Forecasting Accuracy Research:** Conduct longitudinal studies to evaluate forecasting accuracy over extended periods (2-5 years), analyze factors affecting forecasting accuracy across different medicine categories, study seasonal pattern variations and their impact on accuracy, and develop medicine-specific forecasting strategies based on demand patterns.

**System Enhancement Research:** Research and develop mobile applications for sales representatives (field-based order management), pharmacists (mobile prescription verification), and managers (mobile analytics and reporting). Explore advanced analytics capabilities including predictive analytics for customer behavior and purchasing patterns, prescriptive analytics for inventory optimization recommendations, and anomaly detection for unusual demand patterns.

**Quality and Compliance Research:** Conduct comprehensive quality evaluation including comparative analysis with other healthcare software systems, extended quality assessment using multiple frameworks, longitudinal quality assessment over multiple years, and quality cost-benefit analysis. Research advanced compliance capabilities including real-time compliance monitoring and alerting, predictive compliance risk assessment, and automated compliance reporting.

### 5.3.3 Recommendations for the Industry

**Digital Transformation Initiatives:** The pharmaceutical distribution industry, particularly small-to-medium enterprises, should consider adopting similar web-based ordering systems with predictive analytics. The demonstrated benefits (30% cost reduction, 300% ROI) justify investment in digital transformation initiatives. Organizations should implement demand forecasting systems to enable data-driven inventory management, achieving significant operational improvements and cost savings.

**Predictive Analytics Implementation:** Pharmaceutical distributors should prioritize supply chain optimization through data-driven approaches. The integration of forecasting with inventory management demonstrates significant operational improvements and cost savings. Organizations should focus on understanding customer needs, purchasing patterns, and demand trends to improve service delivery and customer satisfaction.

**Customer-Centric Approach:** Organizations should emphasize customer analytics and enhance digital customer experience. The study demonstrates that web-based ordering systems significantly improve customer experience through streamlined processes, real-time visibility, and convenient access. Organizations should prioritize digital customer experience enhancement to maintain competitive advantage.

**Quality and Compliance:** Organizations should prioritize healthcare compliance from system design through deployment. The research demonstrates that comprehensive healthcare compliance (97.8%) is achievable and essential for pharmaceutical systems. Organizations should adopt systematic quality assessment frameworks for healthcare software systems to ensure reliability, security, and usability.

### 5.3.4 Recommendations for Academic and Research Community

**Research Methodologies:** Extend Design and Development Research (DDR) approaches to other healthcare information systems contexts and system types. Develop more comprehensive frameworks for healthcare software quality assessment that integrate multiple quality standards and compliance requirements.

**Publication and Dissemination:** Publish research findings in relevant academic journals including Healthcare Information Systems journals, Supply Chain Management journals, Software Quality and Engineering journals, and Information Systems Research journals. Present findings at academic conferences to share knowledge with the research community, receive feedback for future research directions, and facilitate collaboration with other researchers.

**Educational Applications:** Incorporate the research methodology, findings, and system implementation into Information Systems curriculum, Healthcare Informatics programs, Software Engineering courses, and Supply Chain Management education. Develop case studies for system development methodologies, healthcare software quality assessment, predictive analytics in supply chain management, and Agile development in healthcare contexts.

---

## 5.4 FINAL CONCLUSION

The research successfully achieved all stated objectives through the development, implementation, and evaluation of ON-CARE, a comprehensive web-based medicine ordering system with customer-centric supply chain analytics for Neo Care Philippines. The system demonstrates exceptional technical quality, outstanding forecasting accuracy (5.69% MAPE, 85% accuracy), and delivers significant business value (30% inventory cost reduction, 300% ROI, ₱600,000 annual savings per pharmacy).

The conclusions directly prove the achievement of each specific objective: (1) successful development of a comprehensive web-based ordering system using Django framework, (2) successful implementation of Auto-ARIMA forecasting with automatic parameter selection, (3) comprehensive evaluation demonstrating excellent forecasting performance exceeding research targets, and (4) successful visualization of forecasted demand trends enabling managerial decision-making.

The system is positioned to deliver long-term value through continued enhancement, user adoption, and strategic expansion. The research establishes a foundation for future studies in healthcare information systems, predictive analytics, and supply chain optimization, contributing to the advancement of knowledge in these critical domains.

---

**End of Chapter 5**

---

*This chapter provides a concise summary of the research work, direct conclusions corresponding to each specific objective, and comprehensive recommendations for practice, future research, industry, and the academic community.*

