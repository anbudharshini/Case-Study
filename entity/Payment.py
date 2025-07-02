from datetime import date

class Payment:
    def __init__(self, lease_id:int, amount:float, payment_date:date):
        self.__lease_id = lease_id
        self.__amount = amount
        self.__payment_date = payment_date

    def set_lease_id(self, lease_id: int) -> None:
        self.__lease_id = lease_id

    def set_amount(self, amount: float) -> None:
        self.__amount = amount

    def set_payment_date(self, payment_date: date) -> None:
        self.__payment_date = payment_date

    def get_lease_id(self) -> int:
        return self.__lease_id

    def get_amount(self) -> float:
        return self.__amount

    def get_payment_date(self) -> date:
        return self.__payment_date