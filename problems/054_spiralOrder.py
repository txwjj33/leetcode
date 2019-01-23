'''
题目：螺旋矩阵
描述：
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

'''
40 ms
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        if len(matrix) == 1: return matrix[0]
        m, n = len(matrix), len(matrix[0])
        result = []
        for i in range(min(m, n) // 2 + 1):
            # 上边
            if m - 1 - i >= i:
                result.extend(matrix[i][i : n-i])

            # 右边
            if n - 1 - i >= i:
                for j in range(i + 1, m - i):
                    result.append(matrix[j][n - 1 - i])

            # 下边
            if m - 1 - i > i:
                t = reversed(matrix[m - 1 - i][i : n-i-1])
                result.extend(t)

            # 左边
            if n - 1 - i > i:
                for j in range(m - 2 - i, i, -1):
                    result.append(matrix[j][i])

        return result
