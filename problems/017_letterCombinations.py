'''
题目：电话号码的字母组合
描述：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
注意：
尽管题目说的是求组合，但是从测试用例给的结果看，实际上是求排列
'''

'''
求排列多简单， 28 ms
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        digitDict = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        r = ['']
        for c in digits:
            rBack = r
            r = []
            for s in rBack:
                for s1 in digitDict[int(c)]:
                    r.append(s + s1)
        return r


'''
以下方法求的是组合
'''
class Solution(object):
    # count个数，每个数可能是[0, indexMax)中的整数，共有多少种组合
    # 用递归求解，将已有的结果保存
    def calCombine(self, count, indexMax):
        if indexMax not in self.combinations:
            self.combinations[indexMax] = {1: [[i] for i in range(0, indexMax)]}
        combinations = self.combinations[indexMax]
        if count <= len(combinations): return
        for i in range(len(combinations) + 1, count + 1):
            combinations[i] = []
            for pList in combinations[i - 1]:
                # 为了防止重复, 保证pList[-1] <= j
                for j in range(pList[-1], indexMax):
                    combinations[i].append(pList + [j])

    # 长度为count，每个字母是strs里面的某一个，不同的组合个数
    def createStrs(self, count, strs):
        self.calCombine(count, len(strs))
        r = []
        for pList in self.combinations[len(strs)][count]:
            s = ''
            for i in pList:
                s += strs[i]
            r.append(s)
        return r

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.combinations =  {}
        counts = {}
        for c in digits:
            n = int(c)
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1
        digitDict = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        r = []
        for d, count in counts.items():
            strs = self.createStrs(count, digitDict[d])
            if len(r) == 0:
                r = strs
                continue
            rBack = r
            r = []
            for s in rBack:
                for s1 in strs:
                    r.append(s + s1)
        return r
