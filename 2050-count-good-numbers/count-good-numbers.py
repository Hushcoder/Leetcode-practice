class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 == 0:
            E = n // 2
            O = n // 2
        else:
            E = n // 2 + 1
            O = n // 2
        return (computePow(5,E,MOD) * computePow(4,O,MOD)) % MOD

MOD = 10 ** 9 + 7

def computePow(x,n, mod = MOD):
    if n == 0:
        return 1
    if n % 2 == 0:
        return computePow((x * x) % mod, n // 2)
    else:
        return (x * computePow((x * x) % mod, n // 2)) % mod
    