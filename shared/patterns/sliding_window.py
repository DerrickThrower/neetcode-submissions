"""Sliding window pattern utilities.

The sliding window pattern is duplicated across:
  - longest-substring-without-duplicates
  - longest-repeating-substring-with-replacement
  - minimum-window-with-characters
  - permutation-string

Common structure:
    l = 0
    for r in range(len(s)):
        # expand window
        while invalid_condition:
            # shrink from left
            l += 1
        # update result
"""

from typing import Dict


def longest_substring_no_repeat(s: str) -> int:
    """Length of longest substring without repeating characters.

    Extracted from longest-substring-without-duplicates/submission-0.py:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    """
    char_set: set[str] = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)

    return res


def character_replacement(s: str, k: int) -> int:
    """Longest repeating substring after at most k character replacements.

    Extracted from longest-repeating-substring-with-replacement/submission-1.py.
    """
    res = 0
    char_set = set(s)

    for c in char_set:
        count = l = 0
        for r in range(len(s)):
            if s[r] == c:
                count += 1
            while (r - l + 1) - count > k:
                if s[l] == c:
                    count -= 1
                l += 1
            res = max(res, r - l + 1)

    return res


def min_window_substring(s: str, t: str) -> str:
    """Minimum window in s that contains all characters of t.

    Extracted from minimum-window-with-characters/submission-1.py.
    """
    t_map: Dict[str, int] = {}
    for c in t:
        t_map[c] = t_map.get(c, 0) + 1

    left = 0
    min_win = ""
    have, need = 0, len(t_map)
    window_map: Dict[str, int] = {}

    for right in range(len(s)):
        if s[right] in t_map:
            window_map[s[right]] = window_map.get(s[right], 0) + 1

            if window_map[s[right]] == t_map[s[right]]:
                have += 1

            while have == need:
                candidate = s[left : right + 1]
                if not min_win or len(candidate) < len(min_win):
                    min_win = candidate

                window_map[s[left]] = window_map.get(s[left], 0) - 1
                if s[left] in t_map and window_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

    return min_win


def check_inclusion(s1: str, s2: str) -> bool:
    """Check if any permutation of s1 exists as a substring of s2.

    Extracted from permutation-string/submission-2.py (optimized version).
    """
    if len(s1) > len(s2):
        return False

    s1_count: Dict[str, int] = {}
    s2_count: Dict[str, int] = {}

    for c in s1:
        s1_count[c] = s1_count.get(c, 0) + 1

    for i in range(len(s2)):
        s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

        if i >= len(s1):
            left_char = s2[i - len(s1)]
            s2_count[left_char] -= 1
            if s2_count[left_char] == 0:
                del s2_count[left_char]

        if s1_count == s2_count:
            return True

    return False
