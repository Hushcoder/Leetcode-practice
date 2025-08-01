class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ## M1 -> sort (O(NlogN)) , indexed output
        nums.sort()
        n = len(nums)

        return nums[n-k]