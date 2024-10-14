import heapq
from math import ceil
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        res = 0
        for i in range(k):
            max_val = -heapq.heappop(heap)
            res += max_val
            new_val = ceil(max_val / 3)
            heapq.heappush(heap, -new_val)
        return res
