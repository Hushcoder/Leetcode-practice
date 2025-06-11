class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        count = 0 
        for i in range(n):
            if nums[i] == 1:
                count += 1
                m = max(count, m)
            else:
                count = 0
        return m

