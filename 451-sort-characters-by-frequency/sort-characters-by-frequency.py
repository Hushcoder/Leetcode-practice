class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)
        sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        return ''.join(char * count for char, count in sorted_items)





        # from collections import defaultdict

        # res = ''

        # fmap = defaultdict(int)
        # n = len(s)
        # for i in range(n):
        #     if s[i] not in fmap:
        #         fmap[s[i]] += 1
        #     elif s[i].isupper() and (s[i].lower() in fmap):
        #         fmap[s[i]] -= 1
        #     elif s[i].islower() and (s[i].upper() in fmap):
        #         fmap[s[i]] -= 1
        #     else:
        #         fmap[s[i]] += 1

        
        # for char, freq in sorted(fmap.items(), key=lambda x: -x[1]):
        #     res += char * abs(freq)

        # return res


                