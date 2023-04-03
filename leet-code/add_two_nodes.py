# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val = carry
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val + l2.val
                l2 = l2.next

            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        return dummy.next


solution = Solution()
print(solution.addTwoNumbers([ListNode(2),ListNode(4),ListNode(3)], [ListNode(2),ListNode(4),ListNode(3)]))