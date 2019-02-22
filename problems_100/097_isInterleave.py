'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
'''

'''
44 ms, 6.6 MB
'''
class Solution:
    def isInterleave(self, s1: 'str', s2: 'str', s3: 'str') -> 'bool':
        if len(s3) != len(s1) + len(s2): return False
        # cache[(i, j)]表示isInterleave(s1[i:]，s2[j:]，s3[i+j:])
        cache = {}

        def helper(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(s1):
                cache[(i, j)] = s2[j:] == s3[len(s1) + j:]
            elif j == len(s2):
                cache[(i, j)] = s1[i:] == s3[i + len(s2):]
            else:
                cache[(i, j)] = False
                if (s1[i] == s3[i + j]) and helper(i + 1, j):
                    cache[(i, j)] = True
                elif (s2[j] == s3[i + j]) and helper(i, j + 1):
                    cache[(i, j)] = True
            return cache[(i, j)]
        return helper(0, 0)
