"""Tests for Stack problems."""

import os
import pytest
from conftest import load_solution

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Validate Parentheses ────────────────────────────────────────────────────

class TestValidateParentheses:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "validate-parentheses", "submission-21.py")
        )
        self.sol = mod.Solution()

    def test_valid_simple(self):
        assert self.sol.isValid("()") is True

    def test_valid_multiple(self):
        assert self.sol.isValid("()[]{}") is True

    def test_invalid_mismatch(self):
        assert self.sol.isValid("(]") is False

    def test_nested(self):
        assert self.sol.isValid("([{}])") is True

    def test_empty(self):
        assert self.sol.isValid("") is True

    def test_single_open(self):
        assert self.sol.isValid("(") is False

    def test_single_close(self):
        assert self.sol.isValid(")") is False

    def test_wrong_order(self):
        assert self.sol.isValid(")(") is False


# ── Minimum Stack ────────────────────────────────────────────────────────────

class TestMinimumStack:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "minimum-stack", "submission-1.py"))
        self.MinStack = mod.MinStack

    def test_basic_operations(self):
        ms = self.MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        assert ms.getMin() == -3
        ms.pop()
        assert ms.top() == 0
        assert ms.getMin() == -2

    def test_single_element(self):
        ms = self.MinStack()
        ms.push(5)
        assert ms.top() == 5
        assert ms.getMin() == 5

    def test_push_pop_sequence(self):
        ms = self.MinStack()
        ms.push(1)
        ms.push(2)
        ms.push(3)
        ms.pop()
        assert ms.top() == 2
        ms.pop()
        assert ms.top() == 1

    def test_ascending_min(self):
        ms = self.MinStack()
        ms.push(3)
        ms.push(2)
        ms.push(1)
        assert ms.getMin() == 1
        ms.pop()
        assert ms.getMin() == 2


# ── Evaluate Reverse Polish Notation ────────────────────────────────────────

class TestEvalRPN:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE,
                "evaluate-reverse-polish-notation",
                "submission-6.py",
            )
        )
        self.sol = mod.Solution()

    def test_addition(self):
        assert self.sol.evalRPN(["2", "1", "+"]) == 3

    def test_basic(self):
        assert self.sol.evalRPN(["2", "1", "+", "3", "*"]) == 9

    def test_complex(self):
        assert self.sol.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        ) == 22

    def test_single_number(self):
        assert self.sol.evalRPN(["42"]) == 42

    def test_subtraction(self):
        assert self.sol.evalRPN(["4", "13", "5", "/", "+"]) == 6

    def test_subtraction_op(self):
        assert self.sol.evalRPN(["5", "3", "-"]) == 2


# ── Daily Temperatures ──────────────────────────────────────────────────────

class TestDailyTemperatures:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "daily-temperatures", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
            1, 1, 4, 2, 1, 1, 0, 0,
        ]

    def test_decreasing(self):
        assert self.sol.dailyTemperatures([30, 20, 10]) == [0, 0, 0]

    def test_increasing(self):
        assert self.sol.dailyTemperatures([10, 20, 30]) == [1, 1, 0]

    def test_constant(self):
        assert self.sol.dailyTemperatures([50, 50, 50]) == [0, 0, 0]

    def test_single(self):
        assert self.sol.dailyTemperatures([100]) == [0]


# ── Car Fleet ────────────────────────────────────────────────────────────────

class TestCarFleet:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "car-fleet", "submission-0.py"))
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3

    def test_single_car(self):
        assert self.sol.carFleet(10, [3], [3]) == 1

    def test_no_cars(self):
        assert self.sol.carFleet(100, [], []) == 0

    def test_all_same_speed(self):
        assert self.sol.carFleet(10, [0, 2, 4], [2, 2, 2]) == 3

    def test_all_catch_up(self):
        assert self.sol.carFleet(10, [6, 8], [3, 2]) == 2
