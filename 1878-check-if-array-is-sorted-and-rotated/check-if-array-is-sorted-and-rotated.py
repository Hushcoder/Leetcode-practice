class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        window_size = 1
        for i in range(1, 2*N):
            if nums[(i-1)%N] <= nums[i%N]:
                window_size += 1 
            else:
                window_size = 1
            if window_size == N :
                return True
        return N == 1 


