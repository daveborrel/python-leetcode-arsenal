# We can implement a queue with 2 stacks the following way.

class StackQueue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, val):
        self.s1.append(val)
        
    def pop(self):
        
        while self.s1:
            item = self.s1.pop()
            self.s2.append(item)
        
        res = self.s2.pop()
        
        while self.s2:
            item = self.s2.pop()
            self.s1.append(item)
            
        return res

sq = StackQueue()

sq.push(3)
sq.push(4)
sq.push(5)
print(sq.pop())