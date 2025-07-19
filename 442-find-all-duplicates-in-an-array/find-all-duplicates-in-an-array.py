class Solution:
    from collections import Counter
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
         
        ##### Using Counter but space and time constraints exceeded
        count_dict = list(Counter(nums).items())

        for num, i in count_dict:
            if i == 2:
                res.append(num)

        return res
        
