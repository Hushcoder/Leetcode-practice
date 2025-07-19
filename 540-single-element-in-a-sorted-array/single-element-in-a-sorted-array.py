class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for num in nums:
            lb = self.lowBound(nums, n, num)
            up = self.UpBound(nums, n, num)
            
            # Count check
            if (up - lb) == 1:
                return num


    def lowBound(self, nums: List[int], n: int, target: int) -> int:
        low, high = 0, n - 1
        ans = n

        while(low <= high):
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans 

    def UpBound(self, nums: List[int], n: int, target: int) -> int:
        low, high = 0, n - 1
        ans = n

        while(low <= high):
            mid = (low + high) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans