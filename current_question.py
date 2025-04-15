#open the file
text_file = open('sample_http_requests.txt','r')

#get the list of line
line_list = text_file.readlines()

seen = {}

for line in line_list:
    
    #split will seperate each request by the space
    endpoint_used = line.split()[1]
    
    if endpoint_used not in seen:
        seen[endpoint_used] = seen.get(endpoint_used, 0) + 1
    else:
        seen[endpoint_used] += 1
        
print(seen)