import re
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ## brute --> total substrings => match if have atleast one instance of "abc" => return a count
        
        # length = len(s)
        # count = 0

        # if s == "abc":
        #     return 1

        # for i in range(length):
        #     for j in range(i,length):
        #         temp = s[i:j+1]
        #         if len(temp) >= 3 and ('a' in temp and 'b' in temp and 'c' in temp):
        #             count += 1
        #         else:
        #             pass
        
        # return count


        #### Optimized => sliding window

        from collections import defaultdict
        
        count = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1
            
            # Shrink window from left until it just contains at least one of each 'a', 'b', 'c'
            while all(count[c] > 0 for c in 'abc'):
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res
