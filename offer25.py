"""合并两个排序的列表"""


# 思路：一个一个进行对比，然后根据值得大小进行排序
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1.如果l1 或者l2为空则返回12， l1
        if not l1:
            return l2
        if not l2:
            return l1

        # 2.创建两个指针res, cur
        res = ListNode(-1)
        cur = res
        # 当l1和l2不同时为空，则进行循环
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        # 退出循环后，因为前面是通过两两对比，所以最后一次对比之后会有一个值还没取
        # 所以需要进行判断,如果l1不空的话，则说明最后一个值是在l1里面，所以cur.next = l1
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return res.next