"""Tests for Linked List problems."""

import heapq
import os
import pytest
from conftest import (
    load_solution,
    build_linked_list,
    linked_list_to_list,
    build_linked_list_with_cycle,
    ListNode,
)

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Reverse a Linked List ───────────────────────────────────────────────────

class TestReverseLinkedList:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "reverse-a-linked-list", "submission-3.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        result = linked_list_to_list(self.sol.reverseList(head))
        assert result == [5, 4, 3, 2, 1]

    def test_two_nodes(self):
        head = build_linked_list([1, 2])
        result = linked_list_to_list(self.sol.reverseList(head))
        assert result == [2, 1]

    def test_single(self):
        head = build_linked_list([1])
        result = linked_list_to_list(self.sol.reverseList(head))
        assert result == [1]

    def test_empty(self):
        assert self.sol.reverseList(None) is None


# ── Merge Two Sorted Linked Lists ───────────────────────────────────────────

class TestMergeTwoSortedLinkedLists:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "merge-two-sorted-linked-lists", "submission-8.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        l1 = build_linked_list([1, 2, 4])
        l2 = build_linked_list([1, 3, 4])
        result = linked_list_to_list(self.sol.mergeTwoLists(l1, l2))
        assert result == [1, 1, 2, 3, 4, 4]

    def test_one_empty(self):
        l1 = build_linked_list([])
        l2 = build_linked_list([0])
        result = linked_list_to_list(self.sol.mergeTwoLists(l1, l2))
        assert result == [0]

    def test_both_empty(self):
        result = linked_list_to_list(self.sol.mergeTwoLists(None, None))
        assert result == []

    def test_different_lengths(self):
        l1 = build_linked_list([1])
        l2 = build_linked_list([2, 3, 4])
        result = linked_list_to_list(self.sol.mergeTwoLists(l1, l2))
        assert result == [1, 2, 3, 4]


# ── Linked List Cycle Detection ─────────────────────────────────────────────

class TestLinkedListCycleDetection:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "linked-list-cycle-detection", "submission-2.py")
        )
        self.sol = mod.Solution()

    def test_has_cycle(self):
        head = build_linked_list_with_cycle([3, 2, 0, -4], 1)
        assert self.sol.hasCycle(head) is True

    def test_no_cycle(self):
        head = build_linked_list([1, 2, 3])
        assert self.sol.hasCycle(head) is False

    def test_single_no_cycle(self):
        head = build_linked_list([1])
        assert self.sol.hasCycle(head) is False

    def test_empty(self):
        assert self.sol.hasCycle(None) is False

    def test_cycle_at_head(self):
        head = build_linked_list_with_cycle([1, 2], 0)
        assert self.sol.hasCycle(head) is True


# ── Reorder Linked List ─────────────────────────────────────────────────────

class TestReorderLinkedList:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "reorder-linked-list", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_even(self):
        head = build_linked_list([1, 2, 3, 4])
        self.sol.reorderList(head)
        assert linked_list_to_list(head) == [1, 4, 2, 3]

    def test_odd(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        self.sol.reorderList(head)
        assert linked_list_to_list(head) == [1, 5, 2, 4, 3]

    def test_two_nodes(self):
        head = build_linked_list([1, 2])
        self.sol.reorderList(head)
        assert linked_list_to_list(head) == [1, 2]


# ── Remove Node From End of Linked List ──────────────────────────────────────

class TestRemoveNodeFromEnd:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE, "remove-node-from-end-of-linked-list", "submission-0.py"
            )
        )
        self.sol = mod.Solution()

    def test_basic(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        result = linked_list_to_list(self.sol.removeNthFromEnd(head, 2))
        assert result == [1, 2, 3, 5]

    def test_remove_head(self):
        head = build_linked_list([1])
        result = linked_list_to_list(self.sol.removeNthFromEnd(head, 1))
        assert result == []

    def test_remove_first(self):
        head = build_linked_list([1, 2])
        result = linked_list_to_list(self.sol.removeNthFromEnd(head, 2))
        assert result == [2]

    def test_remove_last(self):
        head = build_linked_list([1, 2])
        result = linked_list_to_list(self.sol.removeNthFromEnd(head, 1))
        assert result == [1]


# ── Merge K Sorted Linked Lists ─────────────────────────────────────────────

class TestMergeKSortedLinkedLists:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "merge-k-sorted-linked-lists", "submission-0.py"),
            extra_names={"heapq": heapq},
        )
        self.sol = mod.Solution()

    def test_basic(self):
        lists = [
            build_linked_list([1, 4, 5]),
            build_linked_list([1, 3, 4]),
            build_linked_list([2, 6]),
        ]
        result = linked_list_to_list(self.sol.mergeKLists(lists))
        assert result == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_empty_lists(self):
        assert self.sol.mergeKLists([]) is None

    def test_single_list(self):
        lists = [build_linked_list([1, 2, 3])]
        result = linked_list_to_list(self.sol.mergeKLists(lists))
        assert result == [1, 2, 3]

    def test_all_none(self):
        result = self.sol.mergeKLists([None, None])
        assert result is None

    def test_mixed_none(self):
        lists = [None, build_linked_list([1])]
        result = linked_list_to_list(self.sol.mergeKLists(lists))
        assert result == [1]
