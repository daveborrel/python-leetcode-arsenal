class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Build pattern frequency map
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1

        # Initialize first window
        start = 0
        end = len(s1) - 1  # end points to last char of first window
        
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord("a")] += 1

        # Check first window
        if s1_count == window_count:
            return True
        
        # Slide window
        start = 0
        end = len(s1)  # end now points to first char after window
        
        while end < len(s2):
            # Remove leftmost character
            window_count[ord(s2[start]) - ord("a")] -= 1
            
            # Add new character
            window_count[ord(s2[end]) - ord("a")] += 1
            
            if s1_count == window_count:
                return True
                
            start += 1
            end += 1
        
        return False