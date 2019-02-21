'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
52 ms, 6.5 MB
'''
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left, right = ListNode(0), ListNode(0)
        leftBack, rightBack = left, right
        while head:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            temp = head.next
            head.next = None
            head = temp
        left.next = rightBack.next
        return leftBack.next
