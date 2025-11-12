# SOFTWARE DEVELOPMENT TOOLS
## ON-CARE Medicine Ordering System - Revised Section

---

## Backend Programming Languages

**Python 3.13:** Python is chosen for backend development due to its simplicity, readability, and extensive library support for data analysis, time series forecasting, and web development. It handles core functionalities such as ARIMA forecasting model implementation, demand prediction algorithms, statistical analysis, data processing, and user authentication. Python's rich ecosystem includes specialized libraries for time series analysis (PMDARIMA, Statsmodels), web development (Django), and data manipulation (Pandas, NumPy), making it an ideal choice for developing the system's backend. The latest version 3.13 provides enhanced performance optimizations and improved security features essential for handling large-scale pharmaceutical transaction data and real-time forecasting computations.

---

## Web Framework and API Development

**Django 5.2.6:** Django serves as the main backend web framework, providing a high-level Python web framework that encourages rapid development and clean, pragmatic design. It offers built-in security features, including protection against common vulnerabilities such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF). Django's Model-View-Template (MVT) architecture facilitates the development of secure and maintainable web applications for medicine ordering, inventory management, and analytics dashboards, while its built-in admin interface simplifies system management tasks for pharmaceutical administrators. Django's ORM (Object-Relational Mapping) provides seamless database integration for managing medicine catalogs, orders, inventory, and user accounts, ensuring data integrity and efficient query execution for the ordering system.

**Django REST Framework 3.16.1:** Django REST Framework (DRF) extends Django's capabilities for building RESTful APIs, providing powerful and flexible tools for building Web APIs. It offers built-in support for authentication, permissions, serialization, and pagination, making it ideal for developing the medicine ordering system API that enables real-time inventory queries, order processing, forecast data access, and analytics reporting. DRF's browsable API feature facilitates testing and documentation, while its comprehensive authentication system supports various authentication methods including token-based authentication essential for secure API access by sales representatives, pharmacists, and system administrators. The framework enables seamless integration between the web interface and ARIMA forecasting engine, allowing asynchronous forecast generation and real-time analytics updates.

---

## Database Management

**MySQL (with mysqlclient 2.2.7):** MySQL serves as the primary database management system for storing medicine catalog data, order transactions, user information, inventory records, forecasting results, and system logs. It provides robust data storage capabilities with ACID compliance, ensuring data integrity and consistency critical for pharmaceutical inventory management and financial transactions. The mysqlclient 2.2.7 library enables seamless integration between Python and MySQL, providing efficient database connectivity and query execution for handling large volumes of transactional data (58,124+ records) and real-time inventory updates. MySQL's advanced security features, including encryption at rest and in transit, protect sensitive pharmaceutical data, customer information, and prescription records from unauthorized access, ensuring compliance with healthcare data protection regulations (HIPAA, GDPR).
 
---

## Data Analysis and Visualization

**Pandas 2.3.2:** Pandas is a powerful data manipulation and analysis library that provides data structures and operations for manipulating numerical tables and time series data. It facilitates the processing of historical transactional sales data, medicine demand patterns, order analytics, and forecasting results. Pandas' efficient data structures and built-in methods enable rapid data transformation and analysis, supporting the system's time series preprocessing for ARIMA modeling, demand trend analysis, and comprehensive reporting capabilities. The library's DataFrame functionality is essential for aggregating transactional data by medicine, time period, and sales representative, enabling accurate demand forecasting and supply chain optimization.

**NumPy 2.3.2:** NumPy provides fundamental support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It serves as the foundation for numerical computations in the system, particularly for ARIMA forecasting calculations, statistical analysis, and time series data processing. NumPy's optimized C implementations ensure high performance for mathematical operations essential in ARIMA parameter optimization, forecast accuracy calculations (RMSE, MAE, MAPE), and statistical model evaluation (AIC, BIC). The library enables efficient handling of large historical datasets (10 years of transaction data) and real-time forecast computations.

**Matplotlib 3.10.6:** Matplotlib is a comprehensive plotting library for creating static, animated, and interactive visualizations in Python. It enables the generation of charts and graphs for demand forecasting trends, inventory analytics, sales performance metrics, and ARIMA model diagnostics. Matplotlib's extensive customization options allow for the creation of publication-quality visualizations that support system reporting and analysis requirements, including time series plots, forecast vs. actual comparisons, seasonal decomposition charts, and model evaluation visualizations essential for managerial decision-making.

