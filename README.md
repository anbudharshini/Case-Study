🚗 CAR RENTAL SYSTEM

📘 Introduction
------------------
The Car Rental System is a terminal-based Python + MySQL application designed to manage vehicle leasing operations.
It provides a menu-driven interface for efficiently handling customer records, leasing workflows, vehicle inventory, and payment transactions.
The system uses an object-oriented, modular design and connects with a MySQL database to persist and retrieve data.

🎯 Project Objective
------------------------
To create a backend application that manages core operations for a vehicle rental business — including customer onboarding, lease management, vehicle handling, and payment tracking — using a layered architecture.

📁 Directory Structure
--------------------------
```text
CarRentalSystem/
├── dao/
│   ├── __init__.py
│   ├── ICarLeaseRepository.py
│   └── ICarLeaseRepositoryImpl.py
│
├── db_setup/
│   ├── __init__.py
│   ├── insert_data.py
│   └── table_creation
│
├── entity/
│   ├── __init__.py
│   ├── Customer.py
│   ├── Lease.py
│   ├── Payment.py
│   └── Vehicle.py
│
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py
│
├── mainmodule/
│   ├── __init__.py
│   └── main.py
│
├── Testing/
│   ├── __init__.py
│   └── TestCRS.py
│
├── util/
│   ├── db.properties
│   ├── DBconnection.py
│   └── PropertyUtil.py
│
└── db.properties
```
## 🚀 Features

- **👤 Customer Management**  
  Add, update, and manage customer records.

- **🚗 Vehicle Management**  
  Register and update available vehicles.

- **📄 Lease Management**  
  Create leases with start/end dates and link them to specific customers and vehicles.

- **💳 Payment Tracking**  
  Record payment details, retrieve payment history, and generate revenue reports.

- **🛢️ Database Integration**  
  Stores all persistent records using MySQL for data durability.

- **⚠️ Custom Exceptions**  
  Handles invalid operations with clean and descriptive error messages.

- **🧩 Modular Design**  
  Organized into clear packages like `entity`, `dao`, `exception`, `util`, and `mainmodule`.

- **✅ Unit Testing**  
  Includes test cases for validating critical modules and operations.


📈 Application Workflow
-------------------------
1. 👤 **Customer Management**
- `Add New Customer`
- `Update Customer Details`
- `Fetch Customer by ID`
- `Delete Customer`
- `List All Customers`

2. 🚗 **Vehicle Management**
- `Add New Vehicle`
- `Update Vehicle Status`
- `Get Vehicle by ID`
- `Remove Vehicle`
- `List Available Vehicles`

3. 📄 **Lease Management**
- `Create Lease Agreement`
- `View Lease by Customer ID`
- `Update Lease Details`
- `Calculate Lease Cost`
- `List All Lease Records`

4. 💳 **Payment Processing**
- `Record Payment`
- `View Payment History by Customer`
- `Generate Payment Receipt`
- `List All Payments`
- `Compute Total Revenue`

5. 🛠️ **Database Setup & Utilities**
- `Initialize Database Schema`
- `Insert Initial Data`
- `Manage DB Connection`
- `Load Properties from File`

💻 Technologies Used
------------------------
>>Language: Python 

>>Database: MySQL 

>>IDE: PyCharm / VS Code

✅ Prerequisites:
----------------
```text
>>pip install mysql-connector-python

>>pip install tabulate
```






