"""定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点"""
# 思想：用三个指针来翻转两个相邻的节点
# pre, cur, nextnode: 分别表示前一个，当前， 下一个
# nextnode = cur.next, pre = cur, cur = nextnode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode):
        pre = None
        cur = head
        if not head :
            return head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        # 因为退出循环的时候cur指向none，pre指向最后一个，所以返回的是pre
        return pre