**Seaborn 0.13.2:** Seaborn is a statistical data visualization library built on top of Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics. It simplifies the creation of complex visualizations such as demand distribution plots, seasonal pattern analysis, correlation matrices between medicine sales, and regression plots for forecasting accuracy assessment. These visualizations are essential for analyzing system performance, identifying demand patterns, and understanding relationships between different medicines and market factors that influence pharmaceutical sales.

**Plotly 6.3.0:** Plotly provides interactive web-based visualizations that can be embedded in web applications. It enables the creation of dynamic charts and dashboards for real-time demand forecasting analytics, inventory level monitoring, order trend visualization, and ARIMA model performance tracking. Plotly's interactive features enhance user experience by allowing managers and administrators to explore forecast data through zooming, panning, and filtering capabilities, enabling interactive exploration of demand trends, seasonal patterns, and forecasting accuracy across different medicine categories and time periods.

**Scikit-learn 1.7.1:** Scikit-learn is a machine learning library that provides simple and efficient tools for data mining and data analysis. It supports various machine learning algorithms that can be used for data preprocessing in ARIMA forecasting, anomaly detection in demand patterns, and predictive analytics for inventory optimization. While ARIMA is the primary forecasting method, scikit-learn provides complementary tools for data scaling, feature engineering, and model validation that enhance the overall forecasting pipeline and support future enhancements with machine learning approaches.

**Statsmodels 0.14.5:** Statsmodels is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests and statistical data exploration. It supports advanced statistical analysis essential for ARIMA forecasting, including stationarity testing (Augmented Dickey-Fuller test), autocorrelation function (ACF) and partial autocorrelation function (PACF) analysis, seasonal decomposition, and residual diagnostics. The library provides comprehensive tools for time series analysis, model diagnostics, and statistical validation of forecasting models, ensuring robust and reliable demand predictions for pharmaceutical inventory management.

**Auto ARIMA (PMDARIMA 2.0.4):** PMDARIMA (Python implementation of Auto ARIMA) provides automated time series forecasting capabilities specifically designed for the ON-CARE system's demand prediction requirements. It automatically selects the optimal ARIMA model parameters (p, d, q) and seasonal components (P, D, Q, s) through systematic grid search, eliminating manual parameter tuning and enabling accurate forecasting without extensive statistical expertise. Auto ARIMA supports the research objective of implementing automatic parameter selection, processing historical transactional data (2015-2024) to generate demand forecasts for multiple time periods (daily, weekly, monthly) with confidence intervals. The library automatically handles stationarity testing, differencing, and model selection based on AIC and BIC criteria, achieving the target forecasting accuracy of ≤15% MAPE for at least 80% of medicine items, with actual performance exceeding targets at 5.69% MAPE (85% accuracy).

---

## Front-end Technologies

**HTML (HyperText Markup Language):** HTML serves as the standard markup language for creating web pages and web applications. It provides the structural foundation for the system's user interface, defining the layout and content organization of web pages for medicine ordering, inventory management, analytics dashboards, and user administration. HTML5 features, including semantic elements and form validation, enhance the user experience and support modern web application requirements, enabling intuitive interfaces for sales representatives to create orders, pharmacists to manage inventory, and administrators to access forecasting analytics.

**CSS (Cascading Style Sheets):** CSS controls the presentation and layout of HTML elements, enabling the creation of visually appealing and responsive user interfaces. It supports the design of professional-looking dashboards for forecasting analytics, order management forms, inventory tracking displays, and interactive elements that enhance user experience across different devices and screen sizes. CSS3 features, including flexbox and grid layouts, ensure responsive design and cross-browser compatibility, enabling sales representatives, pharmacists, and administrators to access the system from various devices while maintaining optimal user experience.

**JavaScript:** JavaScript provides client-side programming capabilities that enable interactive and dynamic user interfaces. It supports real-time form validation for order creation, asynchronous data loading for inventory updates, and interactive features such as dynamic chart updates for forecasting dashboards, real-time stock availability checking, and dynamic content updates for order status tracking. JavaScript's event handling and DOM manipulation capabilities enhance user interaction and provide seamless user experience throughout the medicine ordering process, from cart management to order submission and tracking.

**Bootstrap 5:** Bootstrap provides a responsive front-end framework that enables rapid development of mobile-friendly web interfaces. It supports the creation of consistent, professional user interfaces for the ordering system, ensuring optimal user experience across desktop, tablet, and mobile devices. Bootstrap's component library facilitates rapid development of navigation menus, forms, tables for medicine catalogs, and dashboard layouts for analytics and forecasting visualization.

