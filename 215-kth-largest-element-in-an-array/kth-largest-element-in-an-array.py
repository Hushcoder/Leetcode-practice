class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ## M1 -> sort (O(NlogN)) , indexed output -> kth largest => (n-k)th, distinct => kth
        nums.sort()
        n = len(nums)

        return nums[n-k]

        ## M2 -> Priority Queue (Heap) + divide and conquer

