'''
题目：删除链表的倒数第N个节点
描述：
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
'''

'''
遍历的时候动态保存倒数第n和n+1个节点就好了，52 ms
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        preTarget, target = None, None
        while cur:
            count += 1
            if count == n:
                # 找到第n个节点时，开始记录target，第n+1个节点时，开始记录preTarget
                target = head
            elif count == n + 1:
                preTarget = head
                target = target.next
            elif count > n + 1:
                preTarget = preTarget.next
                target = target.next
            cur = cur.next
        if not preTarget:
            # 需删除的是头结点
            return head.next

        preTarget.next = target.next
        return head
