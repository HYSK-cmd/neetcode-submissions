class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for x in nums:
            d[x] = d.get(x, 0) + 1
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in d.items():
            buckets[freq].append(num)
        res = []
        n = len(buckets)-1
        print(buckets)
        while k > 0 and n >= 0:
            if not buckets[n]:
                n -= 1
                continue
            for i in range(len(buckets[n])):
                res.append(buckets[n][i])
                k -= 1
            n -= 1
        return res
            

