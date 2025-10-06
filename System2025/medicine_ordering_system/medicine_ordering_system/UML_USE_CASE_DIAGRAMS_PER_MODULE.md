# UML Use Case Diagrams Per Module - OnCare Medicine Ordering System

This document contains UML use case diagrams organized by user role and module, showing the general capabilities of each user type within specific functional areas.

## Table of Contents
1. [Sales Representative Modules](#sales-representative-modules)
2. [Pharmacist/Admin Modules](#pharmacistadmin-modules)
3. [System Administrator Modules](#system-administrator-modules)

---

## Sales Representative Modules

### 1.1 Order Management Module - Sales Representative

```plantuml
@startuml Sales_Rep_Order_Management_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title Sales Representative - Order Management Module

actor "Sales Representative" as SR

package "Order Management" {
    usecase "Manage Orders" as UC1
    usecase "Handle Prescriptions" as UC2
    usecase "Track Order Status" as UC3
    usecase "View Order History" as UC4
}

' Define relationships
SR --> UC1 : can do
SR --> UC2 : can do
SR --> UC3 : can do
SR --> UC4 : can do

' Include relationships
UC1 ..> UC2 : includes
UC1 ..> UC3 : includes
UC4 ..> UC3 : includes

' Notes
note right of SR
  Sales Rep Order Management:
  - Create and manage customer orders
  - Handle prescription uploads
  - Track order status
  - View order history
end note

@enduml
```

### 1.2 Cart Management Module - Sales Representative

```plantuml
@startuml Sales_Rep_Cart_Management_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title Sales Representative - Cart Management Module

actor "Sales Representative" as SR

package "Cart Management" {
    usecase "Manage Shopping Cart" as UC1
    usecase "Check Availability" as UC2
    usecase "Convert to Order" as UC3
}

' Define relationships
SR --> UC1 : can do
SR --> UC2 : can do
SR --> UC3 : can do

' Include relationships
UC1 ..> UC2 : includes
UC3 ..> UC1 : includes
UC3 ..> UC2 : includes

' Notes
note right of SR
  Sales Rep Cart Management:
  - Manage customer shopping cart
  - Check medicine availability
  - Convert cart to order
end note

@enduml
```

### 1.3 Medicine Catalog Module - Sales Representative

```plantuml
@startuml Sales_Rep_Medicine_Catalog_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title Sales Representative - Medicine Catalog Module

actor "Sales Representative" as SR

package "Medicine Catalog" {
    usecase "Browse Medicines" as UC1
    usecase "Search Medicines" as UC2
    usecase "View Medicine Details" as UC3
}

' Define relationships
SR --> UC1 : can do
SR --> UC2 : can do
SR --> UC3 : can do

' Include relationships
UC1 ..> UC2 : includes
UC1 ..> UC3 : includes
UC2 ..> UC3 : includes

' Notes
note right of SR
  Sales Rep Medicine Catalog:
  - Browse medicine catalog
  - Search and filter medicines
  - View detailed information
  - Read-only access
end note

@enduml
```

---

## Pharmacist/Admin Modules

### 2.1 Inventory Management Module - Pharmacist/Admin

```plantuml
@startuml Pharmacist_Admin_Inventory_Management_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title Pharmacist/Admin - Inventory Management Module

actor "Pharmacist/Admin" as PA

package "Inventory Management" {
    usecase "Manage Medicines" as UC1
    usecase "Track Stock Levels" as UC2
    usecase "Handle Reorder Alerts" as UC3
    usecase "Monitor Inventory Status" as UC4
}

' Define relationships
PA --> UC1 : can do
PA --> UC2 : can do
PA --> UC3 : can do
PA --> UC4 : can do

' Include relationships
UC1 ..> UC2 : includes
UC2 ..> UC3 : includes
UC4 ..> UC2 : includes
UC4 ..> UC3 : includes

' Notes
note right of PA
  Pharmacist/Admin Inventory:
  - Full medicine management
  - Stock level tracking
  - Reorder alert handling
  - Inventory monitoring
end note

@enduml
```

### 2.2 Analytics and Forecasting Module - Pharmacist/Admin

```plantuml
@startuml Pharmacist_Admin_Analytics_Forecasting_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title Pharmacist/Admin - Analytics and Forecasting Module

actor "Pharmacist/Admin" as PA

package "Analytics and Forecasting" {
    usecase "Generate Forecasts" as UC1
    usecase "View Analytics" as UC2
    usecase "Monitor Trends" as UC3
    usecase "Evaluate Models" as UC4
}

' Define relationships
PA --> UC1 : can do
PA --> UC2 : can do
PA --> UC3 : can do
PA --> UC4 : can do

' Include relationships
UC1 ..> UC4 : includes
UC2 ..> UC3 : includes
UC2 ..> UC4 : includes
UC3 ..> UC1 : includes

' Notes
note right of PA
  Pharmacist/Admin Analytics:
  - Generate demand forecasts
  - View analytics dashboard
  - Monitor sales trends
  - Evaluate forecasting models
end note

@enduml
```

### 2.3 Category Management Module - Pharmacist/Admin

```plantuml
@startuml Pharmacist_Admin_Category_Management_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title Pharmacist/Admin - Category Management Module

actor "Pharmacist/Admin" as PA

package "Category Management" {
    usecase "Manage Categories" as UC1
    usecase "Organize Hierarchy" as UC2
    usecase "Control Access" as UC3
}

' Define relationships
PA --> UC1 : can do
PA --> UC2 : can do
PA --> UC3 : can do

' Include relationships
UC1 ..> UC2 : includes
UC1 ..> UC3 : includes
UC2 ..> UC3 : includes

' Notes
note right of PA
  Pharmacist/Admin Categories:
  - Manage medicine categories
  - Organize category hierarchy
  - Control category access
end note

@enduml
```

---

## System Administrator Modules

### 3.1 User Management Module - System Administrator

```plantuml
@startuml System_Admin_User_Management_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title System Administrator - User Management Module

actor "System Administrator" as SA

package "User Management" {
    usecase "Manage User Accounts" as UC1
    usecase "Control Access Rights" as UC2
    usecase "Monitor User Activity" as UC3
    usecase "Handle User Issues" as UC4
}

' Define relationships
SA --> UC1 : can do
SA --> UC2 : can do
SA --> UC3 : can do
SA --> UC4 : can do

' Include relationships
UC1 ..> UC2 : includes
UC1 ..> UC4 : includes
UC2 ..> UC3 : includes
UC3 ..> UC4 : includes

' Notes
note right of SA
  System Admin User Management:
  - Manage all user accounts
  - Control access rights
  - Monitor user activity
  - Handle user issues
end note

@enduml
```

### 3.2 System Administration Module - System Administrator

```plantuml
@startuml System_Admin_System_Administration_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title System Administrator - System Administration Module

actor "System Administrator" as SA

package "System Administration" {
    usecase "Monitor System Health" as UC1
    usecase "Manage System Maintenance" as UC2
    usecase "Handle System Alerts" as UC3
    usecase "Configure System Settings" as UC4
}

' Define relationships
SA --> UC1 : can do
SA --> UC2 : can do
SA --> UC3 : can do
SA --> UC4 : can do

' Include relationships
UC1 ..> UC3 : includes
UC2 ..> UC1 : includes
UC2 ..> UC3 : includes
UC4 ..> UC1 : includes

' Notes
note right of SA
  System Admin Administration:
  - Monitor system health
  - Manage maintenance
  - Handle alerts
  - Configure settings
end note

@enduml
```

### 3.3 Report Management Module - System Administrator

```plantuml
@startuml System_Admin_Report_Management_Module_General

!theme plain
skinparam packageStyle rectangle
skinparam actorStyle awesome
skinparam usecaseStyle rectangle

title System Administrator - Report Management Module

actor "System Administrator" as SA

package "Report Management" {
    usecase "Create Reports" as UC1
    usecase "Schedule Reports" as UC2
    usecase "Distribute Reports" as UC3
    usecase "Manage Report Access" as UC4
}

' Define relationships
SA --> UC1 : can do
SA --> UC2 : can do
SA --> UC3 : can do
SA --> UC4 : can do

' Include relationships
UC1 ..> UC4 : includes
UC2 ..> UC1 : includes
UC2 ..> UC3 : includes
UC3 ..> UC4 : includes

' Notes
note right of SA
  System Admin Reports:
  - Create custom reports
  - Schedule automated reports
  - Distribute reports
  - Manage report access
end note

@enduml
```

---

## Summary

### Sales Representative Modules (3 modules, 10 total use cases):
1. **Order Management** (4 use cases) - Order management, prescription handling, status tracking
2. **Cart Management** (3 use cases) - Cart management, availability checking, order conversion
3. **Medicine Catalog** (3 use cases) - Browsing, searching, viewing medicine details

### Pharmacist/Admin Modules (3 modules, 11 total use cases):
1. **Inventory Management** (4 use cases) - Medicine management, stock tracking, reorder alerts
2. **Analytics and Forecasting** (4 use cases) - Forecast generation, analytics viewing, trend monitoring
3. **Category Management** (3 use cases) - Category management, hierarchy organization, access control

### System Administrator Modules (3 modules, 12 total use cases):
1. **User Management** (4 use cases) - Account management, access control, activity monitoring
2. **System Administration** (4 use cases) - Health monitoring, maintenance, alert handling, configuration
3. **Report Management** (4 use cases) - Report creation, scheduling, distribution, access management

## Usage Instructions

1. Copy any PlantUML code block into a PlantUML editor
2. Render the diagram to visualize the use cases
3. Use these diagrams for system documentation and requirement analysis
4. Each diagram shows the general capabilities within specific modules for each user role

## Key Features

- **Role-based Access Control**: Each diagram shows what each user role can do within specific modules
- **General Functionality**: Focuses on core capabilities rather than detailed operations
- **Modular Organization**: Separates functionality by system modules
- **Clear Relationships**: Shows include relationships between use cases
- **Comprehensive Coverage**: Covers all major functional areas of the system
