# Requirements
# - Let you know how much of each item in your fridge you actually have in real time.
# - See the expiration dates of each item
# - Should be able to connect to a Smart Phone App

# Constraints
# - The total space in the fridge

# Basic Design
# - SmartRefrigerator
# - Food

import datetime
from enum import Enum

class FoodNotFoundError(Exception):
    pass

class FoodType(Enum):
    MEAT = 1
    DAIRY = 2
    FRUIT = 3
    VEGETABLE = 4
    NON_PERISHABLE = 5

# There should only be one refridgerator - So I would want to use a singleton pattern.
class SmartRefridgerator:
    _instance = None
    
    def __init__(self):
        if self._instance is not None:
            raise Exception("This class is a Singleton")
        else:
            SmartRefridgerator._instance = self
            self.stored_food = []
    
    @staticmethod
    # This static method should not have itself as a parameter.
    def get_instance():
        if SmartRefridgerator._instance is None:
            SmartRefridgerator()
        return SmartRefridgerator._instance
    
    def store_food(self, food):
        self.stored_food.append(food)
        
    def remove_food(self, food):
        try:
            if food not in self.stored_food:
                raise FoodNotFoundError(f"{food.name} is not found in your fridge")
            self.stored_food.remove(food)
        except FoodNotFoundError as e:
            print(e)
        
    def get_count_of_food(self):
        count = len(self.stored_food)
        print(f"You have a total of {count} foods in your fridge")
        return count
    
    def get_count_of_food_based_on_type(self, type):
        count = 0
        
        for food in self.stored_food:
            if food.type == type:
                count += 1
                
        print(f"You have {count} {type.name} items in your fridge")
        return count
    
    def simulate_day_passing(self):
        for food in self.stored_food:
            food.simulate_day()
        
        print(f"One day has passed.")
            
        for food in self.stored_food:
            if food.quality < 1:
                print(f"You need to buy more {food.name}")
            if food.quality <= 2:
                print(f"Your {food.name} is close to expiring")
                
        # Too many for loops
        # Are there any design patterns I could potentially lean on here?
        
            
class Food:
    
    def __init__(self, name, type, expiry_date):
        self.name = name
        self.type = type
        self.quality = 10
        self.expiry_date = expiry_date
    
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


        
class Main:
    
    def run(self):
        smart_refridgerator = SmartRefridgerator.get_instance()
        
        steak = Meat("Steak", FoodType.MEAT, datetime.datetime(2025,3,5))
        milk = Dairy("Milk", FoodType.DAIRY, datetime.datetime(2025,2,28))
        apple = Fruit("Apple", FoodType.FRUIT, datetime.datetime(2025,3,3))
        carrot = Vegetable("Carrot", FoodType.VEGETABLE, datetime.datetime(2025,3,3))
        water_bottle = NonPerishable("Dasani", FoodType.NON_PERISHABLE, datetime.datetime(2025,3,3))
        
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