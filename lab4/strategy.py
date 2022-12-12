from abc import ABC, abstractmethod


# strategy interface
class CoffeeMachine(ABC):
    @staticmethod
    @abstractmethod
    def make_coffee():
        pass


# context class
class Coffee:
    def __init__(self, coffee_type: CoffeeMachine):
        self.__coffee_type = coffee_type

    @property
    def coffee_type(self):
        return self.__coffee_type

    @coffee_type.setter
    def coffee_type(self, coffee_type: CoffeeMachine):
        self.__coffee_type = coffee_type

    def lets_drink_coffee(self):
        self.__coffee_type.make_coffee()


# concrete strategy
class Americano(CoffeeMachine):
    @staticmethod
    def make_coffee():
        print('Coffee machine made Americano\n')


# concrete strategy
class Latte(CoffeeMachine):
    @staticmethod
    def make_coffee():
        print('Coffee machine made Latte\n')


# concrete strategy
class Cappuccino(CoffeeMachine):
    @staticmethod
    def make_coffee():
        print('Coffee machine made Cappuccino\n')


def client_code():
    americano = Americano()
    latte = Latte()
    cappuccino = Cappuccino()

    coffee = Coffee(americano)
    coffee.lets_drink_coffee()

    coffee.coffee_type = latte
    coffee.lets_drink_coffee()

    coffee.coffee_type = cappuccino
    coffee.lets_drink_coffee()


def main():
    client_code()


if __name__ == '__main__':
    main()