'''
题目：全排列
描述：
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

import copy
import itertools

# 以下算法中写的都是在sublime里面计算list(range(10))的时间

'''
回溯法寻找所有排列, 使用二分法找到remain中第一个比n大的数，86s
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        nums.sort()
        result = [copy.deepcopy(nums)]
        ans = nums    # 当前确定的数字
        remain = []   # 还未确定的数字，remain为空时开始回溯
        # 回溯完以后ans长度为0，说明回溯之前ans是逆序排列的，已经是最后一个了
        while len(ans) > 0:
            # 开始回溯
            while len(ans) > 0:
                n = ans.pop()
                if len(remain) == 0 or n > remain[-1]:
                    remain.append(n)
                else:
                    # 回溯停止，生成下一个排列
                    # remain正好是顺序排列，找到remain中第一个比n大的数
                    left, right = 0, len(remain)
                    while left < right:
                        mid = left + (right - left) // 2
                        if remain[mid] < n:
                            left = mid + 1
                        else:
                            right = mid
                    # 把left的数放在n的位置上，剩下的数从小到大，这就是下一个排列
                    ans.append(remain[left])
                    remain[left] = n
                    ans.extend(remain)
                    result.append(copy.deepcopy(ans))
                    remain = []
                    break

        return result


'''
最快的代码，没啥好说的，几乎是瞬间
'''
class Solution:
    def permute(self, nums):
        return list(itertools.permutations(nums))


'''
某个数字放在最后，其余的数字直接使用递归，37.5
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        results = []
        for index in range(len(nums)):
            for item in self.permute(nums[:index] + nums[index+1:]):
                results.append([nums[index]] + item)

        return results

'''
广度优先（BFS），92.1
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        results = []
        counts = {n:0 for n in nums}
        ans = []

        def search():
            if len(ans) == len(nums):
                results.append(copy.deepcopy(ans))
                return
            for n in nums:
                if counts[n] == 0:
                    counts[n] = 1
                    ans.append(n)
                    search()
                    ans.pop()
                    counts[n] = 0

        search()
        return results


'''
广度优先优化（BFS），每个答案少一次search，pop，append，21s
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        results = []
        counts = {n:0 for n in nums}
        ans = []

        def search():
            for n in nums:
                if counts[n] == 1: continue
                if len(ans) == len(nums) - 1:
                    results.append(ans + [n])
                    break

                counts[n] = 1
                ans.append(n)
                search()
                ans.pop()
                counts[n] = 0

        search()
        return results


'''
递归思想，n-1个数的排列求出来以后，把第n个数插入前面每个排列的每个位置，都是一个新的排列，且不会重复，8.2s
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def combine(tList,x):
            res =[]
            for i in range(len(tList)+1):
                l = tList[:]
                l.insert(i,x)
                res.append(l)
            return res

        l = nums.pop()
        res =[[l]]
        while len(nums)>0:
            x = nums.pop()
            test = []
            for i in res:
                test += combine(i , x)
            res = test
        return res


'''
这就是前一个算法的简化写法
'''
class Solution:
    def permute(self, nums):
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
            result = newResult
        return result