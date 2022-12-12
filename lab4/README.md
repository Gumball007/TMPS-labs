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

__Adapter__ is a structural design pattern that allows objects with incompatible interfaces to collaborate.

```python
class IranSocket: # client
    _type = '2'


class Adapter: # adapter
    _socket = None
    _pinType = '3to2'

    def __init__(self, socket):
        self._socket = socket


class Fridge: # adaptee
    _adapter = None
    _pinType = '3'

    def __init__(self, adapter):
        self._adapter = adapter

    def fnFreeze(self):
        if self._adapter._pinType == self._pinType + 'to' + self._adapter._socket._type:
            print('Done...')
        else:
            print('Sorry, it is not possible...')

```

__Decorator__ is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

```python
class History:
    def all_history(self):
        print('print all articles')


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def check_staff_password(self):
        if self.username == 'admin' and self.password == 'password':
            return True

def outer(Func):
    def inner():
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        log = Login(username,password)
        res = log.check_staff_password()
        if res:
            Func()
        else:
            print('Sorry, you don\'t have access')
    return inner

@outer
def show_all_history():
    articles = History()
    articles.all_history()

show_all_history()
```

__Facade__ is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

```python
class Raw:
    def raw(self):
        print('buy raw food ...')

class Transfer:
    def teransfer(self):
        print('transfer food to restutant')

class Cook:
    def cook(self):
        print('cook food by cheif')

class ItalianResturant:
    def get(self):
        r = Raw()
        r.raw()

        t = Transfer()
        t.teransfer()

        c = Cook()
        c.cook()

def order():
    i = ItalianResturant()
    i.get()

order()
```

__Proxy__ is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

```python
class DB:
    def work(self):
        print('You are admin so you can work with DB')


class proxy:
    _password = 'Secret'

    def check_user_password(self, password):
        if self._password == password:
            db = DB()
            db.work()
        else:
            print('Sorry you dont have permison to access db')

p = proxy()
p.check_user_password('Secret')
p.check_user_password('Wrong_password')
```

</br>

## Conclusions

At this laboratoty work I found out Structural Design Patterns. I became familiar with all the definitions, with all of the aspects and how to implement them.
