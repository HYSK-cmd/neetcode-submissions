class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            key = {}
            for ch in s:
                key[ch] = key.get(ch, 0) + 1
            
            k = frozenset(key.items())

            if k not in group:
                group[k] = []
            group[k].append(s)
        
        ans = [x for x in group.values()]
        return ans