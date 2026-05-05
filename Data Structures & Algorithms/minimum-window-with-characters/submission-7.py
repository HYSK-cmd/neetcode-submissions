class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        n, m = len(s), len(t)
        if n < m:
            return ""
        
        t1 = Counter(t)
        lst = []
        mn = 1000
        ans = None
        for r in range(n):
            right_ch = s[r]
            if right_ch in t1:
                s1 = Counter()
                j = r
                while j < n:
                    if s[j] in t1:
                        s1[s[j]] += 1
                    j += 1
                    if all(s1[ch] >= t1[ch] for ch in t1):
                        sub_len = len(s[r:j])
                        if sub_len < mn:
                            ans = s[r:j]
                            mn = sub_len
                        break
        if ans is None:
            return ""
        return ans