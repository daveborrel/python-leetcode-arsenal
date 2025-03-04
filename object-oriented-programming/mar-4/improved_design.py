# Improvements Based on Prior Examples
# [x] Updated the singleton implementation to use the __new__ keyword
# [x] Observer pattern. SmartFridge would be the subject and MobileAppNotifier would be the observer.
# [x] Go through pros and cons of storage
# [x] Explain why an enum is advantageous
# [] Fix error handling approach

import logging
from enum import Enum

class FoodNotFoundError(Exception):
    pass
class NoMoreFoodError(Exception):
    pass

# Enums are useful here because it prevents any typos. Good for self documentation of code.
class FoodType(Enum):
    MEAT = 1
    DAIRY = 2
    FRUIT = 3
    VEGETABLE = 4
    NON_PERISHABLE = 5

# There should only be one refridgerator - So I would want to use a singleton pattern.
# list - is useful if you want to manipulate data at a certain index.
# lookup time complexity - O(N) as you're looking through the entire list
# easier to simulate the days
# dictionary - useful for looking up key value pairs.
# harder to simulate days
class SmartRefrigerator:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartRefrigerator, cls).__new__(cls)
            # initialize the stored food
            cls._instance.stored_food = {}
            cls._instance.observers = []
        return cls._instance
    
    def store_food(self, food):
        if food.name in self.stored_food:
            self.stored_food[food.name].append(food)
        else:
            self.stored_food[food.name] = [food]
        
    # should modify this because these errors are not critical enough
    def remove_food(self, food):
        try:
            if food.name not in self.stored_food:
                raise FoodNotFoundError(f"{food.name} is not found in your fridge")
            if len(self.stored_food[food.name]) == 0:
                raise NoMoreFoodError(f"There is no more {food.name} in the fridge")
            self.stored_food[food.name].remove(food)
        except FoodNotFoundError as e:
            logging.error(f"Food removal failed: {e}")
        except NoMoreFoodError as e:
            logging.error(f"Food removal failed: {e}")
    
    def add_observer(self, observer):
        self.observers.append(observer)
        
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
        
    def get_count_of_food(self):
        count = len(self.stored_food)
        print(f"You have a total of {count} foods in your fridge")
        return count
    
    def get_count_of_food_based_on_type(self, type):
        count = 0
        
        for key, val in self.stored_food.items():
            if val[0].type == type:
                count += len(val)
                
        print(f"You have {count} {type.name} items in your fridge")
        return count
    
    def simulate_day_passing(self):
        for key, val in self.stored_food.items():
            for v in val:
                v.simulate_day()
        
        print(f"One day has passed.")
        
        self.notify_observers()
        
            
class Food:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.quality = 10
    
    def simulate_day(self):
        self.quality -= 1

class Meat(Food):
    
    def simulate_day(self):
        self.quality -= 3
        
class Dairy(Food):
    
    def simulate_day(self):
        self.quality -= 3

class Fruit(Food):
    
    def simulate_day(self):
        self.quality -= 2
        
class Vegetable(Food):
    
    def simulate_day(self):
        self.quality -= 2
        
class NonPerishable(Food):
    
    def simulate_day(self):
        return
    
class SmartFridgeMobileApp:
    def update(self, refrigerator):
        for key, val in refrigerator.stored_food.items():
            for v in val:
                if v.quality < 1:
                    print(f"You need to buy more {v.name}")
                if v.quality <= 2:
                    print(f"Your {v.name} is close to expiring")

        
class Main:
    
    def run(self):
        smart_refridgerator = SmartRefrigerator()
        mobile_app = SmartFridgeMobileApp()
        
        smart_refridgerator.add_observer(mobile_app)
        
        steak = Meat("Steak", FoodType.MEAT)
        milk = Dairy("Milk", FoodType.DAIRY)
        apple = Fruit("Apple", FoodType.FRUIT)
        carrot = Vegetable("Carrot", FoodType.VEGETABLE)
        water_bottle = NonPerishable("Dasani", FoodType.NON_PERISHABLE)
        
        smart_refridgerator.store_food(steak)
        smart_refridgerator.store_food(milk)
        smart_refridgerator.store_food(apple)
        smart_refridgerator.store_food(carrot)
        smart_refridgerator.store_food(water_bottle)
        
        smart_refridgerator.get_count_of_food()
        smart_refridgerator.get_count_of_food_based_on_type(FoodType.MEAT)  
        
        smart_refridgerator.simulate_day_passing()
        smart_refridgerator.simulate_day_passing() 
        smart_refridgerator.simulate_day_passing() 
        
        smart_refridgerator.remove_food(steak)
        smart_refridgerator.remove_food(milk)
        
        smart_refridgerator.simulate_day_passing()
        
        smart_refridgerator.remove_food(steak)

main = Main()
main.run()