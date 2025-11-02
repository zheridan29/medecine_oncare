# ON-CARE: A Web-Based Ordering System with Customer-Centric Supply Chain Analytics for Neo Care Philippines

A Project  
Presented to the Graduate Department  
Information Technology Program  
Technological Institute of the Philippines  

In Partial Fulfillment of the Requirements for the Degree in  
Master in Information and Technology  

Gutierrez, Ace Zheridan  
December 2024

---

# Chapter 1

## 1.1 Introduction
Over the years, internet commerce has significantly impacted the global business environment (Irkinovich, 2022). It enables consumers to buy goods and services online through electronic commerce, a common practice especially among younger generations (Iriani & Andjarwati, 2020). An ordering system manages transactions from order placement to delivery of goods or services (Martinez et al., 2019). Delivery procedure is concerned with the supply chain—how organizations, people, actions, information, and resources coordinate to move products from suppliers to customers (Azzi et al., 2019). Companies analyze transactional data to recommend products or services tailored to customer needs (Boone et al., 2019; Van Nguyen et al., 2020).

Neo Care Philippines faces significant operational challenges in managing its pharmaceutical distribution network. The company relies heavily on manual processes for inventory and order administration, complicating file maintenance and data analysis. Importing pharmaceutical products from international suppliers requires extensive analysis and strategic decision-making. Ensuring pharmaceutical availability across a wide network of hospitals and drugstores is vital—stockouts directly impact sales performance and reputation.

Currently, Neo Care lacks an online platform for order management, limiting its digital presence and competitiveness. Developing ON-CARE will improve operational efficiency and establish a strong digital identity. Managing a nationwide client base is demanding; a system can streamline processes so the company can focus on strategic priorities. An Agile methodology will guide development.

---

## 1.2 Objectives of the Study

### General Objective
Develop a web-based system called “ON-CARE: A Web-Based Ordering System with Customer-Centric Supply Chain Analytics for Neo Care Philippines.”

### Specific Objectives
1. Develop a web-based ordering system for Neo Care Philippines using the Django framework to support product ordering, data management, and analytics.
2. Implement an Auto ARIMA-based forecasting module that automatically selects optimal ARIMA parameters (p, d, q) using ACF and PACF for time series analysis.
3. Evaluate the forecasting model using statistical model selection criteria (AIC, BIC) and accuracy metrics (RMSE, MAE, MAPE).
4. Visualize forecasted demand trends for managerial decision-making.
5. Assess system quality using the ISO 9126 software evaluation standard.

---

## 1.3 Significance of the Study
The project assists Neo Care Philippines in monitoring online transactions and generating sales reports that inform strategic decisions. The system will serve as both an order management platform and a corporate website.

- Neo Care Philippines: Establishes online presence and enhances credibility; supports customer behavior insights to improve relationships and revenue.
- Manager: Generates sales reports based on predictive analytics; supports inventory and product management decisions; clarifies product flows.
- Staff: Provides a user-friendly interface for monitoring client transactions, recording essential data, streamlining record-keeping, and accessing past/current transactions.
- Sales Agents: Offers organized transaction records and product reports to identify viable products by area.
- Clients: Serves as a digital brochure of products, updates, promotions, and features; provides convenient access to medicine information.

---

## 1.4 Scope and Delimitations
The project integrates file management, order processing, and report generation tools. Analytics support supply chain decisions, particularly forecasting import volumes by region to ensure product availability and reliability.

Focus areas include establishing a strong digital presence via a corporate website and enhancing managerial decision-making with analytics-driven reports. Initial deployment will be a one-month test within the Luzon area. Only over-the-counter medicines will be available for online purchase. Analytics will use transactional time series data collected from clients through sales agents.

- Methodology: Agile software development
- Target Completion: September 2025 (testing), full completion by December 2025

### Delimitations
- Geographic Scope: Initial implementation limited to Luzon region
- Product Scope: Over-the-counter medications only
- Data Sources: Transactional time series data from sales agents
- Timeline: Completion by December 2025 with a three-month testing phase before full integration
- Technical Limitations: Dependent on internet connectivity

Primary analytical outputs are Stock and Inventory reports that support supply chain optimization.

---

## 1.5 Value Proposition
For small to medium-sized community pharmacies facing stockouts, overstocking, and manual inventory inefficiencies, ON-CARE integrates real-time web-based order management, automated reorder notifications, and predictive analytics optimized for pharmaceutical supply chains. Leveraging ARIMA algorithms, the system targets 85% forecasting accuracy, enabling optimal stock levels, reduced waste, and enhanced patient satisfaction through consistent medicine availability.

With an estimated development cost of ₱200,000, the system is cost-effective, projecting up to 30% inventory cost reduction and 35% waste reduction, with potential annual savings of ₱600,000 per pharmacy and an estimated 300% ROI in the first year.

---

## 1.6 Itemized Cost Breakdown

| Cost Item | Estimated Cost (₱) | Justification / Details |
|---|---:|---|
| Project Management & Requirements | 20,000 | Planning, research alignment, stakeholder meetings |
| UI/UX Design | 15,000 | Frontend mockups, pharmacist workflow optimization |
| Web Application Development | 60,000 | Backend, frontend coding, integration |
| ARIMA Predictive Analytics Integration | 30,000 | Data cleaning, model coding, testing |
| Real-time Database & Cloud Hosting | 15,000 | Secure cloud services, scalable storage |
| API Integrations (Suppliers, POS, etc.) | 15,000 | External supplier and POS integrations |
| QA Testing & User Training | 20,000 | Quality assurance, pilot testing, staff instruction |
| Cybersecurity & Compliance | 10,000 | Regulatory and data privacy features |
| Support & Maintenance (1st year) | 15,000 | Ongoing bug fixes, feature tuning |
| Hardware/Devices (optional, one-time) | 20,000 | Barcode scanners or tablets for order management |
| Miscellaneous/Contingency | 10,000 | Project overrun, minor enhancements |
| **Total** | **200,000** | Covers complete implementation and pilot rollout |

---

## 1.7 Methodology
The project will follow Agile methodology, enabling iterative development, stakeholder feedback, and incremental delivery aligned with project objectives and timelines.

---

## References (selected)
- Azzi, A., et al. (2019). Supply chain coordination and logistics.
- Boone, T., et al. (2019). Data-driven recommendations.
- Iriani, T., & Andjarwati, T. (2020). E-commerce adoption.
- Irkinovich, A. (2022). Internet commerce trends.
- Martinez, A., et al. (2019). Ordering systems and workflows.
- Van Nguyen, T., et al. (2020). Customer analytics and recommendation systems.
