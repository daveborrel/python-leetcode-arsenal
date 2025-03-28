# Just a random python file for any testing you might have
# Think of this as replit

# def minimum_window_substring(s, t):
    
#     start, end = 0, 0
    
#     while start < len(s):
        
s = "ABAACBAB" 
t = "ABC"

count_map = {}

for char in t:
    count_map[char] = count_map.get(char, 0) + 1
    
print(count_map)

print(sum(list(count_map.values())))