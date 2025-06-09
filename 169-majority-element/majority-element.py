import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # l = sorted(set((nums)))
        # ml = sorted(nums)
        # n = len(nums)
        # nl = len(l)
        # freq = [0] * nl
        # k = 0
        # freq[k] = 1
        # for i in range(1,n):
        #     if ml[i-1] == ml[i]:
        #         freq[k] += 1
        #     else:
        #         k += 1
        #         freq[k] = 1
        # for j in range(nl):
        #     if freq[j] > math.floor(n//2):
        #         return l[j] 

        # Boyer-Moore Voting Algorithm
        count = 0
        no = None
        for num in nums:
            if count == 0:
                no = num
            count += (1 if num == no else -1)
        return no