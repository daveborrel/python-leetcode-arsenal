#!/bin/python3

import math
import os
import random
import re
import sys

def most_common_characters(s):
    s_list = list(s)
    seen = {}
    
    for i in range(len(s_list)):
        if s_list[i] not in seen:
            seen[s_list[i]] = seen.get(s_list[i], 0) + 1
        else:
            seen[s_list[i]] += 1
    
    sorted_items = sorted(seen.items(), key=lambda x: (-x[1], x[0]))
    
    for i in range(3):
        print(sorted_items[i][0] + " " + str(sorted_items[i][1]))    

if __name__ == '__main__':
    s = input()
    
    most_common_characters(s)
