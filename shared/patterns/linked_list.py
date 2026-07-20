"""Linked list pattern utilities.

Common linked list operations duplicated across:
  - reverse-a-linked-list (4 submissions with identical reversal logic)
  - merge-two-sorted-linked-lists (5 submissions with identical merge logic)
  - reorder-linked-list (uses reverse + merge)
  - linked-list-cycle-detection (2 submissions, Floyd's algorithm)
  - remove-node-from-end-of-linked-list (two-pointer gap technique)
"""

from typing import Optional

from shared.data_structures import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly-linked list in-place.

    Extracted from reverse-a-linked-list submissions 0-3, all using:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    """
    prev: Optional[ListNode] = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def merge_two_sorted(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """Merge two sorted linked lists into one sorted list.

    Extracted from merge-two-sorted-linked-lists submissions 0, 1, 6, 7, 8.
    All use the dummy-node pattern:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val: curr.next = l1; l1 = l1.next
            else: curr.next = l2; l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
    """
    dummy = ListNode()
    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return dummy.next


def has_cycle(head: Optional[ListNode]) -> bool:
    """Detect cycle using Floyd's tortoise-and-hare algorithm.

    Extracted from linked-list-cycle-detection submissions 1-2:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: return True
        return False
    """
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next
        if fast is slow:
            return True

    return False


def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """Find the middle node using slow/fast pointers.

    Used in reorder-linked-list to split the list in half.
    """
    slow = head
    fast = head.next if head else None

    while fast and fast.next:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next

    return slow


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the nth node from end using two-pointer gap technique.

    Extracted from remove-node-from-end-of-linked-list/submission-0.py.
    """
    dummy = ListNode(0, head)
    left: Optional[ListNode] = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next  # type: ignore[union-attr]
        right = right.next

    left.next = left.next.next  # type: ignore[union-attr]
    return dummy.next
