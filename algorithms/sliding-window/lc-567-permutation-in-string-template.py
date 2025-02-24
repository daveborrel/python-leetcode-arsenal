class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Initialize window variables
        start = 0
        end = 0
        
        # Initialize window state
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Fill pattern frequency map
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        # 2. Extend the window with window_end
        while end < len(s2):
            # 3. Add element at window_end to your window state
            window_count[ord(s2[end]) - ord('a')] += 1
            
            # 4. If window is bigger than pattern, shrink it
            if end - start + 1 > len(s1):
                # 5. Remove element at window_start from window state
                window_count[ord(s2[start]) - ord('a')] -= 1
                start += 1
                
            # 6. Update result - check if we found a valid permutation
            if end - start + 1 == len(s1):
                if s1_count == window_count:
                    return True
                    
            end += 1
        
        return False