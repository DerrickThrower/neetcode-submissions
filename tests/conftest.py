"""Shared helpers for loading NeetCode solution classes from submission files."""

import importlib.util
import sys
import types
from collections import defaultdict
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def load_solution(file_path: str, extra_names: dict | None = None):
    """Import a submission file and return its module, injecting common types."""
    spec = importlib.util.spec_from_file_location("submission", file_path)
    mod = importlib.util.module_from_spec(spec)

    # Inject builtins that NeetCode solutions expect
    mod.List = List
    mod.Optional = Optional
    mod.defaultdict = defaultdict
    mod.ListNode = ListNode
    mod.TreeNode = TreeNode

    if extra_names:
        for k, v in extra_names.items():
            setattr(mod, k, v)

    spec.loader.exec_module(mod)
    return mod


# --------------- linked-list helpers ---------------

def build_linked_list(vals):
    """Create a linked list from a list of values. Returns the head node."""
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head):
    """Convert a linked list to a Python list of values."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def build_linked_list_with_cycle(vals, cycle_index):
    """Build a linked list where the tail connects back to node at cycle_index.
    If cycle_index is -1, no cycle is created."""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index >= 0:
        nodes[-1].next = nodes[cycle_index]
    return nodes[0]


# --------------- tree helpers ---------------

def build_tree(vals):
    """Build a binary tree from a level-order list (None for missing nodes)."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    """Convert a binary tree to level-order list representation."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


def find_node(root, val):
    """Find and return the TreeNode with the given value in a BST."""
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)
