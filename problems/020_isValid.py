'''
题目：接雨水
描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''

'''
用一个栈后进先出就完了，44 ms
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = []
        dict = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in '([{':
                li.append(c)
            else:
                if len(li) > 0 and li[-1] == dict[c]:
                    li.pop(-1)
                else:
                    return False
        return len(li) == 0
