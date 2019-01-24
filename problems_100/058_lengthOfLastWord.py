'''
题目：最后一个单词的长度
描述：
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
'''

'''
二分查找插入以后，使用56题类似的算法，44 ms
'''
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = -1  # 单词的结尾
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if index != -1:
                    return index - i
            else:
                if index == -1:
                    index = i
        return index + 1


'''
s.split()就是按空格隔开，并且去掉多余空格，40 ms
'''
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return 0 if len(words) == 0 else len(words[-1])