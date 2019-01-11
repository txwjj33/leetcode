'''
题目：与所有单词相关联的字串
描述：
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:

输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2:

输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
输出: []
!!!!!注意这个例子是与题目矛盾的，题目说的是一些长度相同的单词 words！！！
'''


'''
以下方法仅适用于words里面的单词长度一样，递归求解，92 ms
answers如果用list，那么需要answers.count(w)，时间长点，140ms
'''
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0: return []
        length = len(words[0])
        if len(s) < length * len(words): return []

        wordCount = {} # words中每个不同单词的出现次数
        for w in words:
            wordCount[w] = wordCount.get(w, 0) + 1

        result = []
        # 验证index是否满足条件，[index, cur]中间的字符串是answers，是之前已经求出来的
        def check(index, cur, answers):
            if index > len(s) - length * len(words): return

            while True:
                w = s[cur:cur + length]
                if w not in wordCount:
                    # 验证失败，且[index, cur]中间的数（与index对于length同余）都会失败
                    # 直接从cur + length开始验证
                    check(cur + length, cur + length, {})
                    return

                if answers.get(w, 0) + 1 > wordCount[w]:
                    # 验证失败
                    head = s[index:index + length]
                    answers[head] -= 1
                    check(index + length, cur, answers)
                    return

                answers[w] = answers.get(w, 0) + 1
                cur += length
                if cur == index + length * len(words):
                    # 验证成功
                    result.append(index)
                    head = s[index:index + length]
                    answers[head] -= 1
                    check(index + length, cur, answers)
                    return

        for i in range(length):
            index = i
            check(i, i, {})

        return result


'''
以下用回溯法求，可以处理words里面的单词长度不一样的情况，196 ms
求出每个点上可能匹配的字符串，然后使用回溯法求解所有情况
优化点1、记录words中各个单词出现的次数，求解的时候相同的单词不用尝试两遍了
优化点2、验证某个i的时候，设i这个单词的结束为止为index，则从index开始，记录最长的只有唯一选择的answers，
当验证index是，可以直接使用，不需要重复计算
备注1、如果假设words中不存在某个单词是另一个单词的前缀，那么match表中都至多只有一个匹配的，因此不存在回溯的情况，
以下代码可以做很多优化
'''
class Solution:
    def calMatchDict(self, s, words):
        firstChar = {}      # words里首字母的表，用于加快match的计算
        self.lengthSum = 0  # words里所有单词的长度和
        self.wordCount = {} # wrods中每个不同单词的出现次数
        i = 0
        while i < len(words):
            w = words[i]
            if w == '':
                words.pop(i)
            else:
                charDict = firstChar.setdefault(w[0], {})
                charDict[w] = charDict.get(w, 0) + 1
                self.wordCount[w] = self.wordCount.get(w, 0) + 1
                self.lengthSum += len(w)
                i += 1

        self.match = {}          # s中每个位置匹配words中的单词
        self.matchCount = {}     # math中不同的单词的出现次数
        for i in range(len(s)):
            c = s[i]
            if c not in firstChar: continue
            for w in firstChar[c]:
                if s[i:i + len(w)] != w: continue
                match = self.match.setdefault(i, [])
                match.append(w)
                self.matchCount[w] = self.matchCount.get(w, 0) + 1
        # print(self.match)

    def checkByIndex(self, words, i):
        unique = True
        answers = self.uniqueAnswers.get(i, [])
        if len(answers) > 0:
            # 直接利用之前已经求出的结果
            index = self.uniqueIndexs[i]
            pullbackIndexs = {} # 需要回溯的index

            indexForUnique = i + len(answers[0])
            self.uniqueAnswers[indexForUnique] = answers[1:]
            self.uniqueIndexs[indexForUnique] = index
        else:
            match = self.match[i]
            answers = [match[0]]  # 当前尝试的答案中的单词
            index = i + len(match[0])
            pullbackIndexs = {} # 需要回溯的index
            if len(match) > 1:
                pullbackIndexs[i] = match[1:]

            indexForUnique = index
            self.uniqueAnswers[indexForUnique] = []
            self.uniqueIndexs[indexForUnique] = -1

        while True:
            # print(answers)
            match = self.match.get(index, [])
            # 当前位置可以尝试的单词
            validWords = [w for w in match if answers.count(w) < self.wordCount[w]]
            if len(validWords) > 0:
                # curIndex的位置取validWords[0]
                w = validWords[0]
                answers.append(w)
                index += len(w)

                # 更新uniqueAnswers和uniqueIndexs
                if len(match) == 1:
                    if unique:
                        self.uniqueAnswers[indexForUnique].append(w)
                        self.uniqueIndexs[indexForUnique] = index
                else:
                    unique = False

                if len(answers) == len(words):
                    # 找到了一个答案
                    self.result[i] = True
                    break
                else:
                    if len(validWords) > 1:
                        pullbackIndexs[index] = validWords[1:]
                    continue

            unique = False
            if len(pullbackIndexs) == 0:
                # 不存在回溯的index，break
                break

            # 开始回溯
            while len(answers) > 0:
                word = answers.pop()
                index -= len(word)
                if index in pullbackIndexs:
                    w = pullbackIndexs[index].pop(0)
                    answers.append(w)
                    if len(pullbackIndexs[index]) == 0:
                        del pullbackIndexs[index]
                    break

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0: return []
        self.calMatchDict(s, words)
        if len(s) < self.lengthSum: return []

        for w in self.wordCount:
            if self.matchCount.get(w, 0) < self.wordCount[w]:
                # match中的次数小于words中的次数，肯定没法匹配
                return []

        # 使用回溯法寻找可能的答案
        self.result = {}
        self.uniqueAnswers = {}  # 从i开始的最长的只有唯一可选项的answers
        self.uniqueIndexs = {}   # 从i开始的最长的只有唯一可选项的answer的末尾的index
        for i in range(len(s) - self.lengthSum + 1):
            # print(i)
            if i not in self.match: continue
            if i in self.result: continue
            if len(words) == 1: self.result[i] = True

            self.checkByIndex(words, i)

        return [i for i in self.result if self.result[i] == True]
