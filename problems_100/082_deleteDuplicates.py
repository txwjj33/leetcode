'''
题目：删除排序链表中的重复元素 II
描述：
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = result
        same = False
        while head:
            n = head.next
            if n:
                if head.val == n.val:
                    same = True
                else:
                    if not same:
                        cur.next = head
                        cur = head
                    same = False
            else:
                if not same:
                    cur.next = head
                    cur = head
                else:
                    cur.next = None
            head = n
        return result.next
