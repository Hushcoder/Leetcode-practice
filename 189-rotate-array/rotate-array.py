class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k % n
        # for i in range(k):
        #     nums[i],nums[n-k+i] = nums[n-k+i],nums[i]
        
        # for i in range(k+1,n):
        #     if abs(nums[i-1]) > abs(nums[i]):
        #         nums[i-1],nums[i] = nums[i],nums[i-1]
        #     else:
        #         pass
        # Step 1: Rotate using reverse method
        n = len(nums)
        k = k % n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Rotate in-place using reversal
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)