import random
class Solution:
    def maxDiff(self, num: int) -> int:
        # str_num = str(num)
        # num_list = list(str_num)
        # x = str_num[0]
        # a,b = '',''
        # for j in range(2):
        #     y = str(random.randint(0,9))      
        #     for i in range(len(num_list)):
        #         num_list[i] = y          
        #     if j == 0:
        #         a = ''.join(num_list)  
        #     else:
        #         b = ''.join(num_list)  
         
        # return abs(int(a) - int(b)) 
        s = str(num)
        for c in s:
            if c != '9':
                max_num = int(s.replace(c, '9'))
                break
        else:
            max_num = num

        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for c in s[1:]:
                if c != '0' and c != '1':
                    min_num = int(s.replace(c, '0'))
                    break
            else:
                min_num = num

        return max_num - min_num

            
            

