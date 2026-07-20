"""Testing utilities for building and verifying data structures.

Provides helper functions to quickly construct linked lists and binary trees
from Python lists, reducing boilerplate in local test scripts.
"""

from collections import deque
from typing import List, Optional

from shared.data_structures import ListNode, TreeNode


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a list of integers.

    Example:
        >>> build_linked_list([1, 2, 3])
        1 -> 2 -> 3
    """
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert a linked list back to a Python list.

    Example:
        >>> linked_list_to_list(build_linked_list([1, 2, 3]))
        [1, 2, 3]
    """
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def build_linked_list_with_cycle(
    values: List[int], cycle_pos: int = -1
) -> Optional[ListNode]:
    """Build a linked list with an optional cycle.

    Args:
        values: Node values.
        cycle_pos: Index where the tail connects back to (-1 for no cycle).

    Example:
        >>> build_linked_list_with_cycle([3, 2, 0, -4], 1)
        # Creates: 3 -> 2 -> 0 -> -4 -> (back to node with val 2)
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list (None = missing node).

    Example:
        >>> build_tree([1, 2, 3, None, 4])
        #       1
        #      / \\
        #     2   3
        #      \\
        #       4
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Convert a binary tree to level-order list representation.

    Example:
        >>> tree_to_list(build_tree([1, 2, 3, None, 4]))
        [1, 2, 3, None, 4]
    """
    if not root:
        return []

    result: List[Optional[int]] = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)  # type: ignore[arg-type]
            queue.append(node.right)  # type: ignore[arg-type]
        else:
            result.append(None)

    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()

    return result
