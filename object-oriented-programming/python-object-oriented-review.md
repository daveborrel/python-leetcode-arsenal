# Classes and Objects Review

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



### Try and Except Blocks
[Best Practices](https://python.land/deep-dives/python-try-except)