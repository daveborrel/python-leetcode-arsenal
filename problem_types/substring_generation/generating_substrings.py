class Solution:
    def generate_substring(self, s):
        res = []
        
        def dfs(i):
            if i >= len(s):
                return
                
            for j in range(i + 1, len(s) + 1):
                # Add the substring from index i to j
                substring = s[i:j]
                res.append(substring)
                
            # Move to the next starting position
            dfs(i + 1)
                    
        dfs(0)
        return res
    
# Basically think of it as this:
# Starting at a --> ab --> abc
# Moving onto b --> bc
# Finally c

sol = Solution()
res = sol.generate_substring(s)
print(res)
