'''
题目：编辑距离
描述：
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
'''

'''
找出两个字符串的所有相同的子序列，子序列可以不连续
求每个子序列所需的编辑步数，取最小值
优化点1：把已经计算过的最小编辑距离保存下来，防止重复计算
优化点2：在循环i和j的时候，一旦大于distance，break
152 ms
'''
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = [{} for _ in range(len(word1))]

        def getDistance(index1, index2):
            if index1 == len(word1): return len(word2) - index2
            if index2 == len(word2): return len(word1) - index1
            if index2 in result[index1]: return result[index1][index2]

            s1, s2 = word1[index1:], word2[index2:]
            distance = max(len(s1), len(s2))
            for i in range(len(s1)):
                if i >= distance: break
                for j in range(len(s2)):
                    if j >= distance: break
                    if s1[i] == s2[j]:
                        count = max(i, j) + getDistance(i + 1 + index1, j + 1 + index2)
                        if count < distance: distance = count
            result[index1][index2] = distance
            return distance

        return getDistance(0, 0)


'''
从后往前动态规划
128 ms
'''
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = [{} for _ in range(len(word1) + 1)]

        def getDistance(i, j):
            if i == 0: return j
            if j == 0: return i
            if j in result[i]: return result[i][j]

            if word1[i - 1] == word2[j - 1]:
                distance = getDistance(i - 1, j - 1)
            else:
                distance = min(getDistance(i - 1, j - 1),
                              getDistance(i - 1, j),
                              getDistance(i, j - 1)) + 1
            result[i][j] = distance
            return distance

        return getDistance(len(word1), len(word2))
