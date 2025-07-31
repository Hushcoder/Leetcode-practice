class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        ### track of 5's and 10's

        five = ten = 0

        for i in range(len(bills)):

            if bills[i] == 5 : five += 1

            elif bills[i] == 10:
                if five :
                    ten += 1
                    five -= 1
                
                else :
                    return False
            else:
                ## 20 -> 10 + 5 or 5 + 5 + 5
                
                if five and ten:
                    five -= 1 
                    ten -= 1
                
                elif five >= 3:
                    five -= 3
                
                else:
                    return False
        
        return True
            
                 


                    
                

