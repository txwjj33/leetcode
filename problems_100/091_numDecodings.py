'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''


'''
动态规划
52 ms, 8 MB
'''
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        if len(s) == 0: return 0
        if len(s) == 1: return 1 if s != '0' else 0

        def cal(i):
            # 计算s[i:]的解码数
            if i >= len(s): return 1
            if s[i] == '0': return 0
            if i == len(s) - 1: return 1
            if i in cache: return cache[i]

            if int(s[i : i+2]) <= 26:
                num = cal(i + 1) + cal(i + 2)
            else:
                num = cal(i + 1)
            cache[i] = num
            return num

        return cal(0)
