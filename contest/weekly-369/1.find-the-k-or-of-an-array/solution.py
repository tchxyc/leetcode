# Created by Jones at 2023/10/29 10:30
# leetgo: dev
# https://leetcode.cn/problems/find-the-k-or-of-an-array/
# https://leetcode.cn/contest/weekly-contest-369/problems/find-the-k-or-of-an-array/

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
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = [0] * 32

        for x in nums:
            for i in range(32):
                if x >> i & 1:
                    cnt[i] += 1

        res = 0
        for i in range(32):
            if cnt[i] >= k:
                res |= 1 << i
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKOr(nums, k)

    print("\noutput:", serialize(ans))
