class Solution:
    def largestNumber(self, nums: List[int]) -> str:

    # My Method ----> takes much space and also crashes for some inputs based on the remainder idea.
    #     res = ''
    #     hashmap = {}
    #     ls = list()
        
    #     for num in nums:
    #         rem = num % 10
    #         hashmap[num] = rem
    #         ls.append(rem)
        
    #     sorted_ls = sorted(set(ls),reverse = True) # [::-1]

    #     set_key = set() # tracks the used keys

    #     for rem in sorted_ls:
    #         keepers = [k for k,v in hashmap.items() if v == rem and k not in set_key]
    #         for num in sorted(keepers, reverse = True): # Descending order
    #             res += str(num)
    #             set_key.add(num)

    #     if res and res[0] == '0':
    #         return '0'
        
    #     return res


    # Optimized (or only method)

        nums = sorted(nums, key=lambda num: str(num)*10, reverse = True) # checks lexographically and sorts it in descending order

        res = ''.join([str(num) for num in nums])

        return '0' if res[0] == '0' else res

        
        
        

            