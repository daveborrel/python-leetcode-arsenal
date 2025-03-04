# This is a useful pattern to allow observers to watch a subject


class Subject:
    
    def __init__(self):
        self.observers = []
        
    def notify_observers(self):
        for observer in self.observers:
            observer.update()
            
    def add_observer(self, observer):
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)

class Observer:
    
    def update(self, subject):
        print("Observe Object")