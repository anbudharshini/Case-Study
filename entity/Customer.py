class Customer:
    def __init__(self, first_name:str, last_name:str, email:str, phone_number:str, customer_id:int = None):
        self.__customer_id=customer_id
        self.__first_name=first_name
        self.__last_name=last_name
        self.__email=email
        self.__phone_number=phone_number

    def set_customer_id(self, customer_id: int) -> None:
        self.__customer_id=customer_id

    def set_first_name(self, first_name: str) -> None:
        self.__first_name=first_name

    def set_last_name(self, last_name: str) -> None:
        self.__last_name=last_name

    def set_email(self, email: str) -> None:
        self.__email=email

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number=phone_number

    def get_customer_id(self) -> int:
        return self.__customer_id

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_email(self) -> str:
        return self.__email

    def get_phone_number(self) -> str:
        return self.__phone_number