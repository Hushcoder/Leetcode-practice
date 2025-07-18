class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        lb = lowbound(nums, n, target)
        up = Upbound(nums, n, target)

        if (lb == n or nums[lb] != target):
            return [-1,-1] 
        else:
            return [lb,up-1]


        ### Linear Search (Brute) ---> O(1)

        # first, last = -1, -1

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if first == -1:
        #             first = i
        #         last = i
        
        # return [first,last]


        ### Optimized (Lower & Upper Bounds ==> Binary Search ) ---> O(logN)
        


def lowbound(arr, n, k):
    low, high = 0, n - 1
    ans = n

    while(low <= high):
        mid = (low+high) // 2
         
        ## Binary Search Logic
        if arr[mid] >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def Upbound(arr, n, k):
    low, high = 0, n - 1
    ans = n

    while(low <= high):
        mid = (low+high) // 2
         
        ## Binary Search Logic
        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


        
        

        