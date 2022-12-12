from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from random import choice, randint


class Earth:
    def __init__(self):
        self.__name = 'earth'
        self.__cell_quantity = 1

    @property
    def cell_quantity(self):
        return self.__cell_quantity

    @property
    def name(self):
        return self.__name


class Lava:
    def __init__(self):
        self.__name = 'lava'
        self.__cell_quantity = 3

    @property
    def cell_quantity(self):
        return self.__cell_quantity

    @property
    def name(self):
        return self.__name


class Factory(ABC):
    @staticmethod
    @abstractmethod
    def create_element():
        pass


class EarthFactory(Factory):
    @staticmethod
    def create_element():
        return Earth()


class LavaFactory(Factory):
    @staticmethod
    def create_element():
        return Lava()


class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self.__collection = collection
        self.__index = 0

    def __next__(self):
        try:
            for _ in self.__collection:
                element = self.__collection[self.__index]
                if isinstance(element, Earth):
                    print(f'{element.name}')
                    self.__index += 1
                elif isinstance(element, Lava):
                    self.__index += element.cell_quantity
        except IndexError:
            StopIteration()


class ConcreteIterable(Iterable):
    def __init__(self, earth_factory: Factory, lava_factory: Factory):
        self._earth_factory = earth_factory
        self._lava_factory = lava_factory
        self.__collection = self.__create_iterable()

    def __create_iterable(self):
        collection = []
        earth_element = self._earth_factory.create_element()
        lava_element = self._lava_factory.create_element()
        possible_element = (earth_element, lava_element)

        for _ in range(randint(10, 15)):
            element = choice(possible_element)
            if isinstance(element, Earth):
                for _ in range(element.cell_quantity):
                    collection.append(element)
            else:
                for _ in range(element.cell_quantity):
                    collection.append(element)

        return collection

    @property
    def collection(self):
        return self.__collection

    def __iter__(self):
        return ConcreteIterator(self.__collection)

    def iterate(self):
        self.__iter__().__next__()


def main():
    earth_factory = EarthFactory()
    lava_factory = LavaFactory()

    collection = ConcreteIterable(earth_factory, lava_factory)

    for element in collection.collection:
        print(f'{element.name}', end=' ')

    print('')

    collection.iterate()


if __name__ == '__main__':
    main()