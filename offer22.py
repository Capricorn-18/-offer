# 思想方法：两个指针，fast,low,先让fast走k步，然后fast和low同时走，
# 这样当fast到最后一个的时候，low与fast相隔k个元素，也就是到时第k+1个
# 但是当fast走到最后一个元素的时候他还需要在循环一次来判断是否还有元素
# 所以fast = fast.next为none, low=low.next退出循环，所以low指向的就是倒数第k个
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = low = head
        while fast is not None and k > 0:
            fast = fast.next
            k -= 1

        while fast is not None:
            fast = fast.next
            low = low.next
        return low
