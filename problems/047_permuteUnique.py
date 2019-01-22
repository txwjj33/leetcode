'''
题目：全排列 II
描述：
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

'''
递归思想，n-1个数的排列求出来以后，把第n个数插入前面每个排列的每个位置，都是一个新的排列，且不会重复，8.2s
为了防止重复，每一个n只能插到前一个n的前面
'''
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for n in nums:
            newResult = []
            for t in result:
                for i in range(len(t) + 1):
                    newResult.append(t[:i] + [n] + t[i:])
                    if i < len(t) and t[i] == n:
                        break
            result = newResult
        return result
