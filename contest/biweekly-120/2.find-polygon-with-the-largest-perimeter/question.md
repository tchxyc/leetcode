# [100180. 找到最大周长的多边形][link] (Medium)

[link]: https://leetcode.cn/contest/biweekly-contest-120/problems/find-polygon-with-the-largest-perimeter/

给你一个长度为 `n` 的 **正** 整数数组 `nums` 。

**多边形** 指的是一个至少有 `3` 条边的封闭二维图形。多边形的 **最长边** 一定 **小于** 所有其他边长度
之和。

如果你有 `k` （ `k >= 3`）个 **正** 数 `a₁`， `a₂`， `a₃`, ...， `aₖ` 满足 `a₁ <= a₂ <= a₃ <= ... <=
aₖ` **且** `a₁ + a₂ + a₃ + ... + aₖ₋₁ > aₖ`，那么 **一定** 存在一个 `k` 条边的多边形，每条边的长度分
别为 `a₁` ， `a₂` ， `a₃` ， ...， `aₖ` 。

一个多边形的 **周长** 指的是它所有边之和。

请你返回从 `nums` 中可以构造的 **多边形** 的 **最大周长** 。如果不能构造出任何多边形，请你返回 `-1` 
。

**示例 1：**

```
输入：nums = [5,5,5]
输出：15
解释：nums 中唯一可以构造的多边形为三角形，每条边的长度分别为 5 ，5 和 5 ，周长为 5 + 5 + 5 = 15 。
```

**示例 2：**

```
输入：nums = [1,12,1,2,5,50,3]
输出：12
解释：最大周长多边形为五边形，每条边的长度分别为 1 ，1 ，2 ，3 和 5 ，周长为 1 + 1 + 2 + 3 + 5 = 12 
。
我们无法构造一个包含变长为 12 或者 50 的多边形，因为其他边之和没法大于两者中的任何一个。
所以最大周长为 12 。
```

**示例 3：**

```
输入：nums = [5,5,50]
输出：-1
解释：无法构造任何多边形，因为多边形至少要有 3 条边且 50 > 5 + 5 。
```

**提示：**

- `3 <= n <= 10⁵`
- `1 <= nums[i] <= 10⁹`
