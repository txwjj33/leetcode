'''
题目：缺失的第一个正数
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
'''

'''
44ms
'''
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            if n > 0: dic[n] = True
        i = 1
        while True:
            if i not in dic:
                return i
            else:
                i += 1
                continue

'''
用了一个很慢的方法，取正数，排序，然后找最小未出现的
44 ms，击败了了99.63%的用户。。
'''
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsP = [i for i in nums if i > 0]
        numsP.sort()
        m = 1
        for i in range(0, len(numsP)):
            if numsP[i] == m:
                m += 1
            elif numsP[i] < m:
                continue
            else:
                return m
        return m
