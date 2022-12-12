from abc import ABC, abstractmethod


# abstract morning class contains template_method
class AbstractMorning(ABC):
    def morning_template_method(self):
        self._wake_up()
        self._take_shower()
        self._additional_method1()
        self._eat_breakfast()
        self._additional_method2()
        self._wear_clothes()
        self._go_somewhere()

    @staticmethod
    @abstractmethod
    def _wake_up():
        pass

    @staticmethod
    def _take_shower():
        print('Take shower')

    @staticmethod
    def _additional_method1():
        pass

    @staticmethod
    def _eat_breakfast():
        print('Eat breakfast')

    @staticmethod
    def _additional_method2():
        pass

    @staticmethod
    @abstractmethod
    def _wear_clothes():
        pass

    @staticmethod
    @abstractmethod
    def _go_somewhere():
        pass


# concrete morning class
class WeekDayMorning(AbstractMorning):
    @staticmethod
    def _wake_up():
        print('Wake up at 6:00')

    @staticmethod
    def _wear_clothes():
        print('Wear work clothes')

    @staticmethod
    def _go_somewhere():
        print('Go to work')


# concrete morning class
class WeekendMorning(AbstractMorning):
    @staticmethod
    def _wake_up():
        print('Wake up at 9:00')

    @staticmethod
    def _additional_method1():
        print('Read newspaper')

    @staticmethod
    def _additional_method2():
        print('Watch movie')

    @staticmethod
    def _wear_clothes():
        print('Wear weekend clothes')

    @staticmethod
    def _go_somewhere():
        print('Go out with friends')


def client_code(morning_type: AbstractMorning):
    morning_type.morning_template_method()


def main():
    print('Weekday morning\n')
    weekday_morning = WeekDayMorning()
    client_code(weekday_morning)

    print('\nWeekend morning\n')
    weekend_morning = WeekendMorning()
    client_code(weekend_morning)


if __name__ == '__main__':
    main()