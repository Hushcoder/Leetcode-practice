class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)

        if sl != tl :
            return False

        element_dict = {}
        rev_dict = {}
        
        for i in range(sl):
            if s[i] not in element_dict:
                if t[i] in rev_dict and rev_dict[t[i]] != s[i]:
                    return False
                element_dict[s[i]] = t[i]
                rev_dict[t[i]] = s[i]
            
            elif element_dict[s[i]] != t[i]:
                return False
            
            else:
                pass
        
        res = ''
        for i in range(tl):
            res += element_dict[s[i]]

        return True if res == t else False
           
                
     