class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_map = set()
        for i in range(len(nums)):
            if nums[i] not in freq_map:
                freq_map.add(nums[i])
            else:
                freq_map.remove(nums[i])
        
        return list(freq_map)[0]