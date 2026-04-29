from _heapq import heapify
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            last = -heapq.heappop(stones)
            second_last = -heapq.heappop(stones)
            if last != second_last:
                heapq.heappush(stones, -(last-second_last))
        if not stones:
            return 0
        return -stones[0]