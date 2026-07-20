class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        msumm = 0
        summ = nums[0]

        for i in range(len(nums)):

            if i > 0:
                if nums[i] > nums[i-1]:
                    summ += nums[i]
                else:
                    msumm = max(msumm,summ)
                    summ = nums[i]
        msumm = max(msumm, summ)
        return msumm

         
        