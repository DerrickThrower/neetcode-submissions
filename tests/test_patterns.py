"""Tests for shared algorithmic patterns."""

import sys
sys.path.insert(0, "/home/ubuntu/repos/neetcode-submissions")

from shared.patterns.binary_search import (
    binary_search,
    binary_search_condition,
    find_min_rotated,
    search_rotated,
)
from shared.patterns.two_pointer import (
    is_palindrome,
    max_water_container,
    trap_rain_water,
    two_sum_sorted,
)
from shared.patterns.linked_list import (
    has_cycle,
    merge_two_sorted,
    remove_nth_from_end,
    reverse_list,
)
from shared.patterns.sliding_window import (
    character_replacement,
    check_inclusion,
    longest_substring_no_repeat,
    min_window_substring,
)
from shared.patterns.tree_traversal import (
    diameter,
    inorder_traversal,
    invert_tree,
    is_same_tree,
    is_valid_bst,
    level_order,
    max_depth_bfs,
    max_depth_dfs,
)
from shared.patterns.stack import (
    daily_temperatures,
    eval_rpn,
    is_valid_parentheses,
)
from shared.patterns.hashmap import (
    group_anagrams,
    has_duplicate,
    top_k_frequent,
    two_sum,
)
from shared.testing import (
    build_linked_list,
    build_linked_list_with_cycle,
    build_tree,
    linked_list_to_list,
    tree_to_list,
)


# --- Binary Search ---

def test_binary_search_found():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2


def test_binary_search_not_found():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1


def test_binary_search_condition():
    # Find smallest x in [1, 10] where x*x >= 16 → answer is 4
    result = binary_search_condition(1, 10, lambda x: x * x >= 16)
    assert result == 4


def test_search_rotated():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_find_min_rotated():
    assert find_min_rotated([3, 4, 5, 1, 2]) == 1
    assert find_min_rotated([1, 2, 3, 4, 5]) == 1


# --- Two Pointer ---

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False


def test_two_sum_sorted():
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]


def test_max_water_container():
    assert max_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_trap_rain_water():
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


# --- Linked List ---

def test_reverse_list():
    head = build_linked_list([1, 2, 3, 4, 5])
    result = reverse_list(head)
    assert linked_list_to_list(result) == [5, 4, 3, 2, 1]


def test_merge_two_sorted():
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    result = merge_two_sorted(l1, l2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]


def test_has_cycle():
    head = build_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert has_cycle(head) is True

    head = build_linked_list([1, 2, 3])
    assert has_cycle(head) is False


def test_remove_nth_from_end():
    head = build_linked_list([1, 2, 3, 4, 5])
    result = remove_nth_from_end(head, 2)
    assert linked_list_to_list(result) == [1, 2, 3, 5]


# --- Sliding Window ---

def test_longest_substring_no_repeat():
    assert longest_substring_no_repeat("abcabcbb") == 3
    assert longest_substring_no_repeat("bbbbb") == 1


def test_character_replacement():
    assert character_replacement("AABABBA", 1) == 4


def test_min_window_substring():
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"


def test_check_inclusion():
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False


# --- Tree Traversal ---

def test_max_depth():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert max_depth_bfs(root) == 3
    assert max_depth_dfs(root) == 3


def test_diameter():
    root = build_tree([1, 2, 3, 4, 5])
    assert diameter(root) == 3


def test_invert_tree():
    root = build_tree([4, 2, 7, 1, 3, 6, 9])
    inverted = invert_tree(root)
    assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]


def test_is_same_tree():
    a = build_tree([1, 2, 3])
    b = build_tree([1, 2, 3])
    c = build_tree([1, 2, 4])
    assert is_same_tree(a, b) is True
    assert is_same_tree(a, c) is False


def test_is_valid_bst():
    valid = build_tree([2, 1, 3])
    invalid = build_tree([5, 1, 4, None, None, 3, 6])
    assert is_valid_bst(valid) is True
    assert is_valid_bst(invalid) is False


def test_level_order():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_inorder_traversal():
    root = build_tree([3, 1, 4, None, 2])
    assert inorder_traversal(root) == [1, 2, 3, 4]


# --- Stack ---

def test_is_valid_parentheses():
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([)]") is False


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1, 1, 4, 2, 1, 1, 0, 0
    ]


def test_eval_rpn():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6


# --- HashMap ---

def test_two_sum():
    result = two_sum([2, 7, 11, 15], 9)
    assert result == [0, 1]


def test_has_duplicate():
    assert has_duplicate([1, 2, 3, 1]) is True
    assert has_duplicate([1, 2, 3, 4]) is False


def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort inner lists and outer list for comparison
    result_sorted = sorted([sorted(g) for g in result])
    expected = sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
    assert result_sorted == expected


def test_top_k_frequent():
    result = sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    assert result == [1, 2]
