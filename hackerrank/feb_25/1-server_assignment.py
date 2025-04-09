class Solution:
    def returnRequestId(self, num_servers, requests):
        servers = [0] * num_servers
        
        for i in range(len(requests)):
            
            range_of_requests = requests[i]
            
            minimum_value = float('inf')
            minimum_index = 0
                      
            for j in range(range_of_requests + 1):
                
                val = servers[j]
                
                if val < minimum_value:
                    minimum_value = val
                    minimum_index = j
            
            servers[minimum_index] += 1
            requests[i] = minimum_index
            
        return requests
    
s = Solution()

num_servers = 5
requests = [3,2,3,2,4]

num_servers_2 = 5
requests_2 = [0,1,2,3]


res = s.returnRequestId(num_servers,requests)
res2 = s.returnRequestId(num_servers_2,requests_2)

print("TEST CASE 1")
print(res)

print("TEST CASE 2")
print(res2)