# Business Requirements Documentation 

## 1) Project Overview 
The Enterprise Master Data & Analytics Dashboard is a fictional internal business application designed to centralize and manage key enterprise data, including customers, products, vendors, and sales transactions.

The system is intended to provide employees with a structured way to view and maintain business data while improving data consistency, completeness, and reliability.

The project simulates a real-world enterprise IT environment where master data and transactional data are managed through a centralized relational database and accessed through a business application.

This is an educational project inspired by common enterprise IT, ERP, and data management workflows. It does not represent or use confidential data from any real organization.
## 2) Business Problem 

The organization currently manages customer, product, vendor, and sales information across multiple spreadsheets and manually maintained files.

As the volume of business data increases, several data quality and management problems have emerged. These include duplicate customer records, missing contact information, inconsistent naming conventions, invalid phone numbers, incomplete location data, inactive vendors, and suspicious product values.

The lack of a centralized and structured data management system makes it difficult for employees to maintain accurate records, identify data quality issues, and obtain reliable information for business activities and reporting.

The organization therefore requires a centralized system that can organize enterprise data, enforce appropriate relationships between business entities, and provide a foundation for future data validation, analytics, and reporting.

## 3) Project Objectives 

The objectives of the project are to:

1. Centralize customer, product, vendor, and sales data within a structured relational database.

2. Establish clear relationships between business entities using appropriate primary and foreign keys.

3. Improve the consistency and quality of enterprise master data by identifying duplicate, missing, inconsistent, and invalid records.

4. Provide employees with a simple interface for viewing customer, product, vendor, and sales information.

5. Create a foundation for future data validation, data cleaning, analytics, and reporting capabilities.

6. Demonstrate common enterprise IT concepts, including master data management, transactional data, relational databases, data quality, REST APIs, business processes, and ERP-related workflows.

7. Develop the system using a structured software development process that includes requirements analysis, system design, implementation, testing, documentation, and version control.

## 4) Scope 

### 4.1 In Scope

The initial stage of the project will include:

- Designing a relational database for enterprise data.
- Creating customer master data.
- Creating product master data.
- Creating vendor master data.
- Creating sales transaction data.
- Establishing primary key and foreign key relationships.
- Creating realistic fictional business data.
- Including intentionally messy records to simulate real-world data quality issues.
- Providing a simple interface for viewing customers, products, vendors, and sales transactions.
- Documenting the database design and business requirements.
- Using Git and GitHub for version control.

### 4.2 Future Scope

The following capabilities are planned for later stages:

- SQL practice and interactive SQL exercises.
- Python-based data cleaning and transformation using pandas.
- Automated data-quality validation.
- Data-quality dashboard.
- Executive analytics dashboard.
- REST API development.
- Advanced filtering and reporting.
- ERP and SAP-related business process documentation.
- Project management and action tracking features.
- Automated testing.
- Additional business process simulations.

### 4.3 Out of Scope for the Initial Stage

The initial stage will not include:

- User authentication and authorization.
- Real company or customer data.
- Real SAP system integration.
- Real payment processing.
- Production deployment.
- Advanced analytics or machine learning.
- Automated Python data-cleaning pipelines.

## 5) Stakeholders 

Business users - Use the system to view and manage business data 
Sales Team - Work with customers and sales transactions 
Procurement Team - Work with vendors and products 
Management - Review business information and reports 
IT - Digital Solutions Team 
Data/ ERP Team - Manage enterprise data and business processes. 
Project Manager - Coordinate project activities and stakeholders 

## 6) Business Requirements 
### BR-001 - Centralized Customer Data 
The system shall provide a centralized repository for customer information 
### BR-002 - Centralized Product Data 
The system shall maintain product information 
### BR-003 - Centralized Vendor Data 
The system shall maintain vendor information 
### BR-004 - Sales transaction records 
The system shall maintain sales transaction records 
### BR-005 - Data Relationships 
The system shall establish appropriate relationships between customers, products, vendors and sales 
### BR-006 Data Quality Issues 
The system shall support the identification of common data quality issues 
### BR-007 Transaction Data Viewing 
The system shall provide users with simple interface for viewing sales transactions 
## 7) Assumptions and Constraints 
### 7.1 Assumptions

- The project uses fictional business data for educational purposes.
- Users have basic computer skills and access to the internal application.
- Customer, product, vendor, and sales information can be represented using a relational database.
- The initial system will be used for learning and demonstration rather than production business operations.
- Future system capabilities may be developed in additional project phases.

### 7.2 Constraints

- No real company or customer data will be used.
- The project will not integrate with a real SAP or ERP system.
- The initial stage will focus on database design and basic data viewing.
- Advanced analytics, machine learning, authentication, and production deployment are outside the initial scope.
- The project is developed using a limited set of technologies and resources for educational purposes.

