from entity.Customer import Customer
from entity.Vehicle import Vehicle
from entity.Lease import Lease
from entity.Payment import Payment
from datetime import date
from dao.ICarLeaseRepository import ICarLeaseRepository
from exceptions.custom_exceptions import *
from util.DBconnection import *

class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self) -> None:
        self.conn = DBConnection.getConnection()
        print("Debug: repo.conn =", self.conn)
        self.cursor = self.conn.cursor()

    def add_car(self, vehicle: Vehicle) -> int:
        try:
            self.cursor.execute("""insert into Vehicle(make, model, year, dailyrate, status, passengercapacity, enginecapacity)
                values(%s, %s, %s, %s, %s, %s, %s);""",(vehicle.get_make(), vehicle.get_model(), vehicle.get_year(),vehicle.get_daily_rate(), vehicle.get_status(), vehicle.get_passenger_capacity(),vehicle.get_engine_capacity()))
            self.conn.commit()
            vehicle_id=self.cursor.lastrowid
            return vehicle_id
        except Exception as e:
            self.conn.rollback()
            print("Error Occurred,", str(e))

    def remove_car(self, vehicle_id: int) -> None:
        try:
            self.cursor.execute("delete from Vehicle where vehicleID=%s;",(vehicle_id,))
            if self.cursor.rowcount == 0:
                raise CarNotFoundException(vehicle_id)
            self.conn.commit()
            print("Vehicle Removed Successfully!!\n")
        except CarNotFoundException as e:
            print(e)
        except Exception as e:
            self.conn.rollback()
            print("Error Occurred,", str(e))

    def list_available_cars(self):
        try:
            self.cursor.execute("select * from Vehicle where status='available';")
            available_cars = []
            for row in self.cursor.fetchall():
                vehicle_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity = row
                vehicle = Vehicle(make=make, model=model, year=year, daily_rate=daily_rate, status=status,
                                  passenger_capacity=passenger_capacity, engine_capacity=engine_capacity,
                                  vehicle_id=vehicle_id)
                available_cars.append(vehicle)
            return available_cars
        except Exception as e:
            print("Error occurred while Fetching Available Cars,", str(e))
            return []

    def list_rented_cars(self):
        try:
            self.cursor.execute("select * from Vehicle where status!='available';")
            rented_cars = []
            for row in self.cursor.fetchall():
                vehicle_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity = row
                vehicle = Vehicle(make=make, model=model, year=year, daily_rate=daily_rate, status=status,
                                  passenger_capacity=passenger_capacity, engine_capacity=engine_capacity,
                                  vehicle_id=vehicle_id)
                rented_cars.append(vehicle)
            return rented_cars
        except Exception as e:
            print("Error occurred while Fetching Not Available Cars,",str(e))
            return []

    def find_car_by_id(self, vehicle_id: int) -> Vehicle:
        try:
            self.cursor.execute("select * from Vehicle where vehicleID=%s;",(vehicle_id,))
            row = self.cursor.fetchone()
            if row is None:
                raise CarNotFoundException(vehicle_id)
            return Vehicle(vehicle_id=row[0], make=row[1], model=row[2], year=row[3], daily_rate=row[4],
                           status=row[5], passenger_capacity=row[6], engine_capacity=row[7])
        except CarNotFoundException as e:
            raise
        except Exception as e:
            print("Error occurred,", str(e))
            return None

    def add_customer(self, customer: Customer) -> None:
        try:
            self.cursor.execute("""insert into Customer(firstname, lastname, email, phonenumber)values(%s, %s, %s, %s);""",
                (customer.get_first_name(), customer.get_last_name(), customer.get_email(),customer.get_phone_number()))
            self.conn.commit()
            print("Customer Added Successfully!!\n")
        except Exception as e:
            self.conn.rollback()
            print("Error occurred,", str(e))

    def remove_customer(self, customer_id: int) -> None:
        try:
            self.cursor.execute("delete from Customer where customerID=%s;",(customer_id,))
            if self.cursor.rowcount == 0:
                raise CustomerNotFoundException(customer_id)
            self.conn.commit()
            print("Customer Removed Successfully!!\n")
        except CustomerNotFoundException as e:
            print(e)
        except Exception as e:
            self.conn.rollback()
            print("Error occurred,", str(e))

    def list_customers(self) -> list[Customer]:
        try:
            self.cursor.execute("select * from Customer;")
            customers = []
            for row in self.cursor.fetchall():
                customer_id, first_name, last_name, email, phone_number = row
                customer = Customer(customer_id=customer_id, first_name=first_name, last_name=last_name, email=email,phone_number=phone_number)
                customers.append(customer)
            return customers
        except Exception as e:
            print("Error occurred,", str(e))
            return []

    def find_customer_by_id(self, customer_id: int) -> Customer:
        try:
            self.cursor.execute("select * from Customer where customerID = %s;",(customer_id,))
            row = self.cursor.fetchone()
            if row is None:
                raise CustomerNotFoundException(customer_id)
            return Customer(*row)
        except CustomerNotFoundException as e:
            raise
        except Exception as e:
            print("Error occurred,", str(e))
            return None

    def create_lease(self, lease: Lease) -> int:
        try:
            self.cursor.execute("""insert into Lease (vehicleid, customerid, startdate, enddate, type)values (%s, %s, %s, %s, %s);""",
                (lease.get_vehicle_id(), lease.get_customer_id(), lease.get_start_date(),lease.get_end_date(), lease.get_type()))
            self.conn.commit()
            lease_id=self.cursor.lastrowid
            return lease_id
        except Exception as e:
            self.conn.rollback()
            print("Error occurred,", str(e))

    def return_car(self, lease_id: int):
        try:
            self.cursor.execute("select * from Lease where leaseID = %s;", (lease_id,))
            row = self.cursor.fetchone()
            if row is None:
                raise LeaseNotFoundException(lease_id)
            return row
        except LeaseNotFoundException as e:
            raise
        except Exception as e:
            self.conn.rollback()
            print("Error occurred,", str(e))
            return None

    def list_active_leases(self) -> list[Lease]:
        try:
            start_date = input("Enter Start Date(YYYY-MM-DD): ")
            self.cursor.execute("select * from Lease where startDate = %s;", (start_date,))
            return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print("Error occurred,", str(e))

    def list_lease_history(self) -> list[Lease]:
        try:
            self.cursor.execute("select * from Lease;")
            return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print("Error occurred,", str(e))
            return []

    def record_payment(self, payment: Payment) -> None:
        try:
            self.cursor.execute("""insert into Payment (leaseid, paymentdate, amount) values (%s, %s, %s);""",
                (payment.get_lease_id(), payment.get_payment_date(), payment.get_amount()))
            self.conn.commit()
            print("Payment Recorded Successfully!!\n")
        except Exception as e:
            self.conn.rollback()
            print("Error occurred,", str(e))

    def update_customer(self, customer: Customer) -> None:
        try:
            sql = """update customer set firstname = %s, lastname = %s, email = %s, phonenumber = %s where customerID = %s"""
            values=(customer.get_first_name(),customer.get_last_name(),customer.get_email(),customer.get_phone_number(),customer.get_customer_id())
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Customer updated successfully!\n")
        except Exception as e:
            self.conn.rollback()
            print("Error occurred while updating customer,", str(e))

    def update_car_status(self, carID: int, new_status: str) -> None:
        try:
            self.cursor.execute("update vehicle set status = %s where vehicleID = %s", (new_status, carID))
            self.conn.commit()
            print("Vehicle status updated successfully!\n")
        except Exception as e:
            self.conn.rollback()
            print("Error occurred while updating vehicle status,", str(e))

    def get_payment_history_by_customer(self, customerID: int):
        try:
            self.cursor.execute("""
                select p.paymentID, p.paymentDate, p.amount, l.leaseID from payment p
                join lease l ON p.leaseID = l.leaseID
                where l.customerID = %s""", (customerID,))
            return self.cursor.fetchall()
        except Exception as e:
            print("Error occurred while fetching payment history,", str(e))
            return []

    def get_total_revenue(self) -> float:
        try:
            self.cursor.execute("select sum(amount) from payment")
            result = self.cursor.fetchone()
            return result[0] if result and result[0] else 0.0
        except Exception as e:
            print("Error occurred while calculating total revenue,", str(e))
            return 0.0

    def find_lease_by_customer_and_vehicle(self, customer_id: int, vehicle_id: int):
        try:
            self.cursor.execute("""select * from Lease where customerID = %s and vehicleID = %s""", (customer_id, vehicle_id))
            row = self.cursor.fetchone()
            if row:
                return Lease(lease_id=row[0],vehicle_id=row[1],customer_id=row[2],start_date=row[3],end_date=row[4],type=row[5])
            else:
                print("No lease found for this customer and vehicle.")
                return None
        except Exception as e:
            print("Error occurred while fetching lease,", str(e))
            return None

    def update_payment(self, payment_id: int, new_date: str, new_amount: float) -> None:
        try:
            self.cursor.execute(
                "update Payment set paymentDate = %s, amount = %s where paymentID = %s",(new_date, new_amount, payment_id))
            if self.cursor.rowcount == 0:
                print(f"No payment found with ID {payment_id}.")
            else:
                self.conn.commit()
                print("Payment updated successfully!\n")
        except Exception as e:
            self.conn.rollback()
            print("Error occurred while updating payment,", str(e))

    def update_vehicle(self, vehicle: Vehicle) -> None:
        try:
            self.cursor.execute("""update vehicle set make = %s, model = %s, year = %s, dailyrate = %s, status = %s,passengercapacity = %s, enginecapacity = %s
                where vehicleID = %s""", (vehicle.get_make(),vehicle.get_model(),vehicle.get_year(),vehicle.get_daily_rate(),vehicle.get_status(),vehicle.get_passenger_capacity(),vehicle.get_engine_capacity(),
                vehicle.get_vehicle_id()))
            if self.cursor.rowcount == 0:
                print(f"No vehicle found with ID {vehicle.get_vehicle_id()}")
            else:
                self.conn.commit()
                print("Vehicle updated successfully!\n")
        except Exception as e:
            self.conn.rollback()
            print("Error occurred while updating vehicle,", str(e))

    def get_lease_count_by_customer_id(self, customer_id: int):
        try:
            self.cursor.execute("""select count(*) from lease where customerID = %s""",(customer_id,))
            result = self.cursor.fetchone()
            return result[0] if result else 0
        except Exception as e:
            print("Error fetching lease count by customer ID,", str(e))
            return 0

    def close_conn(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            DBConnection.connection = None

