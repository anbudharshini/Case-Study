from datetime import date

class Lease:
    def __init__(self, vehicle_id:int, customer_id:int, start_date:date, end_date:date, type:str, lease_id=None):
        self.__lease_id=lease_id
        self.__vehicle_id=vehicle_id
        self.__customer_id=customer_id
        self.__start_date=start_date
        self.__end_date=end_date
        self.__type=type

    # Setters
    def set_lease_id(self, lease_id: int) -> None:
        self.__lease_id=lease_id

    def set_vehicle_id(self, vehicle_id: int) -> None:
        self.__vehicle_id=vehicle_id

    def set_customer_id(self, customer_id: int) -> None:
        self.__customer_id=customer_id

    def set_start_date(self, start_date: date) -> None:
        self.__start_date=start_date

    def set_end_date(self, end_date: date) -> None:
        self.__end_date=end_date

    def set_lease_type(self, type: str) -> None:
        self.__type=type

    def get_lease_id(self) -> int:
        return self.__lease_id

    def get_vehicle_id(self) -> int:
        return self.__vehicle_id

    def get_customer_id(self) -> int:
        return self.__customer_id

    def get_start_date(self) -> date:
        return self.__start_date

    def get_end_date(self) -> date:
        return self.__end_date

    def get_type(self) -> str:
        return self.__type