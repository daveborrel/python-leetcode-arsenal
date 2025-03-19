# Just a random python file for any testing you might have
# Think of this as replit

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
       digit_mapping = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"],
       }

       res = []

       def dfs(i):
        if i == len(digits) - 1:
            combined = ""
            for c in current_combination:
                combined += c
            res.append(combined)

        for i in range(len(digits)):
            for letter in digit_mapping[digits[i]]:
                current_combination.append(letter)
                dfs(i+1)
                current_combination.pop()

        current_combination = []
        dfs(0)
        return res
    
s = Solution()
res = s.letterCombinations("23")
print(res)


