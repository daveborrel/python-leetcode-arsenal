s = "aaabccz"

def find_first_non_repeating_char(s):
    
    seen = {}
    
    for i in range(len(s)):
        if s[i] not in seen:
            seen[s[i]] = seen.get(s[i], 0) + (i) # almost giving it an id
        else:
            seen[s[i]] = float('inf')
    
    return (s[min(seen.values())])
    
    # emphasis on the first non repeating character.
    # so we have to check the entire string and keep track of the solo
    # I think we can use a queue.

res = find_first_non_repeating_char(s)

print(res)