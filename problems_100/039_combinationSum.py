'''
题目：组合总和
描述：
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

'''
直接递归，196 ms
下面两个思路是差不多的，不明白第二个为什么比第3个更快
第二个是求sub，然后传递sub，第三个是传index
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []
        if len(candidates) == 1:
            n = candidates[0]
            if target % n == 0 and target >= n:
                return [[n] * (target // n)]
            else:
                return []

        n = candidates[-1]
        result = []
        for i in range(target // n + 1):
            remain = target - n * i
            if remain == 0:
                result.append([n] * i)
            else:
                r = self.combinationSum(candidates[:-1], remain)
                for t in r:
                    if i > 0:
                        t.extend([n] * i)
                    result.append(t)
        return result


'''
80 ms
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []

        def combination(candidates, target):
            n = candidates[0]
            if target < n:
                return []

            result = []
            if target % n == 0:
                result.append([n] * (target // n))
            if len(candidates) == 1: return result

            sub = candidates[1:]
            for i in range(target // n + 1):
                remain = target - n * i
                if remain > 0:
                    r = combination(sub, remain)
                    for t in r:
                        result.append([n] * i + t)
            return result

        candidates.sort()
        return combination(candidates, target)


'''
116 ms
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []

        def combination(candidates, target, index):
            n = candidates[index]
            if target < n:
                return []

            result = []
            if target % n == 0:
                result.append([n] * (target // n))
            if index == len(candidates) - 1: return result

            for i in range(target // n + 1):
                remain = target - n * i
                if remain > 0:
                    r = combination(candidates, remain, index + 1)
                    for t in r:
                        result.append([n] * i + t)
            return result

        candidates.sort()
        return combination(candidates, target, 0)


'''
72 ms
'''
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, index, path, res):
            if target == 0:
                return res.append(path)
            elif target < 0:
                return False
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res


'''
m[i]代表所有和为target-i的组合，从后往前遍历求m，68 ms
'''
class Solution:
    def combinationSum(self, candidates, target):
        m = [[] for i in range(target)]
        for n in candidates:
            if target - n > -1:
                m[target - n].append([n])
            for s in range(target-1, n-1, -1):
                for entry in m[s]:
                    m[s - n].append(entry + [n])
        return m[0]