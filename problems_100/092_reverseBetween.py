'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''


'''
44 ms, 6.6 MB
'''
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        back = head
        count = 0
        # pre是第m-1个node
        pre = None
        # 已翻转节点里面的开始结束节点，开始节点是上一个节点，结束节点就是第m个节点
        start, stop = None, None
        while head:
            count += 1
            if count < m - 1:
                head = head.next
            elif count == m - 1:
                pre = head
                head = head.next
            elif count == m:
                start = head
                stop = head
                head = head.next
                stop.next = None
            elif m + 1 <= count <= n:
                temp = head.next
                head.next = start
                start = head
                head = temp
            elif count == n + 1:
                stop.next = head
                head = head.next
            elif count > n + 1:
                break

        if pre:
            pre.next = start
            return back
        else:
            return start
