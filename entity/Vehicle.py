class Vehicle:
    def __init__(self, make:str, model:str, year:int, daily_rate:float, status:str, passenger_capacity:int,
                 engine_capacity:float, vehicle_id=None):
        self.__vehicle_id = vehicle_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__daily_rate = daily_rate
        self.__status = status
        self.__passenger_capacity = passenger_capacity
        self.__engine_capacity = engine_capacity

    def set_vehicle_id(self, vehicle_id: int) -> None:
        self.__vehicle_id = vehicle_id

    def set_make(self, make: str) -> None:
        self.__make = make

    def set_model(self, model: str) -> None:
        self.__model = model

    def set_year(self, year: int) -> None:
        self.__year = year

    def set_daily_rate(self, daily_rate: float) -> None:
        self.__daily_rate = daily_rate

    def set_passenger_capacity(self, passenger_capacity: int) -> None:
        self.__passenger_capacity = passenger_capacity

    def set_engine_capacity(self, engine_capacity: float) -> None:
        self.__engine_capacity = engine_capacity

    def set_status(self, status) -> None:
        self.__status = status

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_daily_rate(self):
        return self.__daily_rate

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def get_engine_capacity(self):
        return self.__engine_capacity

    def get_status(self):
        return self.__status