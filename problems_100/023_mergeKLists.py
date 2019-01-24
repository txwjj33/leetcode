'''
题目：合并K个排序链表
描述：
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
把每个值对应的ListNode串起来，head，tai分别保存这个串的首位
然后把keys排序，从小到大把这些串再连到一起
这个方法最主要的是不需要创建多余的ListNode，所以很快
其实这个题目费时的不是排序，而是创建那些ListNode
能达到56ms，是所有提交里最快的
如果把那些keys按照原来的lists顺序存在一个list里面，然后使用更快的排序方式，应该能比56更小
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        head = {}
        tail = {}
        for t in lists:
            while(t):
                v = t.val
                if v in head:
                    tail[v].next = t
                    tail[v] = t
                else:
                    head[v] = t
                    tail[v] = t
                t = t.next
        keys = head.keys()
        keys.sort()
        r = ListNode(0)
        temp = r
        for k in keys:
            temp.next = head[k]
            temp = tail[k]
        return r.next

'''
每两个列表排序合并成新的列表，所有新的列表放在一起，作为新的lists，如果len(lists) > 1，则继续
相比以下的方法优化点在于，中间的计算结果都是list，不用ListNode，最后返回的时候再把list转成ListNode
112 ms
'''
class Solution(object):
    def mergeTwoListNode(self, l1, l2):
        r = []
        while(l1 or l2):
            if l1 == None:
                r.append(l2.val)
                l2 = l2.next
                continue
            if l2 == None:
                r.append(l1.val)
                l1 = l1.next
                continue
            x1 = l1.val
            x2 = l2.val
            if x1 <= x2:
                r.append(x1)
                l1 = l1.next
            else:
                r.append(x2)
                l2 = l2.next
        return r

    def mergeTwoList(self, l1, l2):
        if len(l1) == 0: return l2
        if len(l2) == 0: return l1
        r = []
        i, j = 0, 0
        while True:
            if i >= len(l1):
                return r + l2[j:]
            if j >= len(l2):
                return r + l1[i:]
            if l1[i] <= l2[j]:
                r.append(l1[i])
                i += 1
            else:
                r.append(l2[j])
                j += 1
        return r

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        first = True
        while(len(lists) > 1):
            newLists = []
            i = 0
            while(i < len(lists) - 1):
                if first:
                    l = self.mergeTwoListNode(lists[i], lists[i + 1])
                    newLists.append(l)
                else:
                    l = self.mergeTwoList(lists[i], lists[i + 1])
                    newLists.append(l)
                i += 2
            if i == len(lists) - 1:
                if first:
                    r = []
                    p = lists[-1]
                    while(p):
                        r.append(p.val)
                        p = p.next
                    newLists.append(r)
                else:
                    newLists.append(lists[-1])
            lists = newLists
            if first: first = False

        l = lists[0]
        if len(l) == 0: return None
        r = ListNode(l[0])
        temp = r
        for i in range(1, len(l)):
            temp.next = ListNode(l[i])
            temp = temp.next
        return r


'''
每两个列表排序合并成新的列表，所有新的列表放在一起，作为新的lists，如果len(lists) > 1，则继续
设m为lists的个数
时间大概是log2(m) * max(len(m))
376 ms
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None
        while(len(lists) > 1):
            newLists = []
            i = 0
            while(i < len(lists) - 1):
                a1 = lists[i]
                a2 = lists[i + 1]
                r = ListNode(0)
                temp = r
                while True:
                    if a1 == None:
                        temp.next = a2
                        break
                    if a2 == None:
                        temp.next = a1
                        break
                    x1 = a1.val
                    x2 = a2.val
                    if x1 <= x2:
                        a1 = a1.next
                        temp.next = ListNode(x1)
                    else:
                        a2 = a2.next
                        temp.next = ListNode(x2)
                    temp = temp.next

                newLists.append(r.next)
                i += 2
            if i == len(lists) - 1:
                newLists.append(lists[-1])
            lists = newLists
        return lists[0]

'''
把前两个列表排序合并成新的列表，然后把新的列表与下一个比较， 超时
设m为lists的个数
时间大概是m * len(l1) + (m- 1) * len(l2) + (m - 2) * len(l3) + ...
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None
        r = lists[0]
        for i in range(1, len(lists)):
            a1 = r
            a2 = lists[i]
            r = ListNode(0)
            temp = r
            while True:
                if a1 == None:
                    temp.next = a2
                    break
                if a2 == None:
                    temp.next = a1
                    break
                x1 = a1.val
                x2 = a2.val
                if x1 <= x2:
                    a1 = a1.next
                    temp.next = ListNode(x1)
                else:
                    a2 = a2.next
                    temp.next = ListNode(x2)
                temp = temp.next
            r = r.next
        return r
