# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# https://leetcode.com/problems/linked-list-cycle-ii/submissions/
# Using floyd's cycle detection algorithm
# https://poteblog.com/2020/04/17/post-926/
class DetectCycle:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None

        sl, fa = head, head

        while fa and fa.next:
            sl = sl.next
            fa = fa.next.next

            if sl == fa:
                while head is not sl:
                    head = head.next
                    sl = sl.next
                return sl

        return None
