from abc import ABC, abstractmethod


# concrete commands interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# concrete commands
class PreparationCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.set_camera()


class ShootingCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.start_shooting()


# command sender
class DirectorSender:
    def __init__(self, command: Command):
        self._command = command

    def execute_command(self):
        return self._command.execute()


# command receivers
class OperatorReceiver:
    @staticmethod
    def set_camera():
        return 'Operator is setting camera'

    @staticmethod
    def start_shooting():
        return 'Operator is shooting'


class ActorReceiver:
    @staticmethod
    def start_shooting():
        return 'Actor is acting'


def client_code_prepare():
    operator_receiver = OperatorReceiver()

    command = PreparationCommand(operator_receiver)

    director = DirectorSender(command)

    preparation = director.execute_command()
    print('Preparing for shooting:')
    print(preparation)


def client_code_start_shooting():
    operator_receiver = OperatorReceiver()
    actor_receiver = ActorReceiver()

    command_for_operator = ShootingCommand(operator_receiver)
    command_for_actor = ShootingCommand(actor_receiver)

    director1 = DirectorSender(command_for_operator)
    director2 = DirectorSender(command_for_actor)

    shooting1 = director1.execute_command()
    shooting2 = director2.execute_command()

    print('Shooting:')
    print(shooting1)
    print(shooting2)


def main():
    client_code_prepare()
    print('')
    client_code_start_shooting()


if __name__ == '__main__':
    main()