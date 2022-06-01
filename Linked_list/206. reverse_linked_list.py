class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = head, None
        while pre:
            temp = pre.next
            pre.next = cur
            cur = pre
            pre = temp
        return cur