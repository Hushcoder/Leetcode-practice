class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # l, r, ls = 0, n - 1, []
        
        # if n == 0:
        #     return [-1,-1]

        # while(l <= r):
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         if mid not in ls:
        #             ls.append(mid)
        #             l += 1
        #         elif nums[l] == target:
        #             ls.append(l)
        #             l += 1
        #         elif nums[r] == target:
        #             ls.append(r)
        #             r -= 1
        #     elif nums[mid] < target :
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        
        # m = len(ls)
        
        # # check for no target in nums
        # if m == 0 :
        #     return [-1,-1]
        # else:
        #     return [min(ls),max(ls)]

        
        ### Linear Search (Brute)

        first, last = -1, -1

        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        
        return [first,last]
        