'''
题目：两数相除
描述：
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''

'''
92 ms
'''
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0: return 0
        if dividend == -2 ** 31 and divisor == -1: return 2 ** 31 - 1

        a = abs(dividend)
        b = abs(divisor)
        back = b
        r = 0
        while a >= b:
            t = 1
            # <<1相当于乘以2
            while a >= b:
                a -= b
                r += t
                b <<= 1
                t <<= 1
            b = back

        if dividend < 0:
            r = -r
        if divisor < 0:
            r = -r
        return r

'''
1、使用位移操作符实现乘2和除2
2、找到最小的2^n * divisorP > dividendP
84 ms
'''
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0: return 0
        if dividend == -2 ** 31 and divisor == -1: return 2 ** 31 - 1
        if divisor == 1: return dividend
        if divisor == -1: return -dividend

        dividendP = abs(dividend)
        divisorP = abs(divisor)
        back = divisorP
        r = 0
        while dividendP >= divisorP:
            t = 1
            # <<1相当于乘以2，找到最小的2^n * divisorP > dividendP
            while dividendP > divisorP:
                divisorP <<= 1
                t <<= 1

            if divisorP == dividendP:
                r += t
                break
            else:
                # >>1相当于除以2
                r += t >> 1
                dividendP -= divisorP >> 1
                divisorP = back

        if dividend < 0:
            r = -r
        if divisor < 0:
            r = -r
        return r
