from abc import ABC, abstractmethod


# abstract class for concrete states
class State(ABC):
    def __init__(self):
        self.__human = None

    @property
    def human(self):
        return self.__human

    @human.setter
    def human(self, human):
        self.__human = human

    @staticmethod
    @abstractmethod
    def do_work():
        pass

    @staticmethod
    @abstractmethod
    def go_sleep():
        pass


# human objects change its state
class Human:
    def __init__(self, initial_state):
        self.__state = initial_state
        self.__state.human = self

    def change_state(self, state: State):
        self.__state = state

    def do_work(self):
        self.__state.do_work()

    def go_sleep(self):
        self.__state.go_sleep()

    def relax(self):
        self.__state.relax()

    def ride_bike(self):
        self.__state.ride_bike()


# concrete state
class TiredState(State):
    @staticmethod
    def do_work():
        print('Tired human can\'t work')

    @staticmethod
    def go_sleep():
        print('Tired human is sleeping')

    @staticmethod
    def relax():
        print('Tired human is relaxing')


# concrete state
class FreshState(State):
    @staticmethod
    def do_work():
        print('Fresh human is working')

    @staticmethod
    def go_sleep():
        print('Fresh human can\'t sleep')

    @staticmethod
    def ride_bike():
        print('Fresh human is riding a bike')


def client_code():
    print('Morning...')

    morning_state = FreshState()
    human = Human(morning_state)

    try:
        human.do_work()
        human.ride_bike()
        human.go_sleep()
        human.relax()
    except AttributeError:
        print('---Wrong state... human can\'t do something now')

    print('\nEvening...')

    evening_state = TiredState()
    evening_state.human = human
    evening_state.human.change_state(evening_state)
    # human.change_state(evening_state)

    human.do_work()
    human.relax()
    human.go_sleep()


def main():
    client_code()


if __name__ == '__main__':
    main()