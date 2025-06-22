class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # n = len(s)
        # rest_str = ""
        # if n % k == 0:
        #     res = [s[i:i+k] for i in range(0, n , k)]
        #     return res
        # else:
        #     next_mul = ((n + k - 1) // k) * k
        #     # for just_great in k_mul:
        #     #     if just_great > n:
        #     #         sol_mul.append(just_great)
        #     diff = next_mul - n
        #     while diff > 0:
        #         rest_str += fill
        #         diff -= 1
        #     # Or Instead if while use s += fill * diff
        #     final_str = s + rest_str
        #     res = [final_str[i:i+k] for i in range(0, len(final_str) , k)]
            
        #     return res


            # Optimized Implementation 
            n = len(s)
            diff = (k - (n%k))%k # handles the n % k == 0
            s += fill * diff

            return [s[i:i+k] for i in range(0, len(s) , k)]
            
        
