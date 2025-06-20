import math

n = 12

square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

# i ** 2 --> this will square the number you're at
# math.sqrt(n) means that we take the square root of n and then add 1



print(square_nums)