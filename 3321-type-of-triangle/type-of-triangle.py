class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = nums[0]+nums[1]
        b = nums[1]+nums[2]
        c = nums[0]+nums[2]
        if nums[0] == nums[1] == nums[2] :
            return "equilateral"
        elif ((a > nums[2]) and (b > nums[0]) and (c > nums[1])) and ((a != b) and (b != c) and (a != c)):
            return "scalene"
        elif ((a > nums[2]) and (b > nums[0]) and (c > nums[1])):
            return "isosceles"
        else:
            return "none"
        
        