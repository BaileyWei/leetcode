# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = head
        pre = head
        while pre:
            i = 0
            head = pre
            while i < k and pre.next:
                pre = pre.next
                i += 1
            if pre.next:
                cur = pre.next
                pre.next = None
                pre = cur
                while head:
                    head.next.next = head
                    head.next = cur
                    cur = head
                    head = head.next
            else:
                pre = pre.next
        return dummy





