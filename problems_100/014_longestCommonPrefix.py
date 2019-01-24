'''
题目：最长公共前缀
描述：
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
'''

'''
48 ms
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ''
        lens = [len(str) for str in strs]
        m = min(lens)
        if m == 0: return ''
        for i in range(0, m):
            c = strs[0][i]
            for str in strs:
                if str[i] != c:
                    return strs[0][0:i]
        return strs[0][0:m]
