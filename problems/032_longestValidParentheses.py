'''
题目：最长有效括号
描述：
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''

'''
1、用栈存储左括号，这样来快速找到某个右括号的配对
2、动态规划，maxLength表示以第k位结尾的最长的有效括号长度
60 ms
'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxLength = {}   # (k, v)表示以第k位结尾的最长的有效括号长度是v
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0: continue
                index = stack.pop(-1)  # 对应的左括号的index
                if index - 1 in maxLength:
                    maxLength[i] = maxLength[index - 1] + i - index + 1
                else:
                    maxLength[i] = i - index + 1

        if len(maxLength) == 0:
            return 0
        else:
            return max(maxLength.values())


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        start = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    # 当找到配对的左括号时，考虑以i结尾的最长的有效括号，设起点为s
                    # s-1如果是左括号，那么必须等于stack[-1]，就是以下的if部分
                    # s-1如果是右括号，那么是单独没配对的括号，就是以下的else部分
                    if stack:
                        l = i - stack[-1]
                    else:
                        l = i - start
                    if l > maxlen:
                        maxlen = l
                else:
                    start = i
        return maxlen
