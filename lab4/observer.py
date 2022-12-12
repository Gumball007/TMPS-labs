from abc import ABC, abstractmethod


# interface for publisher
class Subject(ABC):
    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass


# interface for subscribers
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


# concrete publisher
class EngineTemperature(Subject):
    __subscribers = []
    __engine_temp = None

    @property
    def engine_temp(self):
        return self.__engine_temp

    def subscribe(self, subscriber: Observer):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Observer):
        self.__subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.__subscribers:
            subscriber.update()

    def start_engine(self, driver_subscriber: Observer):
        print('Engine started')
        self.__engine_temp = 0
        print(f'Engine temperature is now {self.__engine_temp} degrees')
        self.subscribe(driver_subscriber)
        print('Driver subscribed to engine temperature info')

    def drive(self, fan_subscriber):
        print('Driving... Temperature is growing')
        self.__engine_temp = 80
        print(f'Engine temperature is now {self.__engine_temp} degrees')
        if self.__engine_temp >= 75:
            self.subscribe(fan_subscriber)
            print('Fan subscribed to engine temperature info')

    def drive_in_traffic(self):
        self.__engine_temp = 105
        print('Fan is working. But engine temperature is still growing')

    def stop_engine(self):
        for subscriber in self.__subscribers:
            self.unsubscribe(subscriber)
        print('Engine stopped. All unsubscribed')


# concrete subscriber
class FanObserver(Observer):
    def __init__(self, subject, temp_to_start=92):
        self._subject = subject
        self.__temp_to_start = temp_to_start

    @staticmethod
    def __start_working():
        print('Fan is working')

    def update(self):
        print('Fan is checking engine temperature...')
        if self._subject.engine_temp >= self.__temp_to_start:
            print(f'Engine temperature is above {self.__temp_to_start} degrees')
            self.__start_working()
        else:
            print('It\'s low')


# concrete subscriber
class DriverObserver(Observer):
    def __init__(self, subject, critical_engine_temp=105):
        self._subject = subject
        self.__critical_engine_temp = critical_engine_temp

    @staticmethod
    def __turn_on_stove():
        print('Engine temperature is very high...')
        print('Driver turned on stove to lower it')

    def update(self):
        print('Driver is checking engine temperature...')
        if self._subject.engine_temp >= self.__critical_engine_temp:
            print(f'Engine temperature is above {self.__critical_engine_temp} degrees')
            self.__turn_on_stove()
        else:
            print('It\'s OK')


def client_code():
    subject = EngineTemperature()
    fan = FanObserver(subject)
    driver = DriverObserver(subject)

    # driver subscribes when engine starts
    subject.start_engine(driver)
    subject.notify()
    print('')

    # fan subscribes when engine gets hot enough
    subject.drive(fan)
    subject.notify()
    print('')

    subject.drive_in_traffic()
    subject.notify()
    print('')

    # engine stopped. All unsubscribed
    subject.stop_engine()


def main():
    client_code()


if __name__ == '__main__':
    main()