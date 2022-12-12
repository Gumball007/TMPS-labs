from abc import ABC, abstractmethod


# visitor interface
class Delivery(ABC):
    @abstractmethod
    def deliver_ukrainian_cuisine(self, restaurant):
        pass

    @abstractmethod
    def deliver_italian_cuisine(self, restaurant):
        pass


# component interface
class Restaurant(ABC):
    @staticmethod
    @abstractmethod
    def cook():
        pass

    @abstractmethod
    def deliver(self, delivery: Delivery):
        pass


# concrete component
class UkrainianCuisine(Restaurant):
    @staticmethod
    def cook():
        print('Ukrainian dish is cooked')
        return 'borsch'

    def deliver(self, delivery):
        delivery.deliver_ukrainian_cuisine(self)


# concrete component
class ItalianCuisine(Restaurant):
    @staticmethod
    def cook():
        print('Italian dish is cooked')
        return 'pizza'

    def deliver(self, delivery):
        delivery.deliver_italian_cuisine(self)


# concrete visitor
class ExpressDelivery(Delivery):
    def deliver_ukrainian_cuisine(self, restaurant: UkrainianCuisine):
        dish_name = restaurant.cook()
        print(f'Express delivery {dish_name} from ukrainian cuisine restaurant')

    def deliver_italian_cuisine(self, restaurant: ItalianCuisine):
        dish_name = restaurant.cook()
        print(f'Express delivery {dish_name} from italian cuisine restaurant')


# concrete visitor
class RegularDelivery(Delivery):
    def deliver_ukrainian_cuisine(self, restaurant: UkrainianCuisine):
        dish_name = restaurant.cook()
        print(f'Regular delivery {dish_name} from ukrainian cuisine restaurant')

    def deliver_italian_cuisine(self, restaurant: ItalianCuisine):
        dish_name = restaurant.cook()
        print(f'Regular delivery {dish_name} from italian cuisine restaurant')


def client_code():
    ukrainian_restaurant = UkrainianCuisine()
    italian_restaurant = ItalianCuisine()

    express_delivery = ExpressDelivery()
    regular_delivery = RegularDelivery()

    ukrainian_restaurant.deliver(express_delivery)
    print('')
    italian_restaurant.deliver(regular_delivery)


def main():
    client_code()


if __name__ == '__main__':
    main()