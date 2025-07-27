class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # purge the iterable to a str -> int > add 1 -> append to a list -> return the list
        res = []
        purged_itr = "".join(map(str, digits))
        str_to_int = int(purged_itr)

        inc_num = str_to_int + 1

        str_inc_num = str(inc_num)

        for c in str_inc_num:
            res.append(int(c))

        return res

