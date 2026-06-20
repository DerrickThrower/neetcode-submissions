"""Binary search pattern utilities.

The binary search pattern is duplicated across:
  - binary-search (2 submissions)
  - eating-bananas
  - find-minimum-in-rotated-sorted-array (2 submissions)
  - find-target-in-rotated-sorted-array
  - search-2d-matrix

Common structure:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if condition:
            r = mid - 1
        else:
            l = mid + 1
"""

from typing import Callable, List, Optional, TypeVar

T = TypeVar("T")


def binary_search(nums: List[int], target: int) -> int:
    """Standard binary search returning index of target, or -1 if not found.

    Extracted from binary-search/submission-0.py and submission-1.py.
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid

    return -1


def binary_search_condition(
    lo: int,
    hi: int,
    condition: Callable[[int], bool],
) -> int:
    """Generic binary search on a monotonic condition.

    Finds the smallest value in [lo, hi] where condition(mid) is True.
    Extracted from eating-bananas pattern:
        l, r = lo, hi
        while l < r:
            mid = (l + r) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def search_rotated(nums: List[int], target: int) -> int:
    """Search in a rotated sorted array. Returns index or -1.

    Extracted from find-target-in-rotated-sorted-array/submission-1.py.
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


def find_min_rotated(nums: List[int]) -> int:
    """Find minimum in a rotated sorted array.

    Extracted from find-minimum-in-rotated-sorted-array (2 identical submissions).
    """
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        mid = (l + r) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return res
