class Solution:
    def reverseWords(self, s: str) -> str:
        token_list = s.split()
        final_list = []
        n = len(token_list)
        for i in range(n):
            final_list.append(token_list[n-i-1])
        return ' '.join(final_list)



