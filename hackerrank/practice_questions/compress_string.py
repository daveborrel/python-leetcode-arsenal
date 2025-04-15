# https://www.hackerrank.com/challenges/compress-the-string/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

def print_occurences(string):
    
    res = ""
    occurences = []
    current_string = []
    
    for i in range(len(string)):
        if len(current_string) == 0:
            current_string.append(string[i])
            current_string.append(1)
        else:
            if string[i] == current_string[0]:
                current_string[1] += 1
            else:
                occurences.append((current_string[0], current_string[1]))
                current_string[0] = string[i]
                current_string[1] = 1
    
    if current_string:
        occurences.append((current_string[0], current_string[1]))

    for o in occurences:
        res = res + f'({o[1]}, {o[0]}) '
        
    if res[-1] == " ":
        res = res[:-1]
        
    print(res)
    
    
text_input = input()
print_occurences(text_input)