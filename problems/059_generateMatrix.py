'''
题目：螺旋矩阵 II
描述：
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

'''
44 ms
'''
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # !!不能使用result = [[0] * n] * n的写法，否则result中的各个list实际上都指向同一个实例
        result = [[0] * n for i in range(n)]
        cur = 1
        for i in range(n // 2):
            # 上边
            for j in range(i, n - i):
                result[i][j] = cur
                cur += 1
            # 右边
            for j in range(i + 1, n - i):
                result[j][n - i - 1] = cur
                cur += 1
            # 下边
            for j in range(n - i - 2, i - 1, -1):
                result[n - i - 1][j] = cur
                cur += 1
            # 左边
            for j in range(n - i - 2, i, -1):
                result[j][i] = cur
                cur += 1
        if n % 2 == 1:
            result[n // 2][n // 2] = cur
        return result
