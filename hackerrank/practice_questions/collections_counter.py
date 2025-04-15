# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

def calculateEarnings(length):
    string_values = input()
    values = [int(num) for num in string_values.split()]
    count = Counter(values)
    
    number_of_customers = int(input())
    profit = 0
    
    for i in range(number_of_customers):
        input_string = input()
        numbers = [int(num) for num in input_string.split()]
        
        if numbers[0] in count and count[numbers[0]] != 0:
            profit += numbers[1]
            count[numbers[0]] -= 1
    
    print(profit)

text = input()
calculateEarnings(text)