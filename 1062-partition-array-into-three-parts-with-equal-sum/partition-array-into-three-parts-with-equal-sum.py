# class Solution:
#     def canThreePartsEqualSum(self, arr: List[int]) -> bool:
#         k = sum(arr)
#         if k % 3 != 0:
#            return False
        
#         target = k // 3
#         s, f, sums, parts_f = 0,0,0,0

#         while f < len(arr):
#             sums += arr[f]
            
#             while(sums > target):
#                 sums -= arr[s]
#                 s += 1
            
#             if sums == target :
#                 parts_f += 1
#                 sums = 0
#             f += 1

#         return True if parts_f == 3 else False
            
            
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # Calculate total sum
        k = sum(arr)
        # If sum is not divisible by 3, return False
        if k % 3 != 0:
            return False
        
        # Target sum for each part
        target = k // 3
        s, f, sums, parts_f = 0, 0, 0, 0
        n = len(arr)

        while f < n:
            sums += arr[f]
            
            # Check if current sum equals target
            if sums == target and s <= f:
                parts_f += 1
                sums = 0
                s = f + 1
            
            # Move to next element
            f += 1
            
            # If we found two parts and there are remaining elements
            if parts_f == 2 and f < n:
                remaining_sum = sum(arr[f:])
                return remaining_sum == target
        
        # Return True only if we found exactly 3 parts
        return parts_f == 3





        



        