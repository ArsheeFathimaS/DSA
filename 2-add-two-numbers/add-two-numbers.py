# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify result handling
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Loop while there are digits in either list OR carry left
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values + carry
            total = val1 + val2 + carry
            carry = total // 10  # new carry
            digit = total % 10   # digit to store in node

            # Create new node for this digit
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        