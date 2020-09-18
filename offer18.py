"""给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点
返回删除后的链表的头节点。"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 1.先判断特殊情况，head为None和val就是head这两种情况
        if not head:
            return head
        if head.val == val:
            head = head.next
            return head
        # 2.普通情况，设置两个指针cur和pre，分别用来指向当前节点和前一个节点
        # 先从头部开始，cur=head, pre=None
        # 如果当前节点是要删除的节点，则pre.next = cur.next, cur = cur.next
        # 如果当前节点不是要删除的节点，则pre=cur, cur = cur.next
        cur = head
        pre = None
        while cur.val != val:
            pre = cur
            cur = cur.next
        pre.next = cur.next
        cur = cur.next
        return head
