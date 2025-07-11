class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        
        return countfunc(nums,k) - countfunc(nums,k-1) 
        
def countfunc(nums,k):
    if k < 0: return 0
        
    l,r = 0, 0 
    pre_sum = 0
    count = 0
        
    while(r < len(nums)):
        pre_sum += (nums[r] % 2)

        while(pre_sum > k):
            pre_sum -= (nums[l] % 2)
            l += 1
            
        count += (r-l+1)
        r += 1

    return count


