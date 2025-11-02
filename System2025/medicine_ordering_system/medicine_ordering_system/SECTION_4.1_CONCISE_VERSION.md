# Section 4.1: System Development - Concise Academic Version

---

## **4.1 System Development**

In developing the ON-CARE web-based medicine ordering system, a comprehensive technology stack was implemented to address the research objectives of creating an efficient, scalable, and analytically-driven pharmaceutical ordering platform. The system leverages modern web technologies and advanced statistical modeling capabilities to transform Neo Care Philippines' manual operations into a digital, data-driven workflow.

### **Web Framework and Backend**

The system was built using **Django 4.2**, a high-level Python web framework following the Model-Template-View (MTV) architectural pattern. Django was selected for its robust security features, comprehensive authentication system, and excellent database abstraction layer essential for managing complex data relationships in medicine catalogs, orders, and inventory management.

**Python 3.8+** serves as the primary programming language, chosen for its extensive library ecosystem and powerful data processing capabilities required for implementing the ARIMA forecasting module.

### **Frontend Technologies**

The user interface was developed using **HTML5**, **CSS3**, and **JavaScript** with **Bootstrap 5** framework, ensuring responsive, mobile-first design across different devices. **jQuery** facilitates dynamic user interactions and asynchronous communication with the backend, while **Chart.js** provides interactive data visualization capabilities for analytics dashboards, directly supporting the research objective of enabling managerial decision-making through data-driven insights.

### **Database Management**

The system utilizes **SQLite** for development and **MySQL/MariaDB** for production environments. The Django ORM (Object-Relational Mapping) provides unified database operations, supporting complex data relationships required for multi-role user management, order processing workflows, and integrated inventory-forecasting functionality.

### **Analytics and Forecasting Engine**

The core differentiator lies in the integration of **Auto-ARIMA forecasting** capabilities. **Pandas 2.3.2** provides data manipulation tools for processing historical transactional data, while **NumPy 2.3.2** supplies numerical computing capabilities. **Statsmodels 0.14.5** offers statistical modeling including stationarity testing and ARIMA implementation. **PMDARIMA (Auto ARIMA) 2.0.4** automates ARIMA parameter selection through systematic grid search, automatically determining optimal values for autoregressive (p), differencing (d), moving average (q), and seasonal components based on AIC and BIC criteria. This directly addresses Research Objective 2, requiring an Auto ARIMA-based forecasting module with automatic parameter selection.

### **Additional Technologies**

**Django REST Framework 3.14.0** provides RESTful API endpoints for programmatic access and future integrations. **Redis 4.6.0** enables in-memory caching to improve performance, while **Celery 5.3.6** facilitates asynchronous task processing for computationally intensive ARIMA operations, ensuring responsive user interface during forecasting computations.

### **Development Architecture**

The system follows a modular architecture organized into eight specialized Django applications: **accounts** (user management), **inventory** (medicine catalog and stock management), **orders** (order processing), **analytics** (ARIMA forecasting), **transactions** (payment processing), **audits** (security logging), **common** (shared utilities), and **oncare_admin** (administrative functions). This modular design supports maintainability, scalability, and separation of concerns while facilitating the integration of specialized modules such as the analytics forecasting engine.

### **Implementation Achievement**

The development successfully delivered a fully functional web-based ordering system implementing all research objectives. The system is operational, processing orders, managing inventory, and generating forecasts based on Neo Care Philippines' 10-year historical dataset (January 2015 to December 2024), comprising 58,124 transactional records for essential medications including Metformin 500mg, Amoxicillin 250mg, Paracetamol 500mg, Ibuprofen 400mg, and Vitamin C 1000mg.

---

## **Discussion**

The development of ON-CARE represents a comprehensive transformation of manual pharmaceutical distribution processes into an integrated, web-based platform combining e-commerce functionality with advanced predictive analytics. The Django framework enabled rapid development while maintaining security standards essential for healthcare applications. The modular architecture, organized into eight specialized applications, supports complex functional requirements while enabling independent development of system components.

The integration of Auto-ARIMA forecasting represents a significant technical achievement, successfully embedding sophisticated time series analysis within a web application framework. Celery asynchronous processing prevents interface blocking during computationally intensive forecasting operations, while Redis caching optimizes performance. This technical implementation directly supports Research Objectives 2, 3, and 4 by providing automated forecasting with comprehensive evaluation metrics and interactive visualization capabilities.

The technology stack selection balanced development efficiency, performance requirements, and analytical capabilities. Django's built-in security features address healthcare data protection needs, Python's scientific computing libraries provide robust time series analysis, and Bootstrap ensures responsive design for field sales representatives using mobile devices.

The completed system successfully delivers comprehensive functionality addressing all identified operational challenges: order management replacing manual processes, real-time inventory tracking, automated demand forecasting, multi-role support, prescription handling, and interactive analytics dashboards. All five research objectives have been achieved, with the system ready for comprehensive evaluation as detailed in subsequent sections.

---

**Word Count:** ~550 words (adjustable based on requirements)

*This concise version maintains academic rigor while being more suitable for thesis format constraints.*
