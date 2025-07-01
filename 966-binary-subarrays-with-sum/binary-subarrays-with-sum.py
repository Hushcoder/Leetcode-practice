class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return SubarraysWithSum(nums, goal) - SubarraysWithSum(nums, goal - 1)
        # n = len(nums)
        # if sum(nums) == 0 and not goal:
        #     return (n*(n+1)//2)
        
        # l, r, summa, c =  0, 0, 0, 0

        # while(r < n):
        #     summa += nums[r]
            
        #     while(summa > goal):
        #         summa -= nums[l]
        #         l += 1
            
        #     c += (r-l+1)
        #     r += 1
   
def SubarraysWithSum(nums: List[int], goal: int) -> int:
        k = len(nums)
        if goal < 0 :
            return 0

        l, r, summ, count =  0, 0, 0, 0

        while(r < k):
            summ += nums[r]
            
            while(summ > goal):
                summ -= nums[l]
                l += 1
            
            count += (r-l+1)
            r += 1
        
        return count