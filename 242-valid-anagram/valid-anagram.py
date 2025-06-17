class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        n = len(s)
        k = len(t)
        if n != k:
            return False
        # count = 0
        # for i in range(n):
        #     if t[i] in s:
        #         count += 1
        # if count == n:
        #     return True
        # else:
        #     return False

        sl = sorted(set(s)) 
        s_fmap = defaultdict(int)
        t_fmap = defaultdict(int)
        for i in range(n):
            s_fmap[s[i]] += 1
            t_fmap[t[i]] += 1
        for i in range(len(sl)):
            if s_fmap[sl[i]] == t_fmap[sl[i]]:
                pass
            else:
                return False
        return True


        