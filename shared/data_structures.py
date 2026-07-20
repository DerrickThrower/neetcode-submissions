"""Common data structures used across NeetCode problems.

These class definitions appear (commented out) in nearly every linked list
and binary tree problem submission. Centralizing them allows local testing
and reduces boilerplate.
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    """Singly-linked list node.

    Duplicated in:
      - merge-two-sorted-linked-lists (5 submissions)
      - reverse-a-linked-list (4 submissions)
      - linked-list-cycle-detection (2 submissions)
      - remove-node-from-end-of-linked-list
      - reorder-linked-list
      - merge-k-sorted-linked-lists
    """

    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        vals = []
        node: Optional[ListNode] = self
        seen: set[int] = set()
        while node and id(node) not in seen:
            seen.add(id(node))
            vals.append(str(node.val))
            node = node.next
        if node:
            vals.append("...")
        return " -> ".join(vals)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return NotImplemented
        a: Optional[ListNode] = self
        b: Optional[ListNode] = other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None


class TreeNode:
    """Binary tree node.

    Duplicated in:
      - depth-of-binary-tree (2 submissions)
      - binary-tree-diameter
      - invert-a-binary-tree (4 submissions)
      - same-binary-tree (2 submissions)
      - subtree-of-a-binary-tree
      - valid-binary-search-tree
      - lowest-common-ancestor-in-binary-search-tree
      - kth-smallest-integer-in-bst
      - level-order-traversal-of-binary-tree
    """

    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TreeNode):
            return NotImplemented
        if self.val != other.val:
            return False
        left_eq = self.left == other.left if self.left or other.left else self.left is other.left
        right_eq = self.right == other.right if self.right or other.right else self.right is other.right
        return left_eq and right_eq
