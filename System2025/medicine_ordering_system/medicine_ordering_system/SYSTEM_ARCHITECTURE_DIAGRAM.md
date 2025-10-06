# ON-CARE System Architecture Diagram

This document contains the basic system architecture diagram for the ON-CARE: A Web-Based Ordering System with Customer-Centric Supply Chain Analytics for Neo Care Philippines.

## System Architecture Overview

```plantuml
@startuml ON_CARE_System_Architecture

!theme plain
skinparam packageStyle rectangle
skinparam componentStyle rectangle
skinparam databaseStyle rectangle

title ON-CARE System Architecture - Neo Care Philippines

' Define layers
package "Presentation Layer" {
    [Web Browser] as Browser
    [Mobile Browser] as Mobile
    [Admin Dashboard] as AdminUI
    [Sales Rep Interface] as SalesUI
    [Pharmacist Interface] as PharmUI
}

package "Application Layer" {
    package "Django Web Framework" {
        [Django Views] as Views
        [Django Templates] as Templates
        [Django Forms] as Forms
        [Django Admin] as Admin
    }
    
    package "API Layer" {
        [REST API] as API
        [Authentication API] as AuthAPI
        [Analytics API] as AnalyticsAPI
        [Order API] as OrderAPI
    }
}

package "Business Logic Layer" {
    package "Order Management" {
        [Order Processing] as OrderProc
        [Cart Management] as CartMgmt
        [Prescription Handling] as PrescHandling
    }
    
    package "Inventory Management" {
        [Stock Management] as StockMgmt
        [Reorder Alerts] as ReorderAlerts
        [Category Management] as CatMgmt
    }
    
    package "Analytics Engine" {
        [ARIMA Forecasting] as ARIMA
        [Data Processing] as DataProc
        [Model Evaluation] as ModelEval
        [Trend Analysis] as TrendAnalysis
    }
    
    package "User Management" {
        [Authentication] as Auth
        [Authorization] as Authz
        [User Profiles] as UserProfiles
    }
}

package "Data Layer" {
    database "SQLite/MySQL" as DB {
        [User Data] as UserData
        [Medicine Catalog] as MedCatalog
        [Order Data] as OrderData
        [Inventory Data] as InventoryData
        [Analytics Data] as AnalyticsData
        [Transaction Data] as TransactionData
    }
    
    [File Storage] as FileStorage
    [Log Files] as Logs
}

package "External Systems" {
    [Email Service] as Email
    [Payment Gateway] as Payment
    [Supplier APIs] as SupplierAPI
    [Reporting Service] as Reporting
}

package "Infrastructure Layer" {
    [Web Server (Apache/Nginx)] as WebServer
    [Application Server] as AppServer
    [Database Server] as DBServer
    [File Server] as FileServer
}

' Define relationships
Browser --> WebServer
Mobile --> WebServer
AdminUI --> WebServer
SalesUI --> WebServer
PharmUI --> WebServer

WebServer --> AppServer
AppServer --> Views
AppServer --> Templates
AppServer --> Forms
AppServer --> Admin

Views --> API
Views --> AuthAPI
Views --> AnalyticsAPI
Views --> OrderAPI

API --> OrderProc
API --> StockMgmt
API --> ARIMA
API --> Auth

AuthAPI --> Auth
AuthAPI --> Authz
AuthAPI --> UserProfiles

AnalyticsAPI --> ARIMA
AnalyticsAPI --> DataProc
AnalyticsAPI --> ModelEval
AnalyticsAPI --> TrendAnalysis

OrderAPI --> OrderProc
OrderAPI --> CartMgmt
OrderAPI --> PrescHandling

OrderProc --> OrderData
CartMgmt --> OrderData
PrescHandling --> FileStorage

StockMgmt --> InventoryData
ReorderAlerts --> InventoryData
CatMgmt --> MedCatalog

ARIMA --> AnalyticsData
DataProc --> AnalyticsData
ModelEval --> AnalyticsData
TrendAnalysis --> AnalyticsData

Auth --> UserData
Authz --> UserData
UserProfiles --> UserData

OrderData --> TransactionData
InventoryData --> TransactionData
AnalyticsData --> TransactionData

FileStorage --> FileServer
Logs --> FileServer

DB --> DBServer

OrderProc --> Email
OrderProc --> Payment
StockMgmt --> SupplierAPI
ARIMA --> Reporting

' Notes
note right of Browser
  Client Access Points:
  - Web browsers for all users
  - Mobile-responsive design
  - Role-based interfaces
end note

note right of ARIMA
  ARIMA Forecasting Engine:
  - Auto parameter selection
  - ACF/PACF analysis
  - Statistical evaluation
  - Demand prediction
end note

note right of DB
  Database Schema:
  - 8 Django applications
  - 47+ tables
  - Role-based access
  - Audit trails
end note

note bottom of External Systems
  External Integrations:
  - Email notifications
  - Payment processing
  - Supplier connectivity
  - Report generation
end note

@enduml
```

## Architecture Components Description

### Presentation Layer
The presentation layer consists of web-based interfaces accessible through standard browsers, with responsive design supporting both desktop and mobile devices. The system provides role-specific interfaces for different user types: Sales Representatives, Pharmacists/Admins, and System Administrators, each tailored to their specific responsibilities and access levels.

### Application Layer
Built on Django web framework, this layer handles the core application logic through views, templates, and forms. The REST API layer provides programmatic access to system functionality, with specialized APIs for authentication, analytics, and order management. Django Admin provides administrative capabilities for system management.

### Business Logic Layer
This layer contains the core business processes organized into four main modules:
- **Order Management**: Handles order processing, cart management, and prescription handling
- **Inventory Management**: Manages stock levels, reorder alerts, and category organization
- **Analytics Engine**: Implements ARIMA forecasting, data processing, and trend analysis
- **User Management**: Handles authentication, authorization, and user profile management

### Data Layer
The system uses SQLite for development and MySQL for production, storing data across multiple tables organized by Django applications. File storage handles prescription images and documents, while log files maintain system audit trails and debugging information.

### External Systems
The system integrates with external services for email notifications, payment processing, supplier connectivity, and report generation, enabling comprehensive business operations and communication.

### Infrastructure Layer
The infrastructure supports the application through web servers (Apache/Nginx), application servers, database servers, and file servers, providing the necessary computing resources for system operation.

## Key Architectural Features

### 1. **Modular Design**
The system follows a modular architecture with clear separation of concerns, enabling maintainability and scalability.

### 2. **Role-Based Access Control**
Each user role has specific interfaces and permissions, ensuring security and operational efficiency.

### 3. **RESTful API Design**
The API layer provides flexible integration capabilities and supports future mobile application development.

### 4. **ARIMA Integration**
The analytics engine is seamlessly integrated into the business logic layer, providing real-time forecasting capabilities.

### 5. **Database Normalization**
The data layer uses a normalized database schema with proper relationships and constraints.

### 6. **External Integration Ready**
The architecture supports integration with external systems for payment processing, supplier management, and reporting.

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Django (Python)
- **Database**: SQLite (Development), MySQL (Production)
- **Web Server**: Apache/Nginx
- **Analytics**: ARIMA (pmdarima), Statsmodels
- **API**: Django REST Framework
- **Authentication**: Django's built-in authentication system

## Security Considerations

- Role-based access control at the application level
- Database-level security with proper user permissions
- File storage security for sensitive documents
- API authentication and authorization
- Audit logging for compliance requirements

This architecture provides a solid foundation for the ON-CARE system, supporting all identified requirements while maintaining scalability, security, and performance standards.
