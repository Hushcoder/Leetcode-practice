class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num >= 0]
        neg = [num for num in nums if num < 0]
        res = []
        for i in range(len(nums)//2):
            res.extend([pos[i],neg[i]])
        
        return res