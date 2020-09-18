# """输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回)"""
#
# # 有一种想法，但是不知道怎么实现
# # 将链表进行翻转，表头head
# """
# pre=None
# cur = head
# node = cur.next
# cur.next = pre
# pre = cur
# cur = node
#
# 上面的代码实现两个节点进行转换
# 然后通过while 循环进行遍历转换
#
# """
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def reversePrint(self, head):
#         resList = []
#         while head:
#             resList.append(head.val)
#             head = head.next
#         return resList[::-1]


