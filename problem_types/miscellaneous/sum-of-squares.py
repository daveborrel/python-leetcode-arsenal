import sys
import io

# 2 - there will be 2 test cases
# 4 - ???
# 3 -1 1 14 - this is the number of 

def sum_of_squares(text):
    
    for i in range(text):
        first = int(input())
        array = input().split(" ")
        new_array = map(lambda x : int(x) * int(x) if int(x) >= 0 else 0, array)
        print(sum(list(new_array)))


# Simulated input
input_data = """2
4
3 -1 1 14
5
9 6 -53 32 16
"""

# Mock stdin
sys.stdin = io.StringIO(input_data)

test_case = int(input())

sum_of_squares(test_case)
