"""Tests for Tree problems."""

import os
import pytest
from conftest import load_solution, build_tree, tree_to_list, find_node

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Invert a Binary Tree ────────────────────────────────────────────────────

class TestInvertBinaryTree:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "invert-a-binary-tree", "submission-4.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        root = build_tree([4, 2, 7, 1, 3, 6, 9])
        result = tree_to_list(self.sol.invertTree(root))
        assert result == [4, 7, 2, 9, 6, 3, 1]

    def test_empty(self):
        assert self.sol.invertTree(None) is None

    def test_single(self):
        root = build_tree([1])
        result = tree_to_list(self.sol.invertTree(root))
        assert result == [1]

    def test_left_only(self):
        root = build_tree([1, 2])
        result = tree_to_list(self.sol.invertTree(root))
        assert result == [1, None, 2]


# ── Depth of Binary Tree ────────────────────────────────────────────────────

class TestDepthOfBinaryTree:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "depth-of-binary-tree", "submission-1.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        assert self.sol.maxDepth(root) == 3

    def test_single(self):
        root = build_tree([1])
        assert self.sol.maxDepth(root) == 1

    def test_empty(self):
        assert self.sol.maxDepth(None) == 0

    def test_left_skewed(self):
        root = build_tree([1, 2, None, 3])
        assert self.sol.maxDepth(root) == 3


# ── Same Binary Tree ────────────────────────────────────────────────────────

class TestSameBinaryTree:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "same-binary-tree", "submission-1.py")
        )
        self.sol = mod.Solution()

    def test_same(self):
        p = build_tree([1, 2, 3])
        q = build_tree([1, 2, 3])
        assert self.sol.isSameTree(p, q) is True

    def test_different_structure(self):
        p = build_tree([1, 2])
        q = build_tree([1, None, 2])
        assert self.sol.isSameTree(p, q) is False

    def test_different_values(self):
        p = build_tree([1, 2, 1])
        q = build_tree([1, 1, 2])
        assert self.sol.isSameTree(p, q) is False

    def test_both_empty(self):
        assert self.sol.isSameTree(None, None) is True

    def test_one_empty(self):
        p = build_tree([1])
        assert self.sol.isSameTree(p, None) is False


# ── Subtree of a Binary Tree ────────────────────────────────────────────────

class TestSubtreeOfBinaryTree:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "subtree-of-a-binary-tree", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_is_subtree(self):
        root = build_tree([3, 4, 5, 1, 2])
        sub = build_tree([4, 1, 2])
        assert self.sol.isSubtree(root, sub) is True

    def test_not_subtree(self):
        root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        sub = build_tree([4, 1, 2])
        assert self.sol.isSubtree(root, sub) is False

    def test_single_match(self):
        root = build_tree([1])
        sub = build_tree([1])
        assert self.sol.isSubtree(root, sub) is True

    def test_empty_subtree(self):
        root = build_tree([1])
        assert self.sol.isSubtree(root, None) is False


# ── Lowest Common Ancestor in BST ───────────────────────────────────────────

class TestLowestCommonAncestorBST:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE,
                "lowest-common-ancestor-in-binary-search-tree",
                "submission-1.py",
            )
        )
        self.sol = mod.Solution()

    def test_basic(self):
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 8)
        assert self.sol.lowestCommonAncestor(root, p, q).val == 6

    def test_ancestor_is_one_node(self):
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = find_node(root, 2)
        q = find_node(root, 4)
        assert self.sol.lowestCommonAncestor(root, p, q).val == 2

    def test_two_nodes(self):
        root = build_tree([2, 1])
        p = find_node(root, 2)
        q = find_node(root, 1)
        assert self.sol.lowestCommonAncestor(root, p, q).val == 2

    def test_both_in_right(self):
        root = build_tree([6, 2, 8, 0, 4, 7, 9])
        p = find_node(root, 7)
        q = find_node(root, 9)
        assert self.sol.lowestCommonAncestor(root, p, q).val == 8

    def test_both_in_left(self):
        root = build_tree([6, 2, 8, 0, 4, 7, 9])
        p = find_node(root, 0)
        q = find_node(root, 4)
        assert self.sol.lowestCommonAncestor(root, p, q).val == 2


# ── Level Order Traversal of Binary Tree ────────────────────────────────────

class TestLevelOrderTraversal:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE,
                "level-order-traversal-of-binary-tree",
                "submission-0.py",
            ),
            extra_names={"deque": __import__("collections").deque},
        )
        self.sol = mod.Solution()

    def test_basic(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        assert self.sol.levelOrder(root) == [[3], [9, 20], [15, 7]]

    def test_single(self):
        root = build_tree([1])
        assert self.sol.levelOrder(root) == [[1]]

    def test_empty(self):
        assert self.sol.levelOrder(None) == []

    def test_left_skewed(self):
        root = build_tree([1, 2, None, 3])
        assert self.sol.levelOrder(root) == [[1], [2], [3]]


# ── Valid Binary Search Tree ─────────────────────────────────────────────────

class TestValidBST:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "valid-binary-search-tree", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_valid(self):
        root = build_tree([2, 1, 3])
        assert self.sol.isValidBST(root) is True

    def test_invalid(self):
        root = build_tree([5, 1, 4, None, None, 3, 6])
        assert self.sol.isValidBST(root) is False

    def test_single(self):
        root = build_tree([1])
        assert self.sol.isValidBST(root) is True

    def test_equal_values(self):
        root = build_tree([2, 2, 2])
        assert self.sol.isValidBST(root) is False


# ── Kth Smallest Integer in BST ─────────────────────────────────────────────

class TestKthSmallestInBST:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE, "kth-smallest-integer-in-bst", "submission-0.py"
            )
        )
        self.sol = mod.Solution()

    def test_basic(self):
        root = build_tree([3, 1, 4, None, 2])
        assert self.sol.kthSmallest(root, 1) == 1

    def test_larger_k(self):
        root = build_tree([5, 3, 6, 2, 4, None, None, 1])
        assert self.sol.kthSmallest(root, 3) == 3

    def test_single(self):
        root = build_tree([1])
        assert self.sol.kthSmallest(root, 1) == 1

    def test_rightmost(self):
        root = build_tree([3, 1, 4, None, 2])
        assert self.sol.kthSmallest(root, 4) == 4


# ── Binary Tree Diameter ────────────────────────────────────────────────────

class TestBinaryTreeDiameter:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "binary-tree-diameter", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        root = build_tree([1, 2, 3, 4, 5])
        assert self.sol.diameterOfBinaryTree(root) == 3

    def test_single(self):
        root = build_tree([1])
        assert self.sol.diameterOfBinaryTree(root) == 0

    def test_two_nodes(self):
        root = build_tree([1, 2])
        assert self.sol.diameterOfBinaryTree(root) == 1

    def test_left_skewed(self):
        root = build_tree([1, 2, None, 3])
        assert self.sol.diameterOfBinaryTree(root) == 2
