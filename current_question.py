# Just a random python file for any testing you might have
# Think of this as replit

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        n = 3
        res = []
        self.current_combination = ""

        def dfs(left_count, right_count):
            if (left_count + right_count) == 2*n:
                res.append(self.current_combination)
                return
            
            if left_count < n:
                self.current_combination = self.current_combination + "("
                dfs(left_count + 1, right_count)
                self.current_combination = self.current_combination[:-1]
            
            if left_count > right_count:
                self.current_combination = self.current_combination + ")"
                dfs(left_count, right_count + 1)
                self.current_combination = self.current_combination[:-1]
        
        dfs(0, 0)
        return res
    
    
s = Solution()
print(s.generateParenthesis(3))