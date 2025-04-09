# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_words(text):
    
    words = []
    seen = {}
    
    for i in range(int(text)):
        words.append(input())
        
    for word in words:
        if word not in seen:
            seen[word] = seen.get(word, 0) + 1
        else:
            seen[word] += 1
    
    print(len(seen))
    
    second_line = ""
    
    for val in seen.values():
        second_line = second_line + " " + str(val)
        
    print(second_line[1:])
        

# Gets STDIN value
text = input()

# STDOUT is just printing
word_count = count_words(text)