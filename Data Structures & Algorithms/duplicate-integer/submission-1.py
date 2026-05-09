class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set(nums)

        if len(checked) < len(nums):
            return True

        return False
        