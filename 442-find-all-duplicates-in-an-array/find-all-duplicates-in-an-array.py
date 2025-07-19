class Solution:
    from collections import Counter
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        count_dict = list(Counter(nums).items())

        for num, i in count_dict:
            if i == 2:
                res.append(num)

        return res
        
