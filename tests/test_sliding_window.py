"""Tests for Sliding Window problems."""

import os
import pytest
from conftest import load_solution

BASE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Data Structures & Algorithms",
)


# ── Buy and Sell Crypto ──────────────────────────────────────────────────────

class TestBuyAndSellCrypto:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "buy-and-sell-crypto", "submission-1.py")
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_no_profit(self):
        assert self.sol.maxProfit([7, 6, 4, 3, 1]) == 0

    def test_single_day(self):
        assert self.sol.maxProfit([5]) == 0

    def test_two_days_profit(self):
        assert self.sol.maxProfit([1, 2]) == 1

    def test_constant_price(self):
        assert self.sol.maxProfit([3, 3, 3]) == 0


# ── Longest Substring Without Duplicates ─────────────────────────────────────

class TestLongestSubstringWithoutDuplicates:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE, "longest-substring-without-duplicates", "submission-0.py"
            )
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.lengthOfLongestSubstring("abcabcbb") == 3

    def test_all_same(self):
        assert self.sol.lengthOfLongestSubstring("bbbbb") == 1

    def test_mixed(self):
        assert self.sol.lengthOfLongestSubstring("pwwkew") == 3

    def test_empty(self):
        assert self.sol.lengthOfLongestSubstring("") == 0

    def test_all_unique(self):
        assert self.sol.lengthOfLongestSubstring("abcdef") == 6


# ── Longest Repeating Substring With Replacement ─────────────────────────────

class TestLongestRepeatingSubstringWithReplacement:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE,
                "longest-repeating-substring-with-replacement",
                "submission-1.py",
            )
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.characterReplacement("ABAB", 2) == 4

    def test_replace_one(self):
        assert self.sol.characterReplacement("AABABBA", 1) == 4

    def test_no_replacement_needed(self):
        assert self.sol.characterReplacement("AAAA", 0) == 4

    def test_single_char(self):
        assert self.sol.characterReplacement("A", 0) == 1

    def test_empty(self):
        assert self.sol.characterReplacement("", 0) == 0


# ── Permutation String ──────────────────────────────────────────────────────

class TestPermutationString:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(BASE, "permutation-string", "submission-2.py")
        )
        self.sol = mod.Solution()

    def test_true(self):
        assert self.sol.checkInclusion("ab", "eidbaooo") is True

    def test_false(self):
        assert self.sol.checkInclusion("ab", "eidboaoo") is False

    def test_exact_match(self):
        assert self.sol.checkInclusion("abc", "bca") is True

    def test_single_char(self):
        assert self.sol.checkInclusion("a", "a") is True

    def test_longer_s1(self):
        assert self.sol.checkInclusion("abcd", "ab") is False


# ── Minimum Window With Characters ──────────────────────────────────────────

class TestMinimumWindowWithCharacters:
    @pytest.fixture(autouse=True)
    def setup(self):
        mod = load_solution(
            os.path.join(
                BASE, "minimum-window-with-characters", "submission-1.py"
            )
        )
        self.sol = mod.Solution()

    def test_basic(self):
        assert self.sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"

    def test_exact(self):
        assert self.sol.minWindow("a", "a") == "a"

    def test_no_window(self):
        assert self.sol.minWindow("a", "aa") == ""

    def test_whole_string(self):
        assert self.sol.minWindow("aa", "aa") == "aa"
