"""HashMap/frequency-counting pattern utilities.

Frequency counting and hashmap lookup patterns are duplicated across:
  - two-integer-sum (4 submissions, complement lookup)
  - anagram-groups (character frequency grouping)
  - top-k-elements-in-list (frequency counting + heap)
  - duplicate-integer (3 submissions, set-based detection)
  - valid-sudoku (multi-dimensional set tracking)
"""

from collections import defaultdict
from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Find two indices whose values sum to target using a hashmap.

    Extracted from two-integer-sum submissions 0, 1, 3 — all using:
        seen = {}
        for i, val in enumerate(nums):
            need = target - val
            if need in seen: return [seen[need], i]
            seen[val] = i
    """
    seen: Dict[int, int] = {}

    for i, val in enumerate(nums):
        need = target - val
        if need in seen:
            return [seen[need], i]
        seen[val] = i

    return []


def has_duplicate(nums: List[int]) -> bool:
    """Check for duplicate values using a set.

    Extracted from duplicate-integer submissions 0, 1, 2:
        return len(set(nums)) != len(nums)
    """
    return len(set(nums)) != len(nums)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group strings that are anagrams of each other.

    Extracted from anagram-groups/submission-0.py using character frequency tuple as key.
    """
    res: Dict[tuple, List[str]] = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    return list(res.values())


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Find the k most frequent elements.

    Extracted from top-k-elements-in-list/submission-0.py using a min-heap.
    """
    import heapq

    count: Dict[int, int] = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    heap: List[tuple] = []
    for num in count:
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [heapq.heappop(heap)[1] for _ in range(len(heap))]
