#greedy change

def greedy_change(n):
    change = []  # Initialize an empty list to store the coins
    
    while n > 0:
        if n >= 25:
            change.append("quarter")
            n -= 25
        elif n >= 10:
            change.append("dime")
            n -= 10
        elif n >= 5:
            change.append("nickel")
            n -= 5
        else:
            change.append("penny")
            n -= 1
    
    return change

# Example usage:
n = 47
result = greedy_change(n)
print(result)  # Output: ['quarter', 'quarter', 'dime', 'penny', 'penny', 'penny', 'penny']