import unittest
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from exceptions.custom_exceptions import *
from entity.Vehicle import Vehicle
from entity.Lease import Lease
from entity.Customer import Customer
from util.PropertyUtil import PropertyUtil
from util.DBconnection import DBConnection

class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        self.repo = ICarLeaseRepositoryImpl()

    def test_create_car(self):
        car = Vehicle(make="Hyundai",model="i20",year=2022,daily_rate=55.0,status="available",passenger_capacity=5,engine_capacity=1.2)
        car_id = self.repo.add_car(car)
        self.assertIsInstance(car_id, int)
        print("Testing create car successfully passed!")

    def test_create_lease(self):
        lease = Lease(customer_id=100,vehicle_id=1,start_date="2025-07-01",end_date="2025-07-07",type="dailylease")
        lease_id = self.repo.create_lease(lease)
        self.assertIsInstance(lease_id, int)
        print("Testing create lease successfully passed!")

    def test_retrieve_lease(self):
        lease_id = 300
        result = self.repo.return_car(lease_id)
        self.assertIsNotNone(result)
        print("Testing retrieve lease successfully passed!")

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            self.repo.find_customer_by_id(9999)

    def test_car_not_found_exception(self):
        with self.assertRaises(CarNotFoundException):
            self.repo.find_car_by_id(9999)

    def test_lease_not_found_exception(self):
        with self.assertRaises(LeaseNotFoundException):
            self.repo.return_car(9999)

    def tearDown(self):
        self.repo.close_conn()

if __name__ == '__main__':
    unittest.main()
