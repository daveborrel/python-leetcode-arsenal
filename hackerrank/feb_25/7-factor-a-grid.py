import heapq

#
#
#

class Solution:
    def returnMaxValue(self, data, factor, x):
        
        data_with_heaped_rows = self.converIntoMaxHeap(data)
        
        res_heap = []
        heapq.heapify(res_heap)
        count = 0
        
        # go through each row
        for i in range(len(data_with_heaped_rows)):
            
            row = data_with_heaped_rows[i]
            
            while factor[i] > 0:
                val = heapq.heappop(row)
                heapq.heappush(res_heap, val)
                factor[i] -= 1
        
        while x > 0:
            if not res_heap:
                return -1
            else:
                count += (-1 * heapq.heappop(res_heap))
            x -= 1
        
        return count

    def converIntoMaxHeap(self, data):
        
        res = []
        rows = len(data)
        cols = len(data[0])
        
        for i in range(rows):
            x = []
            heapq.heapify(x)
            
            for j in range(cols):
                heapq.heappush(x, (-1 * data[i][j]))
                
            res.append(x)
        return res
    
s = Solution()

n = 3  
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
factor = [1, 2, 1]  
x = 2  

res = s.returnMaxValue(data, factor, x)

print(res)