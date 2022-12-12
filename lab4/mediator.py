from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender_component: object, event: str):
        pass


class BaseComponent:
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


class Footballer(BaseComponent):
    def score_goal(self):
        event = 'Goal is scored!'
        print(event)
        self._mediator.notify(self, event)


class Fan(BaseComponent):
    def celebrate_goal(self):
        event = 'Fans are celebrating'
        print(event)
        self._mediator.notify(self, event)


class ScoreBoard(BaseComponent):
    def change_score(self):
        event = 'Score is changed'
        print(event)
        self._mediator.notify(self, event)


class Announcer(BaseComponent):
    def announce_score(self):
        event = 'Score is announced'
        print(event)
        self._mediator.notify(self, event)


class ConcreteMediator(Mediator):
    def __init__(self, footballer_component, fan_component, score_board_component, announcer_component):
        self._footballer = footballer_component
        self._footballer.mediator = self
        self._fan = fan_component
        self._fan.mediator = self
        self._score_board = score_board_component
        self._score_board.mediator = self
        self._announcer = announcer_component
        self._announcer.mediator = self

    def notify(self, sender_component, event):
        if event == 'Goal is scored!':
            self._fan.celebrate_goal()
            self._score_board.change_score()
        elif event == 'Score is changed':
            self._announcer.announce_score()


def client_code():
    footballer = Footballer()
    fan = Fan()
    score_board = ScoreBoard()
    announcer = Announcer()

    mediator = ConcreteMediator(footballer, fan, score_board, announcer)

    footballer.score_goal()


def main():
    client_code()


if __name__ == '__main__':
    main()