class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()

        for value in nums:
            if value in values:
                return True
            values.add(value)
        

        return False
        