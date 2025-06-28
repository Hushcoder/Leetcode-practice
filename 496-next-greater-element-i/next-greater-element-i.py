class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        # for num in nums1:
        #     for j in range(len(nums2)):
        #         if num == nums2[j]:
        #             if j + 1 < len(nums2) and nums2[j + 1] > nums2[j]:
        #                ans.append(nums2[j+1])
        #             else:
        #                 ans.append(-1)
        #             break
        for num in nums1:
            fp = False
            next_greater = -1
            for j in range(len(nums2)):
                if num == nums2[j]:
                    fp = True
                elif fp and nums2[j] > num:
                    next_greater = nums2[j]
                    break
            ans.append(next_greater)
        
        return ans



        