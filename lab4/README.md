# Behavioral Design Patterns

## Course: Techniques and Mechanisms for Software Design

### FAF - 203

### Author: Ana Corolețchi

----

## Objectives

&ensp; &ensp; __1. Study and understand the Behavioral Design Patterns.__

&ensp; &ensp; __2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.__

&ensp; &ensp; __3. Implement some additional functionalities using behavioral design patterns.__

## Theory

&ensp; &ensp; In software engineering, behavioral design patterns have the purpose of identifying common communication patterns between different software entities. By doing so, these patterns increase flexibility in carrying out this communication.

&ensp; &ensp; Some examples from this category of design patterns are :

* Chain of Responsibility
* Command
* Interpreter
* Iterator
* Mediator
* Observer
* Strategy

## Implementation description

So, I implemented all the Behavioral Design Patterns. I know, they aren't related to the same topic, but at least there are all of them and in time.

__Chain of Responsibility__ is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

```python
# interface for handlers
class Handler(ABC):
    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


# abstract class for concrete handlers
class AbstractHandler(Handler, ABC):
    _next_handler = None
    _can_take_to_club = False

    def set_next_handler(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class Friend(AbstractHandler):
    def handle(self, request):
        if self._can_take_to_club:
            return 'Friend took you to the club!'
        else:
            print('Friend can\'t take you to the club. But he can speak to club member with connections')
            return super().handle(request)

```

The output:

```txt
Ask first handler in chain
Friend can't take you to the club. But he can speak to club member with connections
Club member with connections can't take you to the club. He can speak to vice president of the club
Vice president took you to the club!

Ask last handler in chain
President took you to the club!
```

__Command__ is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

```python
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
```

The output:

```txt
Preparing for shooting:
Operator is setting camera

Shooting:
Operator is shooting
Actor is acting
```

__Iterator__ is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

```python
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
```

The output:

```txt
lava lava lava earth lava lava lava lava lava lava earth lava lava lava lava lava lava lava lava lava lava lava lava lava lava lava earth earth lava lava lava earth 
earth
earth
earth
earth
earth
```

__Mediator__ is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

```python
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
```

The output:

```txt
Goal is scored!
Fans are celebrating
Score is changed
Score is announced
```

__Memento__ is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

```python
class Memento:
    def __init__(self, editor, effect):
        self._editor = editor
        self._effect = effect

    def get_state(self):
        return self._effect


class PhotoEditor:
    def __init__(self, effect=None):
        self._effect = effect
        print(f'Current photo effects are {self._effect}')

    def add_effect(self, new_effect):
        print(f'Applied {new_effect} to photo')
        self._effect = new_effect

    def save(self):
        print('New photo effects are saved')
        return Memento(self, self._effect)

    def restore(self, memento):
        self._effect = memento.get_state()
        print(f'Restored previous state. Current photo effects: {self._effect}')
```

The output:

```txt
Uploaded new photo to editor
Current photo effects are None

Applied Black and White effect to photo
New photo effects are saved

Applied Higher lightness, lower contrast effects to photo
New photo effects are saved

Undoing some effects...
Restored previous state. Current photo effects: Black and White effect
```

__Observer__ is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

```python
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
```

The output:

```txt
Engine started
Engine temperature is now 0 degrees
Driver subscribed to engine temperature info
Driver is checking engine temperature...
It's OK

Driving... Temperature is growing
Engine temperature is now 80 degrees
Fan subscribed to engine temperature info
Driver is checking engine temperature...
It's OK
Fan is checking engine temperature...
It's low

Fan is working. But engine temperature is still growing
Driver is checking engine temperature...
Engine temperature is above 105 degrees
Engine temperature is very high...
Driver turned on stove to lower it
Fan is checking engine temperature...
Engine temperature is above 92 degrees
Fan is working

Engine stopped. All unsubscribed
```

__State__ is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

```python
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
```

The output:

```txt
Morning...
Fresh human is working
Fresh human is riding a bike
Fresh human can't sleep
---Wrong state... human can't do something now

Evening...
Tired human can't work
Tired human is relaxing
Tired human is sleeping
[~/TMPS-labs]$          
```

__Strategy__ is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

```python
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
```

The output:

```txt
Coffee machine made Americano

Coffee machine made Latte

Coffee machine made Cappuccino
```

__Template Method__ is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

```python
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
```

The output:

```txt
Weekday morning

Wake up at 6:00
Take shower
Eat breakfast
Wear work clothes
Go to work

Weekend morning

Wake up at 9:00
Take shower
Read newspaper
Eat breakfast
Watch movie
Wear weekend clothes
Go out with friends
```

__Visitor__ is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

```python
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
```

The output:

```txt
Ukrainian dish is cooked
Express delivery borsch from ukrainian cuisine restaurant

Italian dish is cooked
Regular delivery pizza from italian cuisine restaurant
```

</br>

## Conclusions

At this laboratoty work I found out Behavioral Design Patterns. I became familiar with all the definitions, with all of the aspects and how to implement them. All of the patterns illustrates in a good way all the aspects.
