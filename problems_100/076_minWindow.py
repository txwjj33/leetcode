'''
题目：最小覆盖子串
描述：
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''

'''
[left, right)记录结果的两端，遍历s，找到一个包含t的子串，然后把left右移
直到[left, right)恰好不含t，再继续遍历s
优化点1：missedChar记录left右移时少的那个字符，遍历s时只需找到这个字符就行
104 ms
'''
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def isBig(d1, d2):
            for k in d2:
                if (k not in d1) or (d1[k] < d2[k]):
                    return False
            return True

        if s == '' or t == '': return ''
        counts = {}
        for c in t:
            counts[c] = counts.get(c, 0) + 1

        left, right = -1, -1
        curCount = {}
        result = ''
        missedChar = None
        for i, c in enumerate(s):
            if c not in counts: continue

            curCount[c] = curCount.get(c, 0) + 1
            if left == -1: left = i
            if missedChar:
                if c != missedChar: continue
            else:
                if curCount[c] < counts[c]: continue
                if not isBig(curCount, counts): continue
            right = i + 1

            # left往右移， 直到(left, right)不含t
            # 同时也能找到以right结尾的最小的满足条件子串
            while True:
                c = s[left]
                if c in counts:
                    curCount[c] -= 1
                    if curCount[c] < counts[c]:
                        if not result or (right - left < len(result)):
                            result = s[left:right]
                            # 当找到result跟t的长度一样时，已经是最小可能的长度了，直接返回
                            if len(result) == len(t): return result

                        missedChar = c
                        left += 1
                        break
                left += 1

        return result


'''
算法跟上一个差不太多，写法上优化了不少，主要是充分发挥count的作用
100 ms
'''
from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == '' or t == '': return ''
        count = defaultdict(int)
        for c in t:
            count[c] += 1
        tLen = len(t)

        minL, minR = 0, len(s)
        l = 0
        for i, c in enumerate(s):
            if count[c] > 0:
                tLen -= 1
            count[c] -= 1

            if tLen == 0:
                while(count[s[l]] < 0):
                    count[s[l]] += 1
                    l += 1
                if i - l < minR - minL:
                    minL, minR = l, i

                count[s[l]] += 1
                l += 1
                tLen += 1

        return '' if minR == len(s) else s[minL:minR + 1]
