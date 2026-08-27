"""Tests for Arrays & Hashing problems."""

import os
import pytest
from conftest import load_solution

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Two Integer Sum ──────────────────────────────────────────────────────────

class TestTwoIntegerSum:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "two-integer-sum", "submission-3.py"))
        self.sol = mod.Solution()

    def test_basic(self):
        assert sorted(self.sol.twoSum([2, 7, 11, 15], 9)) == [0, 1]

    def test_negative_numbers(self):
        assert sorted(self.sol.twoSum([3, 2, 4], 6)) == [1, 2]

    def test_duplicates(self):
        assert sorted(self.sol.twoSum([3, 3], 6)) == [0, 1]

    def test_large_target(self):
        assert sorted(self.sol.twoSum([1, 5, 8, 3], 11)) == [2, 3]


# ── Duplicate Integer ────────────────────────────────────────────────────────

class TestDuplicateInteger:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "duplicate-integer", "submission-2.py"))
        self.sol = mod.Solution()

    def test_has_duplicate(self):
        assert self.sol.hasDuplicate([1, 2, 3, 1]) is True

    def test_no_duplicate(self):
        assert self.sol.hasDuplicate([1, 2, 3, 4]) is False

    def test_empty(self):
        assert self.sol.hasDuplicate([]) is False

    def test_single(self):
        assert self.sol.hasDuplicate([1]) is False

    def test_all_same(self):
        assert self.sol.hasDuplicate([5, 5, 5]) is True


# ── Anagram Groups ──────────────────────────────────────────────────────────

class TestAnagramGroups:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "anagram-groups", "submission-0.py"))
        self.sol = mod.Solution()

    def test_basic(self):
        result = self.sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        result_sorted = sorted([sorted(g) for g in result])
        assert result_sorted == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    def test_empty_strings(self):
        result = self.sol.groupAnagrams([""])
        assert result == [[""]]

    def test_single_char(self):
        result = self.sol.groupAnagrams(["a"])
        assert result == [["a"]]

    def test_no_anagrams(self):
        result = self.sol.groupAnagrams(["abc", "def", "ghi"])
        result_sorted = sorted([sorted(g) for g in result])
        assert result_sorted == [["abc"], ["def"], ["ghi"]]


# ── Top K Elements ───────────────────────────────────────────────────────────

class TestTopKElements:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "top-k-elements-in-list", "submission-0.py"),
            extra_names={"heapq": __import__("heapq")},
        )
        self.sol = mod.Solution()

    def test_basic(self):
        result = sorted(self.sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
        assert result == [1, 2]

    def test_single(self):
        assert self.sol.topKFrequent([1], 1) == [1]

    def test_all_same(self):
        assert self.sol.topKFrequent([3, 3, 3], 1) == [3]

    def test_k_equals_unique(self):
        result = sorted(self.sol.topKFrequent([1, 2], 2))
        assert result == [1, 2]


# ── Products of Array Discluding Self ────────────────────────────────────────

class TestProductsOfArray:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "products-of-array-discluding-self", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_with_zero(self):
        assert self.sol.productExceptSelf([0, 1, 2, 3]) == [6, 0, 0, 0]

    def test_two_elements(self):
        assert self.sol.productExceptSelf([2, 3]) == [3, 2]

    def test_empty(self):
        assert self.sol.productExceptSelf([]) == []

    def test_negatives(self):
        assert self.sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


# ── Valid Sudoku ─────────────────────────────────────────────────────────────

class TestValidSudoku:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(os.path.join(BASE, "valid-sudoku", "submission-1.py"))
        self.sol = mod.Solution()

    def test_valid(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        assert self.sol.isValidSudoku(board) is True

    def test_invalid_row(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "5"],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        assert self.sol.isValidSudoku(board) is False

    def test_invalid_column(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["5", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        assert self.sol.isValidSudoku(board) is False

    def test_all_empty(self):
        board = [["." for _ in range(9)] for _ in range(9)]
        assert self.sol.isValidSudoku(board) is True


# ── Longest Consecutive Sequence ─────────────────────────────────────────────

class TestLongestConsecutiveSequence:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "longest-consecutive-sequence", "submission-0.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

    def test_longer_sequence(self):
        assert self.sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    def test_empty(self):
        assert self.sol.longestConsecutive([]) == 0

    def test_single(self):
        assert self.sol.longestConsecutive([1]) == 1

    def test_no_consecutive(self):
        assert self.sol.longestConsecutive([10, 30, 50]) == 1


# ── String Encode and Decode ─────────────────────────────────────────────────

class TestStringEncodeAndDecode:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "string-encode-and-decode", "submission-1.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        strs = ["hello", "world"]
        assert self.sol.decode(self.sol.encode(strs)) == strs

    def test_empty_list(self):
        assert self.sol.decode(self.sol.encode([])) == []

    def test_empty_strings(self):
        strs = ["", ""]
        assert self.sol.decode(self.sol.encode(strs)) == strs

    def test_special_chars(self):
        strs = ["we#say", "4#hello"]
        assert self.sol.decode(self.sol.encode(strs)) == strs

    def test_single(self):
        strs = ["single"]
        assert self.sol.decode(self.sol.encode(strs)) == strs
