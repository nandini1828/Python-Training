from day1.models.bank_account import BankAccount
from day1.models.vehicle import Car
from day1.models.animal import Dog

def main():

    account = BankAccount(1000)
    print(account.get_balance())

    car = Car()
    car.start()

    dog = Dog("Buddy")
    dog.eat()
    dog.bark()


if __name__ == "__main__":
    main()