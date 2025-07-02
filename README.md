CAR RENTAL SYSTEM
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
 -- It is a Python + MySQL-based terminal application that enables efficient vehicle lease operations.
 -- It is a menu driven system which enables users to handle customer data, register and update vehicle information, create and manage leases, process payments, and generate rental insights — all within a structured and modular architecture.


📁 Folder Structure
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
CarRentalSystem/
│
├── dao/
│ ├── init.py
│ ├── ICarLeaseRepository.py
│ └── ICarLeaseRepositoryImpl.py
│
├── db_setup/
│ ├── init.py
│ ├── insert_data.py
│ └── table_creation
│
├── entity/
│ ├── init.py
│ ├── Customer.py
│ ├── Lease.py
│ ├── Payment.py
│ └── Vehicle.py
│
├── exceptions/
│ ├── init.py
│ └── custom_exceptions.py
│
├── mainmodule/
│ ├── init.py
│ └── main.py
│
├── Testing/
│ ├── init.py
│ └── TestCRS.py
│
└── util/
├── db.properties
├── DBconnection.py
└── PropertyUtil.py


