class SegTree:
    def __init__(self, nums) -> None:
        self.n = n = len(nums)
        N = n * 4
        self.nums = nums
        self.q = [0] * N
        self.lazy = [True] * N
        # root start from 0
        self.build(0, 0, n - 1)

    def calculate(self, o: int, l: int, r: int):
        self.q[o] = self.q[l] + self.q[r]

    def build(self, o: int, l: int, r: int):
        if l == r:
            self.q[o] = self.nums[l]
            return
        mid = (l + r) >> 1
        left, right = o * 2 + 1, o * 2 + 2
        self.build(left, l, mid)
        self.build(right, mid + 1, r)
        self.calculate(o, left, right)

    def update(self, o: int, l: int, r: int, L: int, R: int):
        if L == l and r == R:
            self.lazy[o] = not self.lazy[o]
            ones = self.q[o]
            zeros = R - L + 1 - ones
            self.q[o] = zeros
            return

        left, right = o * 2 + 1, o * 2 + 2
        mid = (l + r) >> 1

        if not self.lazy[o]:
            self.update(left, l, mid, l, mid)
            self.update(right, mid + 1, r, mid + 1, r)
            self.lazy[o] = True

        if R <= mid:
            self.update(left, l, mid, L, R)
        elif L > mid:
            self.update(right, mid + 1, r, L, R)
        else:
            self.update(left, l, mid, L, mid)
            self.update(right, mid + 1, r, mid + 1, R)

        self.calculate(o, left, right)

    def query(self, o: int, l: int, r: int, L: int, R: int):
        if L == l and r == R:
            return self.q[o]

        left, right = o * 2 + 1, o * 2 + 2
        mid = (l + r) >> 1

        if not self.lazy[o]:
            self.update(left, l, mid, l, mid)
            self.update(right, mid + 1, r, mid + 1, r)
            self.lazy[o] = True
        res = 0
        if R <= mid:
            res += self.query(left, l, mid, L, R)
        elif L > mid:
            res += self.query(right, mid + 1, r, L, R)
        else:
            res += self.query(left, l, mid, L, mid)
            res += self.query(right, mid + 1, r, mid + 1, R)

        return res
