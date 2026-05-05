class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        import copy
        d = defaultdict(int)
        for i in range(len(s1)):
            d[s1[i]] += 1
        
        s = copy.deepcopy(d)
        for i in range(len(s2)-len(s1)+1):
            k = i
            
            for _ in range(len(s1)):
                if s2[k] in s:
                    if s[s2[k]] == 0:
                        break
                    s[s2[k]] -= 1
                else:
                    break
                k += 1
            if sum(s.values()) == 0:
                return True
            s = copy.deepcopy(d)
        return False
