class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        l = 0
        mx = 0
        for r in range(len(s)):
            while s[r] in sset:
                sset.remove(s[l])
                l += 1
            sset.add(s[r])
            mx = max(mx, r-l+1)
        return mx
