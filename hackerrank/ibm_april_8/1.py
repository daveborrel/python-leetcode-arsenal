# given s = "a?rt???"
# turn this into the smallest palindrome possibe

class Solution:
    
    def getSmallestPalindrome(self, s):
        
        s_list = list(s)
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s_list[l] == s_list[r]:
                if s_list[l] == "?" and s_list[r] == "?":
                    s_list[l] = "a"
                    s_list[r] = "a"
                else:
                    continue
            else:
                if s_list[l] == "?":
                    s_list[l] = s_list[r]
                elif s[r] == "?":
                    s_list[r] = s_list[l]
                else:
                    return str(-1)
            l += 1
            r -= 1
        
        return "".join(s_list)
        
# Solution
sol = Solution()
s = "a?rt???"
res = sol.getSmallestPalindrome(s)
print(res)

s = "bzrt??h"
res = sol.getSmallestPalindrome(s)
print(res)