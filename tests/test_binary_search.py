"""Tests for Binary Search problems."""

import math
import os
import pytest
from conftest import load_solution

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Binary Search ────────────────────────────────────────────────────────────

class TestBinarySearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "binary-search", "submission-1.py"))
        self.sol = mod.Solution()

    def test_found(self):
        assert self.sol.search([-1, 0, 3, 5, 9, 12], 9) == 4

    def test_not_found(self):
        assert self.sol.search([-1, 0, 3, 5, 9, 12], 2) == -1

    def test_single_found(self):
        assert self.sol.search([5], 5) == 0

    def test_single_not_found(self):
        assert self.sol.search([5], -5) == -1

    def test_first_element(self):
        assert self.sol.search([1, 2, 3], 1) == 0

    def test_last_element(self):
        assert self.sol.search([1, 2, 3], 3) == 2


# ── Search 2D Matrix ────────────────────────────────────────────────────────

class TestSearch2DMatrix:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "search-2d-matrix", "submission-1.py")
        )
        self.sol = mod.Solution()

    def test_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        assert self.sol.searchMatrix(matrix, 3) is True

    def test_not_found(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        assert self.sol.searchMatrix(matrix, 13) is False

    def test_single_element_found(self):
        assert self.sol.searchMatrix([[1]], 1) is True

    def test_single_element_not_found(self):
        assert self.sol.searchMatrix([[1]], 0) is False

    def test_single_row(self):
        assert self.sol.searchMatrix([[1, 3, 5]], 3) is True


# ── Eating Bananas (Koko) ───────────────────────────────────────────────────

class TestEatingBananas:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "eating-bananas", "submission-1.py"),
            extra_names={"math": math},
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.minEatingSpeed([3, 6, 7, 11], 8) == 4

    def test_tight(self):
        assert self.sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30

    def test_generous_time(self):
        assert self.sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

    def test_single_pile(self):
        assert self.sol.minEatingSpeed([10], 10) == 1


# ── Find Minimum in Rotated Sorted Array ────────────────────────────────────

class TestFindMinimumInRotatedSortedArray:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE,
                "find-minimum-in-rotated-sorted-array",
                "submission-1.py",
            )
        )
        self.sol = mod.Solution()

    def test_rotated(self):
        assert self.sol.findMin([3, 4, 5, 1, 2]) == 1

    def test_more_rotation(self):
        assert self.sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0

    def test_not_rotated(self):
        assert self.sol.findMin([1, 2, 3, 4, 5]) == 1

    def test_single(self):
        assert self.sol.findMin([1]) == 1

    def test_two_elements(self):
        assert self.sol.findMin([2, 1]) == 1

    def test_rotation_in_right_half(self):
        assert self.sol.findMin([2, 3, 4, 5, 1]) == 1


# ── Find Target in Rotated Sorted Array ─────────────────────────────────────

class TestFindTargetInRotatedSortedArray:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE,
                "find-target-in-rotated-sorted-array",
                "submission-1.py",
            )
        )
        self.sol = mod.Solution()

    def test_found(self):
        assert self.sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_not_found(self):
        assert self.sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_single_found(self):
        assert self.sol.search([1], 1) == 0

    def test_single_not_found(self):
        assert self.sol.search([1], 0) == -1

    def test_not_rotated(self):
        assert self.sol.search([1, 2, 3, 4, 5], 3) == 2

    def test_target_at_pivot(self):
        assert self.sol.search([4, 5, 6, 7, 0, 1, 2], 4) == 0

    def test_target_in_right_sorted(self):
        assert self.sol.search([4, 5, 6, 7, 0, 1, 2], 1) == 5

    def test_target_in_left_sorted(self):
        assert self.sol.search([6, 7, 0, 1, 2, 3, 4, 5], 7) == 1
