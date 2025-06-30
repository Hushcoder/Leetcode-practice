class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # stack = []
        # ans = []

        # for num in nums:
        #     if num not in stack :
        #         stack.append(num)
        # mono_stack = list(sorted(stack))
        
        # for num in nums:
        #     next_greater = -1
        #     for j in range(len(mono_stack)):
        #         if num < stack[j]:
        #             # next_greater = nums[j+1] # will give out of bound error
        #            next_greater = stack[j]
        #            break
        #         else:
        #            pass 
        #     ans.append(next_greater)
        
        # return ans

        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):  # loop twice for circular array
            current = nums[i % n]
            while stack and nums[stack[-1]] < current:
                idx = stack.pop()
                res[idx] = current
            if i < n:
                stack.append(i)

        return res
                 