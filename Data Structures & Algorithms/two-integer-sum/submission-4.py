class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for x in range(len(nums)):
                val = nums[i] + nums[x]

                if val == target and i != x:
                    return [i,x]

        