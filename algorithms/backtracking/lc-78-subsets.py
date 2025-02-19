# Here's what the decision tree would look like for [1, 2, 3]:

# Start with an empty subset [].
# Choose whether to include 1 or not, resulting in subsets [] and [1].
# For each of these subsets, choose whether to include 2, leading to [], [1], [2], and [1, 2].
# Finally, for each of these, choose whether to include 3, ending with [], [1], [2], [1, 2], [3], [1, 3], [2, 3], and [1, 2, 3].

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        def depth_first_search(index: int):
            if index == len(nums):
                all_subsets.append(current_subset[:])
                return
          
            current_subset.append(nums[index])
            depth_first_search(index + 1)
          
            current_subset.pop()
            depth_first_search(index + 1)

        all_subsets = []
        current_subset = []
        depth_first_search(0)
        return all_subsets