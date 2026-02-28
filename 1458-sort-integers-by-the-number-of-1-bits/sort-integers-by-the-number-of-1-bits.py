from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        ## hashmap to maintain bit_sum and poss. vlaue lists
        final_dict = defaultdict(list)
        final_sort = []
        
        ## for computing bit-sum
        for num in arr:
            bit_sum = 0
            k = num

            while k > 0:
                rem = k % 2 
                bit_sum += rem 
                k = k // 2

            # dict update
            final_dict[bit_sum].append(num)
        
        ## python handles generator functions and normal functions differently
        for bsum in sorted(final_dict.keys()):
            final_sort.extend(sorted(final_dict[bsum]))


        return final_sort
            
            
            

            
