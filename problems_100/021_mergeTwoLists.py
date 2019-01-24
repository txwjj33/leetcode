'''
题目：合并两个有序链表
描述：
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
56 ms
'''
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        r = ListNode(0)
        head = r
        while l1 or l2:
            if not l1:
                r.next = l2
                break
            if not l2:
                r.next = l1
                break

            if l1.val <= l2.val:
                r.next = l1
                r = l1
                l1 = l1.next
            else:
                r.next = l2
                r = l2
                l2 = l2.next
        return head.next
