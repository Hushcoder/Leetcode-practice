class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # if (a == "0" and b == "1") or (a == "1" and b == "0"): 
        #     return "1"
        # if (a == "0" and b == "0"):
        #     return "0"
        
        # res = ""
        # carry = 0
        

        ##### Cheated

        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]
        
              
