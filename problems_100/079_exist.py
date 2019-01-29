'''
题目：子集
描述：
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

'''
递归，48 ms
'''
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0: return True
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        if n == 0: return False
        flag = [[0] * n for _ in range(m)]

        def check(i, j, index):
            if index == len(word): return True
            result = False
            if flag[i][j] == 0:
                if board[i][j] == word[index]:
                    flag[i][j] = 1
                    result = checkAround(i, j, index + 1)
                    flag[i][j] = 0
            return result

        def checkAround(i, j, index):
            if index == len(word): return True
            if i > 0 and check(i - 1, j, index):
                return True
            if i < m - 1 and check(i + 1, j, index):
                return True
            if j > 0 and check(i, j - 1, index):
                return True
            if j < n - 1 and check(i, j + 1, index):
                return True
            return False

        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False
