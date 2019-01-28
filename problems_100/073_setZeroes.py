'''
题目：矩阵置零
描述：
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
'''

'''
第一次遍历使用位移操作记录哪些行和列有0
第二次遍历置0
108 ms
'''
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        line, col = 0, 0
        for i, tList in enumerate(matrix):
            for j, v in enumerate(tList):
                if v == 0:
                    line |= 1 << i
                    col |= 1 << j
        for i, tList in enumerate(matrix):
            lineFlag = line & (1 << i)
            for j in range(len(tList)):
                if lineFlag != 0 or (col & (1 << j) != 0):
                    tList[j] = 0
