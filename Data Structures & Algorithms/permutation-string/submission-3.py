class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        m, n = len(s1), len(s2)
        if m > n:
            return False
        need = Counter(s1)
        window = Counter(s2[:m])
        if need == window:
            return True
        
        for r in range(m, n):
            left_char = s2[r-m]
            right_char = s2[r]
            window[left_char] -= 1
            window[right_char] += 1
            print(window)
            if window[left_char] == 0:
                del window[left_char]
            
            if need == window:
                return True
        return False