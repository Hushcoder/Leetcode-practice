# from collections import defaultdict
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ## counting the frequency
        d = {}

        for num in nums:
            ## increment the frequency
            count = 1
            if num not in d:
                d[num] = count 
            else:
                d[num] += count 

        ## for repeated element => traverse d
        for num, val in d.items():
            if val == (len(nums) // 2):
                return num 



            
            



