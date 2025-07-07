class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == 0 or num2[0] == 0:
            return 0
        
        else:
            return ''.join(str(int(num1) * int(num2)))


        