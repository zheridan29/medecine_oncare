# Chapter 3
# Operational Framework

## 3.1 Materials

### 3.1.1 Software
Throughout this capstone project, the following software is to be used:

1. Programming Language
- Python 3.13

2. Web Framework and API
- Django 5.2.6 – Main backend web framework
- Django REST Framework 3.16.1 – RESTful API development

3. Database
- MySQL (with mysqlclient 2.2.7)

4. Data Analysis and Visualization
- Pandas 2.3.2 – Data manipulation
- Numpy 2.3.2 – Numerical computations
- Matplotlib 3.10.6, Seaborn 0.13.2, Plotly 6.3.0 – Data visualization
- Scikit-learn 1.7.1
- Statsmodels 0.14.5
- Auto ARIMA (via statsmodels) – Machine learning and forecasting

5. Front-end Technologies
- HTML, CSS, JavaScript

---

### Software Development Tools

Backend Programming Languages

Python 3.13: Python is chosen for backend development due to its simplicity, readability, and extensive library support. It handles core functionalities such as data processing, analytics, and authentication. The latest version 3.13 provides performance optimizations and improved security features.

Web Framework and API Development

Django 5.2.6: Django serves as the main backend web framework, providing rapid development, built-in security protections (SQL injection, XSS, CSRF), and an MVT architecture that supports maintainable web applications. Its admin interface simplifies system management tasks.

Django REST Framework 3.16.1: DRF extends Django for building RESTful APIs with authentication, permissions, serialization, and pagination—ideal for system APIs. The browsable API aids testing and documentation.

Database Management

MySQL (with mysqlclient 2.2.7): MySQL stores transactional data, inventory, and logs with ACID compliance for integrity and consistency. The mysqlclient library enables efficient Python–MySQL connectivity. Encryption at rest/in transit protects sensitive data.

Data Analysis and Visualization

Pandas 2.3.2: Provides data structures and operations for numerical tables and time series; supports reporting and analytics.

NumPy 2.3.2: Foundation for numerical computations and vectorized operations.

Matplotlib 3.10.6 / Seaborn 0.13.2 / Plotly 6.3.0: Static and interactive visualizations for analytics dashboards and reports.

Scikit-learn 1.7.1: Machine learning utilities for pattern recognition and anomaly detection.

Statsmodels 0.14.5: Statistical models, tests, and exploration.

Auto ARIMA (via statsmodels): Automated time series forecasting and parameter selection.

Front-end Technologies

HTML, CSS, JavaScript: Core web technologies for responsive and interactive UI.

Development and Deployment Tools

Git Version Control: Distributed version control for collaborative development.

Virtual Environment (venv): Isolates project dependencies for reproducible environments.

Package Management (pip): Installs and manages Python libraries and dependencies.

Security and Testing Tools

Django Security Features: Built-in protections against common web vulnerabilities.

Unit Testing Framework (unittest): Automated testing of components and functions.

Integration Testing Tools: End-to-end testing of workflows and APIs.

---

### 3.1.2 Hardware
The researcher used a Lenovo LOQ 15IRX9 laptop with the following specifications:
- Processor: 13th Gen Intel(R) Core(TM) i5-13450HX CPU @ 2.40 GHz
- Installed RAM: 16.0 GB
- Storage: 512 GB SSD NVMe
- Graphics: Nvidia GeForce RTX 4050 GPU

The system development and data processing components for the ON-CARE Medicine Ordering System were executed on this platform to support Python/Django programming, database integration, and ARIMA-based forecasting. The hardware provided sufficient performance for real-time analytics and development workloads [Lenovo, 2025; Martinez & Thompson, 2023].

---

### 3.1.3 Data
The researcher conducted business meetings with Neo Care Philippines. A formal request letter was sent to obtain time-based transactional sales data (2015–2024) under an NDA. The ten-year dataset was verified by administrative staff and includes both pre- and post-pandemic data. Integrity was confirmed—no modifications during filtering.

Dataset contains 58,124 transactional records for key medications: Amoxicillin 250mg, Metformin 500mg, Paracetamol 500mg, Ibuprofen 400mg, and Vitamin C 1000mg.

Dataset Structure:
- Order ID (oid): Unique identifier for each transaction
- Sales Representative ID: User responsible for order creation
- Medicine ID (prod_id): Product identifier
- Order Quantity (oqty): Quantity ordered (each order is a box of 40 packs)
- Stock Quantity (sqty): Available inventory at transaction time
- Amount: Total value (quantity × unit price)
- Transaction Code: Unique transaction identifier
- Order Date (dateorder): ISO timestamp (YYYY-MM-DDTHH:MM:SS)
- Status (issaved): Transaction status for recovery

Table 3-1. Sample Raw Data from Neo Care Philippines

---

## 3.2 Methods

### 3.2.1 Waterfall Model
This study adopts the SDLC Waterfall Model with sequential phases where each phase output feeds the next (Virtasant, 2020; Yas et al., 2023). Suitable for stable, well-defined requirements in healthcare (Alam et al., 2022; Yas et al., 2023).

