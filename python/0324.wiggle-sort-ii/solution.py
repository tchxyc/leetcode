# Created by Jones at 2023/12/21 15:43
# leetgo: dev
# https://leetcode.cn/problems/wiggle-sort-ii/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, log2, perm, sqrt
from operator import xor
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = sorted(nums)
        half = (len(nums) + 1) // 2
        nums[::2] = tmp[:half][::-1]
        nums[1::2] = tmp[half:][::-1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    wiggleSort(nums)
    ans = nums

    print("\noutput:", serialize(ans))
