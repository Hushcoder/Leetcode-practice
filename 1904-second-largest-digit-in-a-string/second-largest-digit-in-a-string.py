class Solution:
    def secondHighest(self, s: str) -> int:
        max_1 = -1
        max_2 = -1
        # My first Approach : 
        # for i in range(len(s)):
        #     if s[i] not in [range(10)]:
        #         pass
        #     else:
        #         if s[i] > max_1:
        #             max_2 = max_1
        #             max_1 = s[i]
        #         # print(f'{max_1} : {max_2}')
        
        # return max_2    # always return -1 say "54321" , here it never gets updated.

        # Corrected :===> let's say 5 3 4 , then check if num > max_2 if true then put max_2 = num ---> hop till reach 4.

        setv = set()
        for n in s:
            if n.isdigit():
                setv.add(int(n))
        
        for num in setv:
            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_2 = num

        return max_2

        # Method :====> 2
        # setv = set()
        # for n in s:
        #     if n.isdigit():
        #         setv.add(int(n))
        # # sorted_ls = list(sorted(setv, reverse=True)) # for descending order

        # # if len(setv) < 2:
        # #     return -1
        
        # # return sorted_ls[1]