Phases:
- Requirements Analysis: Gather and validate functional/non-functional requirements.
- System Design: Define architecture, data flows, schemas, and interface layouts.
- Implementation: Build components with code quality and version control.
- Testing: Unit, integration, and UAT to verify requirements (Alam et al., 2022).
- Deployment: Release with user training and documentation.
- Maintenance: Updates, bug fixes, and improvements (Yas et al., 2023).

### 3.2.2 Data Gathering Tools and Procedures

1. Observation (Goodwin, 2020; Laurier, 2021; Kawulich, 2022)
- Captures spontaneous behaviors in natural environments; yields ecologically valid insights.
- Process: Non-intrusive observation of staff tasks to understand real workflows.

2. Interview (DiCicco-Bloom & Crabtree, 2006; Turner, 2023)
- In-depth, semi-structured interviews to capture preferences and experiences.
- Process: 10 validated questions; distributed to managers, staff, and select clients.

3. Survey (Fowler, 2014; Creswell & Creswell, 2023)
- Quantitative aggregation of participant perceptions and behaviors.
- Procedures: Confidential responses, anonymized identities, one-week response period, no incentives.

### 3.2.3 Design of the Study
Supply chains must prioritize trustworthiness and resilience over mere speed (Ivanov & Dolgui, 2021; Huo, 2024). Digital tools gain strategic importance when deployed to strengthen competitive capability (Lee & Rha, 2023; Gawer & Cusumano, 2022).

System Architecture

Figure 3.2.3 System Architecture

The ON-CARE architecture adopts a layered design: Users, Web Interface, Core System, and Database. Role-based interfaces connect to Django services (Authentication, Cart, Stock, Forecasting), integrating Auto ARIMA forecasting to support predictive, customer-centric supply chain decisions.

Use Case Diagrams

System Administrator
- User Management Module: Manage User Accounts; Control Access Rights; Monitor User Activity; Handle User Issues.
- Report Management Module: Create Reports; Schedule Reports; Distribute Reports; Manage Report Access.

Pharmacist/Admin
- Inventory Management Module: Manage Medicines; Track Stock Levels; Handle Reorder Alerts; Monitor Inventory Status.
- Analytics & Forecasting Module: Generate Forecasts; View Analytics; Monitor Trends; Evaluate Models.

Sales Representatives
- Order Management Module: Manage Orders; Handle Prescriptions; Track Order Status; View Order History.
- Cart Management Module: Manage Shopping Cart; Check Availability; Convert to Order.
- Medicine Catalog Module: Browse Medicines; Search Medicines; View Medicine Details.

System Flowchart

Figure 3.2.3 System Flowchart

High-level flow: Order creation → availability validation → prescription verification → order processing → inventory updates → fulfillment → status tracking → analytics feedback loop for ARIMA forecasting and inventory planning.

### 3.2.4 ARIMA Implementation and Model Evaluation
Auto ARIMA automates model building. Evaluation uses:
- ACF/PACF for lag structure analysis
- Model Selection: AIC, BIC
- Forecast Accuracy: RMSE, MAE, MAPE

Quality thresholds:
- Excellent: MAPE < 5%, AIC < 1000, BIC < 1000
- Good: MAPE 5–15%, AIC 1000–2000, BIC 1000–2000
- Fair: MAPE 15–25%, AIC 2000–3000, BIC 2000–3000
- Poor: MAPE > 25%, AIC > 3000, BIC > 3000

Composite scoring (weights): MAPE 40%, normalized RMSE 30%, AIC 20%, BIC 10%.

### 3.2.5 Testing

Unit Testing (Ali et al., 2024; Smith & Johnson, 2021; Kumar & Lee, 2019; Garcia et al., 2023; Peterson, 2020)
- Verify smallest components via manual/automated tests for correctness and integrity.

User Acceptance Testing (Panaya, 2025; TestDevLab, 2025)
- Validate real-world performance by end users prior to launch.

UAT Test Plan Template
- Testing Start Date: 01-Sep-25
- Testing End Date: 08-Sep-25
- Name of Tester(s): Ace Gutierrez

Columns: Test Case; Data Element; Query Criteria; Expected Results; Pass; Fail; Retest Date; Defect/Comments.

Software Evaluation (ISO/IEC 25010)
- Functional Suitability; Performance Efficiency; Compatibility; Usability; Reliability; Security; Maintainability; Portability.

Likert Scale
- 5: 4.51–5.00 Highly Acceptable
- 4: 3.51–4.00 Moderately Acceptable
- 3: 2.51–3.49 Acceptable
- 2: 1.51–2.49 Slightly Acceptable
- 1: 1.00–1.49 Not Acceptable

---

# Chapter 4
# Results and Discussion

## 4.1 Data Exploration
Figures and summaries (e.g., Metformin dataset summary statistics) demonstrate the dataset scope and revenue totals over 2015–2024.

## 4.2 Stationarity Testing and Seasonal Decomposition
ADF tests and decomposition reveal trends, seasonality, and variance behavior guiding SARIMA modeling.

