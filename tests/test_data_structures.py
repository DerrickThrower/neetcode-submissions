"""Tests for shared data structures."""

import sys
sys.path.insert(0, "/home/ubuntu/repos/neetcode-submissions")

from shared.data_structures import ListNode, TreeNode


def test_listnode_repr():
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert repr(head) == "1 -> 2 -> 3"


def test_listnode_equality():
    a = ListNode(1, ListNode(2, ListNode(3)))
    b = ListNode(1, ListNode(2, ListNode(3)))
    c = ListNode(1, ListNode(2))
    assert a == b
    assert a != c


def test_treenode_repr():
    node = TreeNode(5)
    assert repr(node) == "TreeNode(5)"


def test_treenode_equality():
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    c = TreeNode(1, TreeNode(2), TreeNode(4))
    assert a == b
    assert a != c
