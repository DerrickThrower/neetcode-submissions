class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l, r = 0, len(nums)-1
    
        while l <= r:

            mid = (l+r) //2
            midVal = nums[mid]

            if midVal == target:
                return mid

            if nums[l] <= midVal:
                if nums[l] <= target < midVal:
                    r = mid - 1

                else:
                    l = mid + 1

            else:
                if midVal <= target <= nums[r]:
                    l = mid + 1   # target is in right half
                else:
                    r = mid - 1   # target is in left half


        return -1
            
            

            
