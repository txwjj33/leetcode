'''
题目：文本左右对齐
描述：
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''


'''
48 ms
'''
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        length = len(words[0])
        lineWords = [words[0]]
        for word in words[1:]:
            # 单词间至少要有一个空格
            if length + len(word) + 1 <= maxWidth:
                length += len(word) + 1
                lineWords.append(word)
            else:
                remain = maxWidth - length
                count = len(lineWords) - 1
                if count == 0:
                    result.append(lineWords[0] + ' ' * remain)
                else:
                    n = remain // count
                    a = remain % count
                    line = ''
                    for i in range(len(lineWords) - 1):
                        line += lineWords[i]
                        # length的计算中已经有了一个空格，所以这里要多加一个空格
                        if a > 0:
                            line += ' ' * (n + 2)
                            a -= 1
                        else:
                            line += ' ' * (n + 1)
                    line += lineWords[-1]
                    result.append(line)

                length = len(word)
                lineWords = [word]

        result.append(' '.join(lineWords))
        result[-1] += ' ' * (maxWidth - length)
        return result
