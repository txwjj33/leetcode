'''
题目：单词搜索
描述：
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
'''

'''
BFS，212 ms
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
