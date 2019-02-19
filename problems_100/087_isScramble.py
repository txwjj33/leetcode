'''
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续将其节点 "eat" 和 "at" 进行交换，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

示例 1:

输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:

输入: s1 = "abcde", s2 = "caebd"
输出: false
'''


'''
将s1和s2分别分拆成长度对应的两个字符串，只要任一种分拆的两个子字符串都满足要求，那么s1和s2也满足要求
104 ms, 6.5 MB
'''
from collections import Counter
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counter1, counter2 = Counter(s1), Counter(s2)
        if counter1 != counter2: return False
        if len(s1) < 4: return True
        if s1 == s2: return True

        for i in range(len(s1) - 1):
            sub1, sub2 = s1[:i+1], s1[i+1:]
            if self.isScramble(sub1, s2[:i+1]) and self.isScramble(sub2, s2[i+1:]):
                return True
            if self.isScramble(sub1, s2[-i-1:]) and self.isScramble(sub2, s2[:-i-1]):
                return True
        return False


'''
在上述算法基础上做些优化，减少counter的计算次数
72 ms, 6.5 MB
defaultdict(int)比Counter效率高
'''
from collections import Counter, defaultdict
class Solution:
    def isScrambleHelper(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) < 4: return True

        def validate(dict1, dict2):
            for k in dict1:
                if k not in dict2 or dict1[k]!=dict2[k]:
                    return False
            return True

        leftCounter1 = defaultdict(int)
        # leftCounter2, rightCounter2 分别是从左右数字符的计数
        leftCounter2, rightCounter2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1) - 1):
            leftCounter1[s1[i]] += 1

            leftCounter2[s2[i]] += 1
            if validate(leftCounter1, leftCounter2):
                sub1, sub2 = s1[:i+1], s1[i+1:]
                if self.isScrambleHelper(sub1, s2[:i+1]) and self.isScrambleHelper(sub2, s2[i+1:]):
                    return True

            rightCounter2[s2[-i-1]] += 1
            if validate(leftCounter1, rightCounter2):
                sub1, sub2 = s1[:i+1], s1[i+1:]
                if self.isScrambleHelper(sub1, s2[-i-1:]) and self.isScrambleHelper(sub2, s2[:-i-1]):
                    return True
        return False

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counter1, counter2 = Counter(s1), Counter(s2)
        if counter1 != counter2: return False
        return self.isScrambleHelper(s1, s2)


'''
思路差不多，主要是不计算总的counter，对于s1和s2相同的来说
把s2反过来变成s3
56 ms, 6.5 MB
'''
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def validate(dict1, dict2):
            for k in dict1:
                if k not in dict2 or dict1[k]!=dict2[k]:
                    return False
            return True

        if len(s1)==1 and s1==s2:
            return True
        res=False
        dict1=collections.defaultdict(int)
        dict2=collections.defaultdict(int)
        dict3=collections.defaultdict(int)
        s3=s2[::-1]
        i=0
        while i<len(s1)-1:
            dict1[s1[i]]+=1
            dict2[s2[i]]+=1
            dict3[s3[i]]+=1
            if validate(dict1, dict2) and self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]) or validate(dict1, dict3) and self.isScramble(s1[:i+1], s3[:i+1]) and self.isScramble(s1[i+1:], s3[i+1:]):
                return True
            i+=1
        return False