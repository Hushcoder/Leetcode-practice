class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        # find the j's
        n = len(nums)
        k_dis_index = []
        
        j_arr = [j for j in range(n) if nums[j] == key]

        # loop over j 
        for i in range(n):
            if any(abs(i-j) <= k for j in j_arr):
                k_dis_index.append(i)
            else:
                pass

        return k_dis_index




            