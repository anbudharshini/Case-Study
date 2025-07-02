from abc import ABC, abstractmethod
from datetime import date
from entity.Vehicle import Vehicle
from entity.Customer import Customer
from entity.Lease import Lease
from entity.Payment import Payment


class ICarLeaseRepository(ABC):
    @abstractmethod
    def add_car(self, Vehicle: Vehicle) -> None:
        """Add a new car to the repository."""
    @abstractmethod
    def remove_car(self, vehicle_id: int) -> None:
        """Remove a car from the repository."""
    @abstractmethod
    def list_available_cars(self) -> list[Vehicle]:
        """Get a list of all available cars."""
    @abstractmethod
    def list_rented_cars(self) -> list[Vehicle]:
        """Get a list of all rented cars."""
    @abstractmethod
    def find_car_by_id(self, Vehicle_id: int) -> Vehicle:
        """Find a car in the repository by its ID."""
    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        """Add a new customer to the repository."""
    @abstractmethod
    def remove_customer(self, customer_id: int) -> None:
        """Remove a customer from the repository."""
    @abstractmethod
    def list_customers(self) -> list[Customer]:
        """Get a list of all customers."""
    @abstractmethod
    def find_customer_by_id(self, customer_id: int) -> Customer:
        """Find a customer in the repository by their ID."""
    @abstractmethod
    def create_lease(self, lease: Lease) -> Lease:
        """Create a new lease for a customer with a car."""
    @abstractmethod
    def return_car(self, lease_id: int) -> Lease:
        """Return a leased car."""
    @abstractmethod
    def list_active_leases(self) -> list[Lease]:
        """Get a list of all active leases."""
    @abstractmethod
    def list_lease_history(self) -> list[Lease]:
        """Get a list of all lease history."""
    @abstractmethod
    def record_payment(self, Payment: Payment) -> None:
        """Record a payment for a lease."""

    @abstractmethod
    def find_lease_by_customer_and_vehicle(self, customer_id: int, vehicle_id: int):
        """Find lease by customer ID and vehicle ID."""

    @abstractmethod
    def update_payment(self, payment_id: int, new_date: str, new_amount: float) -> None:
        """Update payment date and amount by payment ID."""

    @abstractmethod
    def update_vehicle(self, vehicle: Vehicle) -> None:
        """Update details of a vehicle."""

    @abstractmethod
    def get_lease_count_by_customer_id(self, customer_id: int):
        """Returns number of leases for a given customer ID."""







