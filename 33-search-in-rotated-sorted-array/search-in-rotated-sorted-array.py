class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        ## sorting it for binary-search logic but TLE.
        # nums = sorted(nums)

        # while(low <= high):
        #     mid = (low + high) // 2

        #     if nums[mid] == target:
        #         ans = mid
        #     elif nums[mid] > target:
        #         high = mid - 1
        #     else:
        #         low  = high + 1
        
        # return ans

        while(low <= high):
            mid = (low + high) // 2

            if nums[mid] == target :
               return mid
            
            # if left half sorted
            elif nums[low] <= nums[mid]:
                if (nums[low] <= target and target <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            
            # if right half sorted
            else:
                if (nums[mid] <= target and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1


        return -1

        
        