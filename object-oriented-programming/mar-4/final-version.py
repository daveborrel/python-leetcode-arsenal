from enum import Enum
    
class ProductType(Enum):
    MEAT = 1
    DAIRY = 2
    FRUIT = 3
    VEGETABLE = 4
    NONPERISHABLE = 5
    
class FridgeException(Exception):
    pass

class ItemNotInFridgeException(FridgeException):
    pass

class ItemNotInFridgeException(FridgeException):
    pass
    
class SmartFridge:

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartFridge, cls).__new__(cls)
            cls.products = {}
        return cls._instance
            
            
    def add_product(self, product):
        if product.name not in self.products:
            self.products[product.name] = [product]
        else:
            self.products[product.name].append(product)
            
    def remove_product(self, product):       
        try:
            if product.name not in self.products or len(self.products[product.name]) == 0:
                raise ItemNotInFridgeException(f"{product.name} is not found in the fridge.")
            self.products[product.name].remove(product)
            return True
        except ItemNotInFridgeException as e:
            print("Error Found: ", e)
            return False
    
    def simulate_day(self):
        for pname, products in self.products.items():
            for p in products:
                p.simulate_day()
                
        print("A day has passed!")
        
        for pname, products in self.products.items():
            for p in products:
                if p.quality < 1:
                    print(f"You need to buy more {p.name}")
                if p.quality <= 2:
                    print(f"Your {p.name} is close to spoiling")    
            
class Product:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.quality = 10
        
    def simulate_day(self):
        self.quality -= 1

class Meat(Product):
    def simulate_day(self):
        self.quality -= 3
        
class Dairy(Product):
    def simulate_day(self):
        self.quality -= 3
        
class Fruit(Product):
    def simulate_day(self):
        self.quality -= 2
        
class Vegetable(Product):
    def simulate_day(self):
        self.quality -= 2
        
class NonPerishable(Product):
    def simulate_day(self):
        return
    
class Main:
    def run(self):
        sf = SmartFridge()
        
        chicken = Meat("Chicken", ProductType.MEAT)
        
        sf.add_product(chicken)
        sf.simulate_day()
        if not sf.remove_product(chicken):
            print(f"Could not remove {chicken.name}")
        sf.simulate_day()
        if not sf.remove_product(chicken):
            print(f"Could not remove {chicken.name}")
            
        chicken2 = Meat("Chicken", ProductType.MEAT)
        water_bottle = NonPerishable("Dasani", ProductType.NONPERISHABLE)
        water_bottle = NonPerishable("Dasani", ProductType.NONPERISHABLE)
        apple = Fruit("Apple", ProductType.FRUIT)
        
        sf.add_product(chicken2)
        sf.add_product(water_bottle)
        sf.add_product(water_bottle)
        sf.add_product(apple)
        
        sf.simulate_day()
        sf.simulate_day()
        sf.simulate_day()

main = Main()
main.run()