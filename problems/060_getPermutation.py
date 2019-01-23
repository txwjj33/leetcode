'''
题目：第k个排列
描述：
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''

'''
48 ms
'''
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 计算阶乘
        f = {0:1}
        for i in range(1, n):
            f[i] = f[i - 1] * i

        remain = [str(i) for i in range(1, n + 1)]
        result = ''
        for i in range(n - 1, 0, -1):
            # 固定某个数字开头，后面n-1个数字的全排列有(n-1)!种，
            # 因此[1, (n-1)!]中的排列都是1开头
            # 而第k个排列的开头可以使用(k - 1) // (n-1)!来确定
            index = (k - 1) // f[i]
            result += remain.pop(index)
            k -= f[i] * index
        result += remain[0]
        return result
