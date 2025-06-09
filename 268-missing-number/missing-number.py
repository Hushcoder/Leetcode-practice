class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)+1):
            if i not in nums:
                a = i
            else:
                pass
        return a
