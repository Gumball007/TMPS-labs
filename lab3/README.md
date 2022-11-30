# Structural Design Patterns

## Course: Techniques and Mechanisms for Software Design

### FAF - 203

### Author: Ana Corolețchi

----

## Objectives

&ensp; &ensp; __1. Study and understand the Structural Design Patterns.__

&ensp; &ensp; __2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.__

&ensp; &ensp; __3. Implement some additional functionalities using structural design patterns.__

## Theory

&ensp; &ensp; In software engineering, the Structural Design Patterns are concerned with how classes and objects are composed to form larger structures. Structural class patterns use inheritance to create a hierarchy of classes/abstractions, but the structural object patterns use composition which is generally a more flexible alternative to inheritance.

&ensp; &ensp; Some examples of from this category of design patterns are:

* Adapter
* Bridge
* Composite
* Decorator
* Facade
* Flyweight
* Proxy

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

```

__Facade__ is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

```python

```

__Proxy__ is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

```python

```

</br>

## Conclusions

At this laboratoty work I found out asymmetric ciphers and choose to implement RSA Cipher. This cipher requires knowlege of prime and coprime numbers, Euler's totient function, GCD and modular multiplicative inverse.