'''
题目：组合总和 II
描述：
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''

'''
先求每个数的出现次数，然后排序，递归，132 ms
'''
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []

        counts = {}
        for n in candidates:
            counts[n] = counts.get(n, 0) + 1
        keys = [i for i in counts]
        keys.sort()

        def dfs(target, index, path, result):
            n = keys[index]
            for i in range(counts[n] + 1):
                if n * i > target:
                    break
                if n * i == target:
                    result.append(path + [n] * i)
                    break
                if index < len(keys) - 1:
                    dfs(target - n * i, index + 1, path + [n] * i, result)

        result = []
        dfs(target, 0, [], result)
        return result


'''
排序，递归，56 ms
'''
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []

        # 求出candidates[index:]中和为target的组合
        def dfs(target, index, path, result):
            # 遍历i，所求和中第一个数是在第i位，也就是说从[index, i]都不选
            for i in range(index, len(candidates)):
                n = candidates[i]
                # 通过以下方式排除掉重复的
                if i > index and n == candidates[i - 1]:
                    continue
                if n > target:
                    break
                if n == target:
                    result.append(path + [n])
                    break
                dfs(target - n, i + 1, path + [n], result)

        result = []
        candidates.sort()
        dfs(target, 0, [], result)
        return result
