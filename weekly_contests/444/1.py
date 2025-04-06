class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while not self.is_ascending(nums):
            pairs = self.get_pairs(nums)
            start = pairs[0]
            end = pairs[1]
            
            self.replace_with_sum(nums, start, end)
            count += 1
        
        return count
        
    def is_ascending(self, list):
        for i in range(0, len(list) - 1):
            if list[i] <= list[i+1]:  # Changed to non-decreasing (<=)
                pass
            else:
                return False
        return True
    
    def get_pairs(self, li):
        dic = {}

        for i in range(0, len(li) - 1):
            curr_sum = li[i] + li[i+1]
            if curr_sum not in dic:
                dic[curr_sum] = [i, i+1]

        min_value = min(dic)

        return dic[min_value]
    
    def replace_with_sum(self, li, start, end):
        curr_sum = li[start] + li[end]
        li[start] = curr_sum
        li.pop(end)