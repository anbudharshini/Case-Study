🚗 CAR RENTAL SYSTEM

📘 Introduction
------------------
The Car Rental System is a terminal-based Python + MySQL application designed to manage vehicle leasing operations.
It provides a menu-driven interface for efficiently handling customer records, leasing workflows, vehicle inventory, and payment transactions.
The system uses an object-oriented, modular design and connects with a MySQL database to persist and retrieve data.

🎯 Project Objective
------------------------
To create a backend application that manages core operations for a vehicle rental business — including customer onboarding, lease management, vehicle handling, and payment tracking — using a layered architecture.

🔧 Features
--------------
Customer Management: Add, update, and manage customer records.

Vehicle Management: Register and update available vehicles.

Lease Management: Create leases with start/end dates and linked customers/vehicles.

Payment Tracking: Record and retrieve payment history and generate revenue reports.

Database Integration: Stores persistent records using MySQL.

Custom Exceptions: Graceful error handling for invalid operations.

Modular Design: Clean separation of concerns using packages like entity, dao, exception, util, and mainmodule.

Unit Testing: Includes test cases for key components.

⚙️ How It Works
-------------------
The system launches with a CLI-based menu from main.py.

Based on user input, appropriate services (DAO methods) are triggered.

All data transactions are executed via SQL through MySQL Connector.

Data classes represent real-world objects (Customer, Vehicle, Lease, Payment).

Validations and exceptions are enforced across all user actions.

💻 Technologies Used
------------------------
>>Language: Python 

>>Database: MySQL 

>>IDE: PyCharm / VS Code

Prerequisites:
----------------
>>pip install mysql-connector-python
>>pip install tabulate

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




