'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''


'''
68 ms, 6.4 MB
'''
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.helper(s, 4)

    # 解析字符串从n段0到255的数字
    def helper(self, s, n):
        if len(s) == 0: return []

        if s[0] == '0':
            if n == 1:
                return [s] if len(s) == 1 else []
            else:
                temp = self.helper(s[1:], n - 1)
                return ['0.' + t for t in temp]

        if n == 1:
            return [s] if int(s) <= 255 else []
        l = max(1, len(s) - 3 * (n - 1))
        r = min(3, len(s) - 1 * (n - 1))
        result = []
        for i in range(l, r + 1):
            a, b = s[:i], s[i:]
            if int(a) > 255: continue
            temp = self.helper(b, n - 1)
            for t in temp:
                result.append(a + '.' + t)
        return result
