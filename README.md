CAR RENTAL SYSTEM
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
 -- It is a Python + MySQL-based terminal application that enables efficient vehicle lease operations.
 -- It is a menu driven system which enables users to handle customer data, register and update vehicle information, create and manage leases, process payments, and generate rental insights — all within a structured and modular architecture.


📁 Folder Structure
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
 CarRentalSystem/
│
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
│   ├── DBconnection.py
│   ├── PropertyUtil.py
│   └── db.properties
│
└── db.properties  # (duplicate copy outside 'util', if needed)

