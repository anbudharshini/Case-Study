import re
from tabulate import tabulate
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from datetime import date
from exceptions.custom_exceptions import *
from entity.Customer import Customer
from entity.Vehicle import Vehicle
from entity.Lease import Lease
from entity.Payment import Payment
from util.DBconnection import DBConnection

class CarLeaseMenu:
    def __init__(self):
        self.repoimpl = ICarLeaseRepositoryImpl()

    def display_menu(self):
        print("\nCar Rental System Menu:")
        print("1. Add a New Car")
        print("2. Remove a Car")
        print("3. List Available Cars")
        print("4. List Rented Cars")
        print("5. Find Car by ID")
        print("6. Add a New Customer")
        print("7. Remove a Customer")
        print("8. List Customers")
        print("9. Find Customer by ID")
        print("10. Create a Lease")
        print("11. Find Leased Car by ID")
        print("12. List Active Leases")
        print("13. List Lease History")
        print("14. Record Payment")
        print("15. Update Customer Details")
        print("16. Update Car Status")
        print("17. View Payment History by Customer")
        print("18. View Total Revenue")
        print("19. Find Lease by Customer ID and Vehicle ID")
        print("20. Update Payment")
        print("21. Update Vehicle Details")
        print("22. View Lease Count by Customer ID")
        print("23. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your Choice: ")
            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.remove_car()
            elif choice == '3':
                self.list_available_cars()
            elif choice == '4':
                self.list_rented_cars()
            elif choice == '5':
                self.find_car_by_id()
            elif choice == '6':
                self.add_customer()
            elif choice == '7':
                self.remove_customer()
            elif choice == '8':
                self.list_customers()
            elif choice == '9':
                self.find_customer_by_id()
            elif choice == '10':
                self.create_lease()
            elif choice == '11':
                self.return_car()
            elif choice == '12':
                self.list_active_leases()
            elif choice == '13':
                self.list_lease_history()
            elif choice == '14':
                self.record_payment()
            elif choice == '15':
                self.update_customer()
            elif choice == '16':
                self.update_car_status()
            elif choice == '17':
                self.view_payment_history()
            elif choice == '18':
                self.get_total_revenue()
            elif choice == '19':
                self.find_lease_by_customer_and_vehicle()
            elif choice == '20':
                self.update_payment()
            elif choice == '21':
                self.update_vehicle()
            elif choice == '22':
                self.view_lease_count_by_customer_id()
            elif choice == '23':
                print("\nExited!!!")
                self.repoimpl.close_conn()
                break
            else:
                print("Invalid Choice.Please try again.")

    def add_car(self):
        make = input("Enter Company Name: ")
        model = input("Enter Model: ")
        year = int(input("Enter Year: "))
        daily_rate = float(input("Enter Daily Rate: "))
        available = input("Enter Status (available, notAvailable): ")
        passenger_capacity = int(input("Enter Passenger Capacity: "))
        engine_capacity = float(input("Enter Engine Capacity: "))
        vehicle = Vehicle(make=make, model=model, year=year, daily_rate=daily_rate, status=available,
                          passenger_capacity=passenger_capacity, engine_capacity=engine_capacity)
        self.repoimpl.add_car(vehicle)
        print("Car added successfully")

    def remove_car(self):
        vehicle_id = int(input("Enter Vechicle ID: "))
        self.repoimpl.remove_car(vehicle_id)

    def list_available_cars(self):
        available_cars = self.repoimpl.list_available_cars()
        if not available_cars:
            print("Available Cars Not Found!")
        else:
            data = []
            for car in available_cars:
                data.append([
                    car.get_vehicle_id(),
                    car.get_make(),
                    car.get_model(),
                    car.get_year(),
                    car.get_daily_rate(),
                    car.get_status(),
                    car.get_passenger_capacity(),
                    car.get_engine_capacity()
                ])
            headers = ["Vehicle ID", "Make", "Model", "Year", "Daily Rate", "Status", "Capacity", "Engine"]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

    def list_rented_cars(self):
        rented_cars = self.repoimpl.list_rented_cars()
        if not rented_cars:
            print("Rented Cars Not Found!")
        else:
            headers = ["Vehicle ID", "Make", "Model", "Year", "Daily Rate", "Status", "Passenger Capacity",
                       "Engine Capacity"]
            data = [
                [
                    car.get_vehicle_id(),
                    car.get_make(),
                    car.get_model(),
                    car.get_year(),
                    car.get_daily_rate(),
                    car.get_status(),
                    car.get_passenger_capacity(),
                    car.get_engine_capacity()
                ]
                for car in rented_cars
            ]
            print(tabulate(data, headers=headers, tablefmt="grid"))

    def find_car_by_id(self):
        vehicle_id = int(input("Enter Vehicle ID: "))
        car = self.repoimpl.find_car_by_id(vehicle_id)
        if car:
            print("Vehicle ID:", car.get_vehicle_id())
            print("Make:", car.get_make())
            print("Model:", car.get_model())
            print("Year:", car.get_year())
            print("Daily Rate:", car.get_daily_rate())
            print("Available:", car.get_status())
            print("Passenger Capacity:", car.get_passenger_capacity())
            print("Engine Capacity:", car.get_engine_capacity())
        else:
            print("Car Not Found!!")

    def add_customer(self):
        while True:
            fname = input("Enter First Name: ")
            if re.match(r"^[A-Za-z]{2,}$", fname):
                break
            else:
                print("Invalid First Name.Only letters, at least 2 characters.")

        while True:
            lname = input("Enter Last Name: ")
            if re.match(r"^[A-Za-z]{2,}$", lname):
                break
            else:
                print("Invalid Last Name.Only letters, at least 2 characters.")

        while True:
            email = input("Enter Email: ")
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                break
            else:
                print("Invalid Email Format.Try again.")

        while True:
            phn = input("Enter Phone Number: ")
            if re.match(r"^[6-9]\d{9}$", phn):
                break
            else:
                print("Invalid Phone Number.Enter 10-digit number starting with 6–9.")

        customer = Customer(first_name=fname, last_name=lname, email=email, phone_number=phn)
        self.repoimpl.add_customer(customer)

    def remove_customer(self):
        customer_id = int(input("Enter Customer ID: "))
        self.repoimpl.remove_customer(customer_id)

    def list_customers(self):
        customers = self.repoimpl.list_customers()
        if customers:
            headers = ["Customer ID", "First Name", "Last Name", "Email", "Phone Number"]
            data = [
                [
                    customer.get_customer_id(),
                    customer.get_first_name(),
                    customer.get_last_name(),
                    customer.get_email(),
                    customer.get_phone_number()
                ]
                for customer in customers
            ]
            print("\nList of Customers:")
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("No Customers Found!!")

    def find_customer_by_id(self):
        customer_id = int(input("\nEnter the Customer ID to Find: "))
        customer = self.repoimpl.find_customer_by_id(customer_id)
        if customer:
            print("Customer Found:")
            print("Customer ID:", customer.get_customer_id())
            print("First Name:", customer.get_first_name())
            print("Last Name:", customer.get_last_name())
            print("Email:", customer.get_email())
            print("Phone Number:", customer.get_phone_number())

    def create_lease(self):
        customer_id = int(input("Enter Customer ID: "))
        vehicle_id = int(input("Enter Vehicle ID: "))
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")
        type = input("Enter Type ('DailyLease', 'MonthlyLease'): ")
        lease = Lease(customer_id=customer_id, vehicle_id=vehicle_id, start_date=start_date, end_date=end_date,
                      type=type)
        self.repoimpl.create_lease(lease)

    def return_car(self):
        lease_id = int(input("Enter the Lease ID to Find: "))
        lease = self.repoimpl.return_car(lease_id)
        if lease:
            print("Lease ID:", lease[0])
            print("Customer ID:", lease[1])
            print("Vehicle ID:", lease[2])
            print("Start Date:", lease[3])
            print("End Date:", lease[4])
            print("Type:", lease[5])
        else:
            print("No Lease Found!!")
        print("Select the Option From Below:")

    def list_active_leases(self):
        lease = self.repoimpl.list_active_leases()
        if lease:
            headers = ["Lease ID", "Customer ID", "Vehicle ID", "Start Date", "End Date", "Type"]
            print("\nActive Leases:")
            print(tabulate(lease, headers=headers, tablefmt="grid"))
        else:
            print("No Lease Found!!")
        print("Select the Option From Below:")

    def list_lease_history(self):
        lease = self.repoimpl.list_lease_history()
        if lease:
            headers = ["Lease ID", "Customer ID", "Vehicle ID", "Start Date", "End Date", "Type"]
            print("\nLease History:")
            print(tabulate(lease, headers=headers, tablefmt="grid"))
        else:
            print("No Lease Found!!")
        print("Select the Option From Below:")

    def record_payment(self):
        try:
            lease_id = int(input("Enter Lease ID: "))
            transaction_date = input("Enter Transaction Date (YYYY-MM-DD): ")
            amount = float(input("Enter Payment Amount: "))
            lease = self.repoimpl.return_car(lease_id)
            if lease:
                pay = Payment(lease_id=lease_id, payment_date=transaction_date, amount=amount)
                self.repoimpl.record_payment(pay)
            else:
                print("Invalid Lease ID!!")
        except ValueError:
            print("Please Enter Valid Input for Payment ID, Lease ID, and Amount.")
        except Exception as e:
            print("Failed to Record Payment!,", str(e))

    def update_customer(self):
        cid = int(input("Enter Customer ID to Update: "))
        fname = input("Enter New First Name: ")
        lname = input("Enter New Last Name: ")

        while True:
            email = input("Enter New Email: ")
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                break
            else:
                print("Invalid Email Format.Try again.")

        while True:
            phone = input("Enter New Phone Number: ")
            if re.match(r"^[6-9]\d{9}$", phone):
                break
            else:
                print("Invalid Phone Number.Enter 10-digit number starting with 6–9.")

        customer = Customer(customer_id=cid, first_name=fname, last_name=lname, email=email, phone_number=phone)
        self.repoimpl.update_customer(customer)

    def update_car_status(self):
        car_id = int(input("Enter Car ID to Update Status: "))
        status = input("Enter New Status (available/notavailable): ")
        self.repoimpl.update_car_status(car_id, status)

    def view_payment_history(self):
        cid = int(input("Enter Customer ID to View Payment History: "))
        history = self.repoimpl.get_payment_history_by_customer(cid)
        if history:
            headers = ["Payment ID", "Payment Date", "Amount (₹)", "Lease ID"]
            print("\nPayment History:")
            print(tabulate(history, headers=headers, tablefmt="grid"))
        else:
            print("No Payment History Found.")

    def get_total_revenue(self):
        total = self.repoimpl.get_total_revenue()
        print(f"Total Revenue Collected: ₹{total:.2f}")

    def find_lease_by_customer_and_vehicle(self):
        try:
            customer_id = int(input("Enter Customer ID: "))
            vehicle_id = int(input("Enter Vehicle ID: "))
            lease = self.repoimpl.find_lease_by_customer_and_vehicle(customer_id, vehicle_id)
            if lease:
                print("Lease Found:")
                print("Lease ID:", lease.get_lease_id())
                print("Customer ID:", lease.get_customer_id())
                print("Vehicle ID:", lease.get_vehicle_id())
                print("Start Date:", lease.get_start_date())
                print("End Date:", lease.get_end_date())
                print("Type:", lease.get_type())
            else:
                print("No lease found for the given Customer ID and Vehicle ID.")
        except ValueError:
            print("Invalid input. Please enter numeric IDs.")
        except Exception as e:
            print("Error:", str(e))

    def update_payment(self):
        try:
            pid = int(input("Enter Payment ID to Update: "))
            new_date = input("Enter New Payment Date (YYYY-MM-DD): ")
            new_amount = float(input("Enter New Payment Amount: "))
            self.repoimpl.update_payment(pid, new_date, new_amount)
        except ValueError:
            print("Invalid input! Please enter numeric Payment ID and valid amount.")
        except Exception as e:
            print("Error:", str(e))

    def update_vehicle(self):
        try:
            vid = int(input("Enter Vehicle ID to Update: "))
            make = input("Enter New Company Name: ")
            model = input("Enter New Model: ")
            year = int(input("Enter New Year: "))
            daily_rate = float(input("Enter New Daily Rate: "))
            status = input("Enter New Status (available/notavailable): ")
            passenger_capacity = int(input("Enter New Passenger Capacity: "))
            engine_capacity = float(input("Enter New Engine Capacity: "))

            updated_vehicle = Vehicle(vehicle_id=vid,make=make,model=model,year=year,daily_rate=daily_rate,status=status,passenger_capacity=passenger_capacity,
                engine_capacity=engine_capacity)
            self.repoimpl.update_vehicle(updated_vehicle)
        except ValueError:
            print("Invalid input type! Please enter correct values.")
        except Exception as e:
            print("Error:", str(e))

    def view_lease_count_by_customer_id(self):
        try:
            cid = int(input("Enter Customer ID: "))
            count = self.repoimpl.get_lease_count_by_customer_id(cid)
            print(f"Customer ID: {cid} has {count} leases.")
        except ValueError:
            print("Please enter a valid numeric Customer ID.")

if __name__ == "__main__":
    menu = CarLeaseMenu()
    menu.run()