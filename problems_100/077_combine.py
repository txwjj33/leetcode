'''
题目：组合
描述：
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

'''
递归，160 ms
'''
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k: return []
        if k == 1: return [[i] for i in range(1, n + 1)]
        t = self.combine(n - 1, k - 1)
        return [d + [n] for d in t] + self.combine(n - 1, k)


'''
124 ms
'''
import itertools
class Solution:
    def combine(self, n, k):
        return list(itertools.combinations(range(1, n+1), k))
