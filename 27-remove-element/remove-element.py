class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        # if n <= 1 or nums[0] == val:
        #     return 0

        count,k = 0,0
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k


