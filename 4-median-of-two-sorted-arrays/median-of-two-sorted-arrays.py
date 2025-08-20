class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Using built-in functions
        #1. merge
        merged_nums = nums1 + nums2
        #2. sort -> O(nlogn)
        merged_nums.sort()
        #3. finding median 
        # i. if odd elements -> middle element is the median (n/2th)
        # ii. if even elements -> n/2th & (n/2 + 1)th 

        n = len(merged_nums)
        if n % 2 != 0:
            return merged_nums[n//2]
        
        if n % 2 == 0:
           j = n - 1
           term_1 = merged_nums[j//2]
           term_2 = merged_nums[j//2 + 1]
           return (term_1 + term_2) / 2
        else:
            pass

        