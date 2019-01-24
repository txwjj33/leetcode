'''
题目：最长回文子串
描述：
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

'''这是所有提交算法中最快的，利用了以下结论：
设当前最长的回文长度为max_len
则以i结尾的回文长度 <= max_len + 2
所以直接检查以i结尾的长度为max_len + 1 和max_len + 2是不是回文
这个方法在字符串较短时（本题<1000）比较快，但是字符串比较长是会比较慢
当s = 'a' * 70000 + 'b'时，这个算法时间是1400+ms，Manacher算法是140+ms，
最坏是O(n^2)
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2 or s==s[::-1]:
            return s
        start,max_len=0,1
        for i in range(1,len(s)):
            odd=s[i-max_len-1:i+1]
            even=s[i-max_len:i+1]

            if i-max_len-1>=0 and odd==odd[::-1]:
                start=i-max_len-1
                max_len+=2
                continue
            if i-max_len>=0 and even==even[::-1]:
                start=i-max_len
                max_len+=1

        return s[start:start+max_len]


'''Manacher算法，O(n)，
技巧1：在原字符串中间都插上#，这样原来的回文都会一一对应到一个新的回文，且新的回文长度为奇数。
新的回文的半径=原来回文长度+1
定义1：p[i]为以i为中心的最长回文的半径
定义2：mx和id，mx代表以id为中心的最长回文的右边界（开区间），也就是mx = id + p[id]
递推公式：if (i < mx)  p[i] = min(p[2 * id - i], mx - i)，j=2 * id - i为i关于id的对称点
公式说明：
1）如果p[j] < mx - i，那么以i为中心的最长回文就是j的最长回文关于id做对称
2）如果p[j] > mx - i，那么以i为中心的最长回文右边界就是mx-i，不能继续往右
3）如果p[j] = mx - i, 那么以i为中心的最长回文右边界是mx-i或者更右边的点
'''
class Solution(object):
    # 104 ms
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s==s[::-1]: return s
        s1 = '#'
        for c in s: s1 += c + '#'
        p = {0: 1}
        id = 0
        mx = 1
        # pi最大的值
        rIndex = 0
        for i in range(1, len(s1)):
            if i < mx:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1

            while(i - p[i] >= 0 and i + p[i] < len(s1) and s1[i - p[i]] == s1[i + p[i]]):
                p[i] += 1

            if mx < i + p[i]:
                # 只有i + p[i] > mx时，才更新
                id = i
                mx = i + p[i]
            if p[i] > p[rIndex]: rIndex = i

        sub = s1[rIndex - p[rIndex] + 1:rIndex + p[rIndex]]
        return sub.replace('#', '')

    # 92 ms
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s==s[::-1]: return s
        s1 = '#'
        for c in s: s1 += c + '#'
        p = {0: 1}
        id = 0
        mx = 1
        # pi最大的值
        rIndex = 0
        for i in range(1, len(s1)):
            if i < mx:
                j = 2 * id - i
                if p[j] < mx - i:
                    p[i] = p[j]
                elif p[j] > mx - i:
                    p[i] = mx - i
                else:
                    p[i] = mx - i
                    n1 = 2 * i - mx
                    n2 = mx
                    while(n1 >= 0 and n2 < len(s1) and s1[n1] == s1[n2]):
                        n1 -= 1
                        n2 += 1
                        p[i] += 1
            else:
                p[i] = 1
                n1 = i - 1
                n2 = i + 1
                while(n1 >= 0 and n2 < len(s1) and s1[n1] == s1[n2]):
                    n1 -= 1
                    n2 += 1
                    p[i] += 1

            if mx < i + p[i]:
                # 只有i + p[i] > mx时，才更新
                id = i
                mx = i + p[i]
            if p[i] > p[rIndex]: rIndex = i

        # 这种方法居然比sub.replace的方法还慢,是字符串的加法比较费时吗
        # rs = ''
        # for i in range(rIndex - p[rIndex] + 1, rIndex + p[rIndex]):
        #     if s1[i] != '#': rs += s1[i]
        # return rs
        sub = s1[rIndex - p[rIndex] + 1:rIndex + p[rIndex]]
        return sub.replace('#', '')


'''直接遍历查找，O(n^2)，516 ms
遍历字符串，找到以i为中心的最长回文，以及以i==i+1为中心的最长回文
优化点1：寻找最长回文之前先判断有没有可能比已知最长回文长
'''
class Solution(object):
    def find(self, s, i, j):
        while(i > 0 and j < len(s) - 1):
            if s[i - 1] != s[j + 1]:
                return i, j + 1
            i -= 1
            j += 1
        return i, j + 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '': return ''
        rStart, rStop = 0, 1
        for i in range(0, len(s)):
            # 检查i作为中心的回文是否有可能比当前最长回文更长
            if i > 0 and i < len(s) - 1 and s[i - 1] == s[i + 1]:
                l = rStop - rStart
                step = int(math.ceil(l / 2))
                n1 = i - step
                n2 = i + step
                if n1 >= 0 and n2 <= len(s) - 1 and s[n1] == s[n2]:
                    start, stop = self.find(s, i, i)
                    if stop - start > l:
                        rStart, rStop = start, stop

            # 检查i==i+1作为中心的回文是否有可能比当前最长回文更长
            if i < len(s) - 1 and s[i] == s[i + 1]:
                l = rStop - rStart
                step = int(math.floor(l / 2))
                n1 = i - step
                n2 = i + 1 + step
                if n1 >= 0 and n2 <= len(s) - 1 and s[n1] == s[n2]:
                    start, stop = self.find(s, i, i + 1)
                    if stop - start > l:
                        rStart, rStop = start, stop
        return s[rStart:rStop]


'''动态规划，O(n^2)，828ms
遍历字符串，subs保存所有以当前位结尾的回文的开始下标，升序排列
备注1：不要直接缓存最长的字符串，而是缓存开始结束下标，速度快多了
备注2：如果subs是字典，subs[i]保存所有的第i位结尾的回文，速度会慢些，猜想是内存分配占了时间？
备注3：必须保存所有的回文，因为当前哪怕最短的回文到后面也可能变成全局最长
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '': return ''
        # 保存以当前位结尾的所有回文的开始下标
        subs = [0]
        # 当前最长的回文的开始结束下标，结束下标是开区间
        rStart, rStop = 0, 1
        for i in range(1, len(s)):
            newSubs = []
            for j in subs:
                if j >= 1 and s[j - 1] == s[i]:
                    newSubs.append(j - 1)
            if s[i] == s[i - 1]:
                newSubs.append(i - 1)
            newSubs.append(i)
            if i - newSubs[0] + 1 >= rStop - rStart:
                rStart, rStop = newSubs[0], i + 1
            subs = newSubs

        return s[rStart:rStop]
