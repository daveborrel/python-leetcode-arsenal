# lexicographical comparison
# 
# When comparing apple and apricot
# - "a" is the same in both cases
# - "p" ^
# - "l" in apple. and "r" in apricot. Since l comes "before" r, then apple is considered smaller.

class Solution:
    def returnSecuredString(self, s, t):
        self.count = 0
             
        def dfs(curr):
            if curr >= len(s):
                copy = current_string[:]
                if self.isLexicographicallyGreater(copy, t):
                    self.count += 1
                return
            
            current_string.append(s[curr])
            dfs(curr + 1)
            
            current_string.pop()
            dfs(curr + 1)
        
        current_string = []
        dfs(0)
        return self.count % (10^9 + 7)
    
    def isLexicographicallyGreater(self, s1, s2):
        length = min(len(s1), len(s2))
        
        for i in range(length):
            if s1[i] > s2[i]:
                return True
        return len(s1) > len(s2)

s = "bab"
t = "ab"

sol = Solution()

res = sol.returnSecuredString(s, t)
res_2 = sol.returnSecuredString("aba", "ab")

print("TEST 1")
print(res)

print("TEST 2")
print(res_2)