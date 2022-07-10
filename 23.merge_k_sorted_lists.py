# 分治法合并链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists):
        def merge(left, right):
            if left > right:
                return
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            l = merge(left, mid)
            r = merge(mid+1, right)
            return merge_two(l, r)

        def merge_two(l1, l2):
            if not l1: return l2
            if not l2: return l1
            head = None
            if l1.val < l2.val:
                head = l1
                head.next = merge_two(l1.next, l2)
            else:
                head = l2
                head.next = merge_two(l1, l2.next)
            return head

        if not lists:
            return None
        return merge(0, len(lists)-1)
