class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans = []
        ## Extra space storing x index || or use enumerate
        index = []
        for i in range(len(nums)):
            if nums[i] == x:
                index.append(i)
        
        print(f'Index Array : {index}')

        #### count of x 
        # count_nums = sorted(Counter(nums).items())
        # print(f'Count Array : {count_nums}')

        ### Occurence Check
        for q in queries:
            if q <= len(index):
                ans.append(index[q-1])
            else:
                ans.append(-1)
        print(f'Ans Array : {ans}')
        
        return ans

            

        ### Count of x 
        ### Check count of x if <= queries[i] , then search for each occurence of x and their indexes ----> not necessary just check the len of the index array . if its <= q then add the index value from index or -1 if not present.
