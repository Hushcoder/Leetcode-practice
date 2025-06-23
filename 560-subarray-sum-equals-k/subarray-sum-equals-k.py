class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     for j in range(i+1,n+1):
        #         sub_arr = nums[i:j]
        #         if sum(sub_arr) == k:
        #             count += 1
        # return count
       
        # Using Hashmap/freqmap and prefix_sum
        count = 0 
        prefix_sum = 0
        freqmap = {0:1}
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in freqmap:
                count += freqmap.get(prefix_sum-k,0)
            freqmap[prefix_sum] = freqmap.get(prefix_sum,0) + 1

        return count
        