'''
题目：Z 字形变换
描述：
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''

'''
遍历字符串，将其放在相应的行里，然后把各行连起来就行，O(n)，64 ms
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        lines = [''] * numRows
        lines[0] = s[0]
        curLine = 0
        down = True
        for i in range(1, len(s)):
            if down:
                curLine += 1
                lines[curLine] += s[i]
                if curLine == numRows - 1:
                    down = False
            else:
                curLine -= 1
                lines[curLine] += s[i]
                if curLine == 0:
                    down = True
        return ''.join(lines)