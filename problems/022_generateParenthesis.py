'''
题目：括号生成
描述：
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


'''
动态规划，从1开始把所有的算出来保存，44 ms
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = {}
        result[0] = ['']
        result[1] = ['()']
        for i in range(2, n + 1):
            # 计算result[i]， 考虑第一对个括号中间包含的括号对，可能是0 - i-1
            result[i] = []
            for j in range(0, i):
                for s1 in result[j]:
                    for s2 in result[i - 1 - j]:
                        result[i].append('({}){}'.format(s1, s2))
        return result[n]
