def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
        
    # Create frequency maps
    s1_count = [0] * 26
    window_count = [0] * 26
    
    # Fill s1 frequency map
    for c in s1:
        s1_count[ord(c) - ord('a')] += 1
    
    # Initialize first window
    for i in range(len(s1)):
        window_count[ord(s2[i]) - ord('a')] += 1
    
    # Check first window
    if s1_count == window_count:
        return True
    
    # Slide window
    for i in range(len(s1), len(s2)):
        # Remove leftmost character
        window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
        # Add new character
        window_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == window_count:
            return True
            
    return False