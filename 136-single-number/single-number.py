class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        freq = [0] * n
        l = sorted(nums)
        for i in range(1,n):
            if l[i-1] == l[i]:
                freq[i-1] = 1
                freq[i] = 1
            else:
                pass

        for i in range(n):
            if freq[i] == 0:
                return l[i] 