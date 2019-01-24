'''
题目：解数独
描述：
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
'''

'''
回溯法，48 ms
'''
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # line = [set()] * 9，这种写法line里面的所有元素其实都是指向一个set实体，改一个就全改了。。
        line = [set() for i in range(9)]   # 每一行已经包含的数字
        col = [set() for i in range(9)]    # 每一列已经包含的数字
        matrix = [set() for i in range(9)] # 每一个3*3矩阵已经包含的数字
        empty = {}  # 空白格字典，key是空白格的坐标(i, j, k)， value是语序填充的数字
        answer = [] # 尝试的答案, 每个元素的结构是[(i, j, k), value]，做成数组是为了方便回溯

        for i in range(len(board)):
            li = board[i]
            for j in range(len(li)):
                k = int(i / 3) * 3 + int(j / 3)
                if li[j] == '.':
                    empty[(i, j, k)] = []
                    continue

                n = int(li[j])
                line[i].add(n)
                col[j].add(n)
                matrix[k].add(n)

        # 计算empty表每个点允许的取值，并找出长度最小的，如果存在某个点允许的取值只有一个，那么直接改变board
        fullIndex = set(range(1, 10))
        while True:
            m, mPos = 10, None
            for pos in empty.keys():
                i, j, k = pos[0], pos[1], pos[2]
                empty[pos] = fullIndex.difference(line[i], col[j], matrix[k])
                if len(empty[pos]) == 1:
                    n = empty[pos].pop()
                    board[i][j] = str(n)
                    line[i].add(n)
                    col[j].add(n)
                    matrix[k].add(n)
                    # 删除empty[pos]，继续外层while循环，重新计算empty
                    del empty[pos]
                    if len(empty) == 0:
                        # 所有的空格都确定了，返回
                        return
                    m = 1
                    break
                else:
                    if len(empty[pos]) < m:
                        m = len(empty[pos])
                        mPos = pos
            if m > 1: break

        emptyBackup = {}
        # 从mPos开始尝试回溯法
        curPos = mPos
        while True:
            curValue = empty[curPos].pop()
            answer.append([curPos, curValue])
            emptyBackup[curPos] = empty[curPos]
            del empty[curPos]

            if len(empty) == 0:
                # 找到答案
                for v in answer:
                    pos = v[0]
                    board[pos[0]][pos[1]] = str(v[1])
                return

            # stepx: 更新empty，并找出新的最小长度
            m, mPos = 10, None
            for pos in empty.keys():
                if pos[0] == curPos[0] or pos[1] == curPos[1] or pos[2] == curPos[2]:
                    if curValue in empty[pos]:
                        empty[pos].remove(curValue)
                if m > 0 and len(empty[pos]) < m:
                    m = len(empty[pos])
                    mPos = pos

            if m > 0:
                # 下次从mPos继续尝试
                curPos = mPos
                continue

            # mPos位置无可填数值，尝试出错，开始回溯
            for i in range(len(answer) - 1, -1, -1):
                pos = answer[i][0]
                del answer[i]
                empty[pos] = emptyBackup[pos]
                del emptyBackup[pos]
                if len(empty[pos]) == 0: continue

                # 回溯到pos停止，下次继续从pos位置开始尝试
                curPos = pos
                # 回溯完成以后，要对empty重新计算，因为在stepx那个循环时删了元素，且不好还原
                for pos in empty:
                    # curPos不再需要重新计算，因为第一个值已经尝试失败了
                    # 少了这句会重复上次的值，导致无限循环
                    if pos == curPos: continue
                    empty[pos] = fullIndex.difference(line[pos[0]], col[pos[1]], matrix[pos[2]])
                    for v in answer:
                        posAns = v[0]
                        if pos[0] == posAns[0] or pos[1] == posAns[1] or pos[2] == posAns[2]:
                            if v[1] in empty[pos]:
                                empty[pos].remove(v[1])
                break
