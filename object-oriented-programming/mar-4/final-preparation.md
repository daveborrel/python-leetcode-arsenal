## Steps to Remember
1. Communicate Thought Process
2. Clarify!
    - What happens when the food is spoiled?
    - How do you want me to notify the user print statements?
    - For product quantities, do you want me to keep a count?

```python
# Consider a structure like:
self.products[product.name] = {
    'count': 1,
    'items': [product]
}
```

## Design Patterns

Singleton - Makes sure that there is only one instance of a class.
Observer - Can be used to create a mobile application class that observes the changes to the fridge
Factory - Provides an interface for creating objects in a superclass

## Time Complexity of List vs Map

List - Search O(n); not that natural
Map - Search O(1); more akin to real life

## OOD
Enum - Useful to avoid typos, more readable, 
Inheritance - product class
Encapsulation - Captures internal state
Polymorphism - Different products override simulate_day()

## Expanding the solution

Storage Sections
Expiration Date

## Testing Approaches

Unit Testing
- Products 
    - making sure that they decrease at the correct rate
    - edge cases like 0
    
- Smart Fridge
    - Test each method
    - Test Exception Handling

Integration Testing
- Product Lifecycle
    - Making sure that from when it gets added to when it expires and is removed that it behaves how we expect it to.

System Testing
- Testing a real life scenario