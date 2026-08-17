class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l = 0
        zC = 0
        maxN = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                zC+=1

            while zC > k:
                if nums[l] == 0:
                    zC -= 1
                l +=1

            maxN = max(maxN,r-l +1)


        return maxN
        