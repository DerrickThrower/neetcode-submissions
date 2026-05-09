class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        output = []

        for i in range(len(nums)):
            prod = 1

            for j in range(len(nums)):

                if j == i:
                    continue
                else:
                    prod = prod * nums[j]

            output.append(prod)



        
        return output
        