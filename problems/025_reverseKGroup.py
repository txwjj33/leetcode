'''
题目：k个一组翻转链表
描述：
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
48 ms, 如果不限制空间，把每k个node存起来，会比较好实现，并且快一些
'''
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        if k == 1: return head

        r = head
        nodeAtK = None
        tail = None
        while head:
            count = 0
            # 计算head后面是否还有至少k个节点
            temp = head
            while temp:
                count += 1
                if count == k:
                    if not nodeAtK:
                        nodeAtK = temp
                    break
                temp = temp.next
            if count < k: break

            count = 1
            pre, n1, n2 = head, head.next, head.next.next
            # 依次把后面的node放到前面去
            while count < k:
                n1.next = pre
                pre, n1 = n1, n2
                if n2: n2 = n2.next
                count += 1

            # 以交换之前的位置做标准， 循环结束以后pre指向这k个node里面最后一个
            # n1 = pre.next，n2 = n1或n1.next
            # 把tail和pre连起来，head和n1连起来
            if tail: tail.next = pre
            head.next = n1
            tail = head
            head = n1

        return nodeAtK if nodeAtK else r
