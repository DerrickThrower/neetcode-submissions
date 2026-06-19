class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, val in enumerate(nums):
            otherval = target - val

            if otherval in seen:
                #valid pair

                return [seen[otherval],i]


            seen[val] = i
        

