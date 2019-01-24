'''
题目：x 的平方根
描述：
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''


'''
牛顿迭代法，y = (y + n / y) / 2, y收敛到sqrt(n), 64 ms
'''
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        y = x
        while True:
            t = (y + x / y) / 2
            if abs(t - y) < 1:
                return int(t)
            else:
                y = t
