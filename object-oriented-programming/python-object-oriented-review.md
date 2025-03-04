# Classes and Objects Review

## Difference between __new__ and __init__

`__init__`
- an instance method
- initializing a newly created instance (object) of a class
- takes object as the argument

`__new__` 
- is a static method
- responsible for creating and returning a new instance of the class.


- In this example, we can see that new is called before init.

```python
class Person:
    def __new__(cls, name, age):
        print("Creating a new Person object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        print("Initializing the Person object")
        self.name = name
        self.age = age

person = Person("John Doe", 30)
print(f"Person's name: {person.name}, age: {person.age}")

# Creating a new Person object
# Initializing the Person object
# Person's name: John Doe, age: 30
```

So if we wanted to create the singleton approach:
```python
class Singleton:

    _instance = None

    def __new__(cls):
        if cls.instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.stored_food = []
        return cls._instance
```

## Types
In python classes there are no explicit types in the fields just based off the way python is structured.

```python
class Vehicle:
    #these annotations won't enforce the types during runtime.
    owner: str
    type: VehicleType
    
    def __init__(self, type: VehicleType, owner: str):
        if not isinstance(type, VehicleType):
            raise TypeError("Vehicle type must be a VehicleType enum")
        self.owner = owner
        self.type = type
```

In order to use types, you have to use a library like [pydantic](https://docs.pydantic.dev/latest/concepts/types/) or validate it at runtime.

```python
def __init__(self, type: VehicleType, owner: str):
    if not isinstance(type, VehicleType):
        raise TypeError("Vehicle type must be a VehicleType enum")
    if not isinstance(owner, str):
        raise TypeError("Owner must be a string")
    self.owner = owner
    self.type = type
```

[Python Documentation on Types](https://docs.python.org/3/library/typing.html#generics)

##  Design Patterns

Naive Singleton
```python
class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            # how would this line ever get reached?
            raise Exception("This class is a Singleton")
        else:
            ParkingLot._instance = self
            self.levels: List[level] = []
    
    @staticmethod
    # A static method belongs to a class itself. You can call it without creating an instance of that class.
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
```

## Class Relationships

### One to One Relationship

### One to Many

### Many to One

## Error Handling

## Main Function
[Why we need this if statement guard](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

### Try and Except Blocks
[Best Practices](https://python.land/deep-dives/python-try-except)