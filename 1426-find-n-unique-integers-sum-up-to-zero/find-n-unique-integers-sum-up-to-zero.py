class Solution:
    #import random
    def sumZero(self, n: int) -> List[int]:
        num_arr = []
        # even then alternate pairs -> [1,-1, 2,-2 .....]
        # if odd then same just add 0

        if n % 2 == 1 : # or != 0 
           num_arr.append(0)
           n -= 1

        for i in range(1, n//2 + 1):
            num_arr.extend([-i,i])

        return num_arr
        
        # while True:
        #     # randn has range -inf to inf
        #     k = random.randn()
        #     # check if its smaller than n
        #     if k < n:
        #         num_arr.append(k)
        #         if (sum(num_arr) == 0 and len(num_arr) == n):
        #             break
        #         else:
        #             continue
        
        # return num_arr
        



               
                  



        
        
