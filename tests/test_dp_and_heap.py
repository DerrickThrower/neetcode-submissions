"""Tests for Dynamic Programming and Heap problems."""

import heapq
import os
import pytest
from conftest import load_solution

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Climbing Stairs ──────────────────────────────────────────────────────────

class TestClimbingStairs:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "climbing-stairs", "submission-3.py")
        )
        self.sol = mod.Solution()

    def test_one_step(self):
        assert self.sol.climbStairs(1) == 1

    def test_two_steps(self):
        assert self.sol.climbStairs(2) == 2

    def test_three_steps(self):
        assert self.sol.climbStairs(3) == 3

    def test_five_steps(self):
        assert self.sol.climbStairs(5) == 8

    def test_ten_steps(self):
        assert self.sol.climbStairs(10) == 89


# ── Find Median in a Data Stream ────────────────────────────────────────────

class TestFindMedianInDataStream:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "find-median-in-a-data-stream", "submission-1.py"),
            extra_names={"heapq": heapq},
        )
        self.MedianFinder = mod.MedianFinder

    def test_basic(self):
        mf = self.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        assert mf.findMedian() == 1.5
        mf.addNum(3)
        assert mf.findMedian() == 2

    def test_single(self):
        mf = self.MedianFinder()
        mf.addNum(5)
        assert mf.findMedian() == 5

    def test_even_count(self):
        mf = self.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        mf.addNum(3)
        mf.addNum(4)
        assert mf.findMedian() == 2.5

    def test_descending_order(self):
        mf = self.MedianFinder()
        mf.addNum(5)
        mf.addNum(4)
        mf.addNum(3)
        mf.addNum(2)
        mf.addNum(1)
        assert mf.findMedian() == 3

    def test_duplicates(self):
        mf = self.MedianFinder()
        mf.addNum(1)
        mf.addNum(1)
        mf.addNum(1)
        assert mf.findMedian() == 1

    def test_negative(self):
        mf = self.MedianFinder()
        mf.addNum(-1)
        mf.addNum(-2)
        assert mf.findMedian() == -1.5