## 4.3 Model Selection
Auto ARIMA (pmdarima 2.0.4) evaluated 29 configurations; optimal ARIMA(0,1,2)(1,0,0)[12] selected by AIC/BIC/HQIC.

## 4.4 Model Evaluation and Validation
Performance (example): MAPE 5.69%, RMSE 129.34, MAE 111.95, strong seasonal component; supports reliable inventory planning and supply chain decisions.

## 4.5 Software Evaluation using ISO 9126
Summarized Likert outcomes across Functionality, Reliability, Usability, Efficiency, Maintainability, and Portability; Total Mean: 4.57 (Highly Acceptable).

---

# Chapter 5
# Summary, Conclusions, and Recommendations

## 5.1 Summary
Concise summary of research and system outcomes.

## 5.2 Conclusions
Direct statements aligned one-to-one with specific objectives.

## 5.3 Recommendations
Actionable recommendations for deployment, training, and future enhancements.

---

# References (APA format)
- ISO/IEC. (2011). Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models (ISO/IEC 25010:2011). International Organization for Standardization.
- Garcia, M., Smith, J., Patel, A., & Lee, C. (2023). Evaluating usability and functional suitability in health IT: A case study. Journal of Medical Informatics, 45(4), 220–234.
- Li, R., & Chen, W. (2022). Applying ISO 25010 for software quality evaluation in healthcare applications. International Journal of Software Engineering, 29(1), 59–73.
- Patel, R., Singh, A., & Thompson, L. (2024). Software maintainability in microservice architectures: An empirical assessment using ISO/IEC 25010. Software Quality Journal, 32(1), 107–127.
- Chen, F., & Wang, Y. (2023). Performance optimization methods for healthcare software: Metrics and practices. Health Informatics Journal, 29(2), 143–159.
- Martinez, S., & Thompson, J. (2023). Microservices and modular design: Enhancing software maintainability. Journal of Systems Architecture, 48(10), 1276–1291.
- Johnson, L., & Davis, M. (2023). Healthcare data security: Encryption and regulatory compliance. Journal of Cybersecurity, 11(1), 12–29.
- Kim, S., & Taylor, R. (2024). Integrity and auditability in healthcare software systems. International Journal of Health IT, 8(3), 56–72.
- Rodriguez, M., Kim, J., & Park, H. (2023). User experience metrics in healthcare software usability studies. International Journal of Human-Computer Studies, 160, 102727.
- Wilson, C., & Davis, S. (2024). Interoperability in multi-tenant healthcare solutions: A practical approach. Journal of Medical Systems, 48(2), 15.
- DiCicco-Bloom, B., & Crabtree, B. F. (2006). The qualitative research interview. Medical Education, 40(4), 314–321. https://doi.org/10.1111/j.1365-2929.2006.02418.x
- Fowler, F. J. (2014). Survey research methods (5th ed.). Sage Publications.
- Goodwin, C. J. (2020). Research in psychology: Methods and design (8th ed.). Wiley.
- Kawulich, B. B. (2022). Observing participants: Strategies for ethnographic research. Forum: Qualitative Social Research, 7(2). https://doi.org/10.17169/fqs-7.2.1017
- Laurier, E. (2021). Studies of everyday interactions: Changing perspectives. Routledge.
- Creswell, J. W., & Creswell, J. D. (2023). Research design: Qualitative, quantitative, and mixed methods approaches (6th ed.). Sage Publications.
- Turner, D. W. (2023). Qualitative interview design: A practical guide for novice investigators. The Qualitative Report, 28(1), 259–271. https://doi.org/10.46743/2160-3715/2023.2616
- Ivanov, D., & Dolgui, A. (2021). A digital supply chain twin for managing disruption risks and resilience in the era of Industry 4.0. Production Planning & Control, 32(16), 1381–1394. https://doi.org/10.1080/09537287.2020.1761677
- Huo, B. (2024). The impact of supply chain resilience on customer satisfaction and financial performance: Contingency perspective. Journal of Purchasing and Supply Management, 30(2), 100762. https://doi.org/10.1016/j.pursup.2024.100762
- Lee, S., & Rha, J. (2023). Dynamic digital capabilities and their role in sustainable competitive advantage: Evidence from manufacturing SMEs. International Journal of Production Economics, 259, 108074. https://doi.org/10.1016/j.ijpe.2023.108074
- Gawer, A., & Cusumano, M. A. (2022). Platform leadership and ecosystem dynamics in the digital age. Business Strategy Review, 33(3), 47–53. https://doi.org/10.1111/1467-8616.12401
- Lenovo. (2025). LOQ 15IRX9 Specifications. Lenovo. https://www.lenovo.com/ph/en/p/laptops/loq-laptops/lenovo-loq-15irx9/len101q0005

---

# Appendices
5.3.1.1.1 <Appendix A:> <Title>
Place your appendices here. Ensure these are referenced in the document body.

---

# Curriculum Vitae
This section is for dissertations only.
