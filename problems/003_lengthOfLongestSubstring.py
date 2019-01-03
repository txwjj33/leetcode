'''
题目：无重复字符的最长子串
描述：
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

'''
滑动窗口，记录每个元素的索引，O(n)，56 ms
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        sub = {}
        subStart = 0
        for i in range(0, len(s)):
            v = s[i]
            if v in sub:
                if sub[v] >= subStart:
                    l = i - subStart
                    if l > max: max = l
                    subStart = sub[v] + 1
            sub[v] = i
        l = len(s) - subStart
        if l > max: max = l
        return max


'''
记录最长无重复子串，O(n^2)，104 ms
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        sub = ''
        subLen = 0
        for i in s:
            find = False
            for j in range(0, len(sub)):
                if sub[j] == i:
                    sub = sub[j + 1:] + i
                    find = True
                    subLen = len(sub)
                    break
            if not find:
                sub = sub + i
                subLen += 1
                if subLen > max: max = subLen
        return max