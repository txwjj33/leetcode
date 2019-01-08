'''
题目：两两交换链表中的节点
描述：
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
24ms
'''
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        r = head.next

        pre, n1, n2 = None, head, head.next
        while n1 and n2:
            if pre: pre.next = n2
            n1.next = n2.next
            n2.next = n1

            n1Next = n1.next
            if n1Next == None:
                break
            pre, n1, n2 = n1, n1Next, n1Next.next
        return r