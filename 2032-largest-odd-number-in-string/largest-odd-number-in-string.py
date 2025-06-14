class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Compiled 162/196 testcases ----> But TC->O(n^2) & does not work well 
        # with large strings.
        
        # if int(num)%2 != 0:
        #     return num
        # l = len(num)
        # max_sub = 0
        # num_substrings = [int(num[i:j]) for i in range(l) for j in range(i+1,l+1)]
        # for num in num_substrings:
        #     if (num%2 != 0):
        #         if num > max_sub:
        #             max_sub = num
        #     else:
        #         pass
        # return "".join([str(max_sub)]) if max_sub else ""

        "Logic --> Check for the longest sub-string from the end to start"
        for i in range(len(num)-1,-1,-1):
            if (int(num[i]) % 2 != 0):
                return num[:i+1]
        return ""
