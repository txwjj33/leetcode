'''
题目：报数
描述：
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。



示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
'''

'''
44ms
'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = {1: [1]}
        for i in range(2, n + 1):
            r = result[i - 1]
            result[i] = []
            pre = r[0]
            count = 1
            for j in range(1, len(r)):
                if r[j] == pre:
                    count += 1
                else:
                    result[i].extend([count, pre])
                    pre = r[j]
                    count = 1
            if count > 0:
                result[i].extend([count, pre])
        return ''.join([str(i) for i in result[n]])

