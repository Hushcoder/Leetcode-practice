class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Optimal using XOR
        # ans = start^goal
        count = 0
        # while(ans>0):
        #     ans = ans & (ans - 1)
        #     count += 1
        
        # return count

        start_bits = ''
        goal_bits = ''
        while(start > 0):
             start_bits += str(start % 2)
             start = start // 2 
        while(goal > 0):
             goal_bits += str(goal % 2)
             goal = goal // 2 
        while(len(start_bits) < len(goal_bits)):
            start_bits += '0'
        while(len(start_bits) > len(goal_bits)):
            goal_bits += '0'

        for i in range(len(start_bits)):
            if start_bits[i] != goal_bits[i]:
                count += 1
        
        return count