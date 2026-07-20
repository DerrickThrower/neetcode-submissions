"""Two-pointer pattern utilities.

The two-pointer pattern is duplicated across:
  - is-palindrome (2 submissions)
  - two-integer-sum-ii
  - three-integer-sum (2 submissions)
  - max-water-container
  - trapping-rain-water

Common structure:
    l, r = 0, len(arr) - 1
    while l < r:
        # process and move pointers inward
"""

from typing import List


def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome (alphanumeric only, case-insensitive).

    Extracted from is-palindrome/submission-0.py and submission-1.py.
    """
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """Two-pointer search on a sorted array. Returns 1-indexed pair.

    Extracted from two-integer-sum-ii/submission-0.py.
    """
    l, r = 0, len(numbers) - 1

    while l < r:
        curr_sum = numbers[l] + numbers[r]

        if curr_sum > target:
            r -= 1
        elif curr_sum < target:
            l += 1
        else:
            return [l + 1, r + 1]

    return []


def max_water_container(heights: List[int]) -> int:
    """Find max area between two vertical lines.

    Extracted from max-water-container/submission-0.py.
    """
    l, r = 0, len(heights) - 1
    res = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)

        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return res


def trap_rain_water(height: List[int]) -> int:
    """Calculate trapped rainwater using two-pointer approach.

    Extracted from trapping-rain-water/submission-0.py.
    """
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water
