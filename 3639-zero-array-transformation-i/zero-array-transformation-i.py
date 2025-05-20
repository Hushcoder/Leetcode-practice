class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff_arr = [0] * (n+1)

        for l,r in queries:
            # Start decrementing by 1
            diff_arr[l] += 1
            if r+1 < len(diff_arr):
                # Stop after decrementing till r 
                diff_arr[r+1] -= 1
        
        # prefix-sum
        curr = 0
        for i in range(n):
            curr += diff_arr[i]
            if curr < nums[i]:
               return False
        return True