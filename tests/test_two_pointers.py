"""Tests for Two Pointers problems."""

import os
import pytest
from conftest import load_solution

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Is Palindrome ────────────────────────────────────────────────────────────

class TestIsPalindrome:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "is-palindrome", "submission-1.py"))
        self.sol = mod.Solution()

    def test_valid_palindrome(self):
        assert self.sol.isPalindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self):
        assert self.sol.isPalindrome("race a car") is False

    def test_single_char(self):
        assert self.sol.isPalindrome("a") is True

    def test_only_non_alphanumeric(self):
        assert self.sol.isPalindrome(" ") is True

    def test_numeric_palindrome(self):
        assert self.sol.isPalindrome("121") is True

    def test_mixed_case(self):
        assert self.sol.isPalindrome("Aa") is True


# ── Two Integer Sum II (sorted) ─────────────────────────────────────────────

class TestTwoIntegerSumII:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "two-integer-sum-ii", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.twoSum([2, 7, 11, 15], 9) == [1, 2]

    def test_negative(self):
        assert self.sol.twoSum([-1, 0], -1) == [1, 2]

    def test_larger(self):
        assert self.sol.twoSum([2, 3, 4], 6) == [1, 3]

    def test_two_elements(self):
        assert self.sol.twoSum([1, 2], 3) == [1, 2]

    def test_target_not_found(self):
        assert self.sol.twoSum([1, 2, 3], 10) == []

    def test_need_to_move_left(self):
        assert self.sol.twoSum([1, 3, 5, 7], 8) == [1, 4]


# ── Three Integer Sum ────────────────────────────────────────────────────────

class TestThreeIntegerSum:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "three-integer-sum", "submission-1.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        result = self.sol.threeSum([-1, 0, 1, 2, -1, -4])
        result_sorted = sorted([sorted(t) for t in result])
        assert result_sorted == [[-1, -1, 2], [-1, 0, 1]]

    def test_no_triplets(self):
        assert self.sol.threeSum([0, 1, 1]) == []

    def test_all_zeros(self):
        result = self.sol.threeSum([0, 0, 0])
        assert result == [[0, 0, 0]]

    def test_empty(self):
        assert self.sol.threeSum([]) == []

    def test_multiple_results(self):
        result = self.sol.threeSum([-2, -1, 0, 1, 2])
        result_sorted = sorted([sorted(t) for t in result])
        assert result_sorted == [[-2, 0, 2], [-1, 0, 1]]


# ── Max Water Container ─────────────────────────────────────────────────────

class TestMaxWaterContainer:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "max-water-container", "submission-0.py"))
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_equal_heights(self):
        assert self.sol.maxArea([1, 1]) == 1

    def test_decreasing(self):
        assert self.sol.maxArea([4, 3, 2, 1, 4]) == 16

    def test_increasing(self):
        assert self.sol.maxArea([1, 2, 3, 4, 5]) == 6


# ── Trapping Rain Water ─────────────────────────────────────────────────────

class TestTrappingRainWater:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "trapping-rain-water", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

    def test_v_shape(self):
        assert self.sol.trap([4, 2, 0, 3, 2, 5]) == 9

    def test_flat(self):
        assert self.sol.trap([1, 1, 1, 1]) == 0

    def test_empty(self):
        assert self.sol.trap([]) == 0

    def test_single(self):
        assert self.sol.trap([5]) == 0

    def test_no_trap(self):
        assert self.sol.trap([1, 2, 3, 4, 5]) == 0