**Chart.js:** Chart.js provides lightweight, responsive charting capabilities for visualizing forecasting results, demand trends, inventory levels, and sales analytics. It enables the creation of interactive line charts for time series forecasts, bar charts for inventory comparisons, and other visualizations that support managerial decision-making through intuitive data presentation.

---

## Development and Deployment Tools

**Git Version Control:** Git provides distributed version control capabilities for tracking changes in source code, managing collaborative development, and maintaining code integrity. It enables version control of the entire codebase, supporting team collaboration and ensuring code quality through branching and merging strategies. Git facilitates management of the Django application code, ARIMA forecasting modules, database migrations, and configuration files, ensuring systematic development and deployment processes.

**Virtual Environment (venv):** Python's built-in virtual environment tool isolates project dependencies and prevents conflicts between different Python packages. It ensures consistent development and deployment environments, supporting reproducible builds and preventing dependency-related issues during system deployment. The virtual environment manages dependencies for Django, PMDARIMA, Statsmodels, Pandas, NumPy, and other libraries, ensuring version compatibility and reliable system deployment.

**Package Management (pip):** pip serves as the standard package manager for Python, facilitating the installation and management of required libraries and dependencies. It ensures proper dependency resolution and version management, supporting reliable system deployment and maintenance. pip manages the comprehensive technology stack including Django 4.2, PMDARIMA 2.0.4, Statsmodels 0.14.5, Pandas 2.3.2, NumPy 2.3.2, and other essential libraries for the medicine ordering system.

---

## Security and Testing Tools

**Django Security Features:** Django's built-in security features provide protection against common web vulnerabilities, including SQL injection, XSS attacks, and CSRF attacks. These features ensure the security of the medicine ordering system and protect sensitive pharmaceutical data, customer information, prescription records, and financial transaction data. Django's security framework supports healthcare compliance requirements (HIPAA, GDPR) by providing secure data handling, encrypted session management, and comprehensive access control mechanisms.

**Unit Testing Framework (unittest):** Python's built-in unittest framework supports automated testing of individual components and functions. It enables comprehensive testing of ARIMA forecasting algorithms, order processing logic, inventory management functions, API endpoints, and business logic, ensuring system reliability and correctness. The framework supports testing of forecasting accuracy calculations, statistical model evaluation, data validation, and database operations critical for the medicine ordering system.

**Integration Testing Tools:** Various testing tools support end-to-end testing of the complete medicine ordering workflow, including order creation, inventory updates, prescription handling, ARIMA forecast generation, and analytics reporting processes. These tools ensure system integration and validate the complete user experience across different user roles (Sales Representatives, Pharmacists/Admins, System Administrators), ensuring that all system components work together seamlessly to deliver the required functionality.

**Django Test Framework:** Django's built-in testing framework provides comprehensive testing capabilities specifically designed for Django applications. It supports testing of models, views, forms, and API endpoints, enabling automated testing of the complete medicine ordering system functionality. The framework facilitates testing of user authentication, role-based access control, order processing workflows, inventory management operations, and ARIMA forecasting integration, ensuring system reliability and compliance with functional requirements.

---

## Summary

This comprehensive technology stack provides a robust foundation for developing a secure, scalable, and efficient web-based medicine ordering system with customer-centric supply chain analytics that meets modern healthcare requirements and user expectations. The technology selection directly supports the research objectives:

1. **Django Framework** enables the development of a comprehensive web-based ordering system with multi-role user management
2. **PMDARIMA (Auto ARIMA)** provides automatic parameter selection for demand forecasting, achieving the target accuracy of ≤15% MAPE (actual: 5.69% MAPE)
3. **Statsmodels and Pandas** support comprehensive statistical evaluation using AIC, BIC, RMSE, MAE, and MAPE metrics
4. **Plotly and Chart.js** enable interactive data visualization dashboards for managerial decision-making
5. **MySQL** ensures robust data storage for transactional data, medicine catalogs, and forecasting results
6. **Django REST Framework** facilitates API development for system integration and real-time data access

The technology stack is specifically designed to address Neo Care Philippines' operational challenges through automated inventory management, predictive demand forecasting, and data-driven decision-making capabilities, ultimately supporting the value proposition of 30% inventory cost reduction, 35% waste reduction, and ₱600,000 annual savings per pharmacy.

---

*This revised section aligns with the ON-CARE Medicine Ordering System research objectives and focuses on medicine ordering, ARIMA forecasting, and supply chain analytics rather than certificate authentication.*

