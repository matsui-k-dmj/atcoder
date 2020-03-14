# factのstartを指定しとけば, 計算量O(k)になる
def comb(n, k, mod):
    a = factmod(n, n - k + 1, mod)
    b = factmod(k, 1, mod)

    div = pow(b % mod, mod - 2, mod)  # フェルマーの小定理

    return a * div % mod


def factmod(n, start, mod):
    val = 1
    for i in range(start, n + 1):
        val *= i
        val %= mod
    return val


# O(N)
class Comb:
    def __init__(self, N, MOD=10**9 + 7):
        self.fac = [0 for _ in range(N)]
        self.finv = [0 for _ in range(N)]
        self.inv = [0 for _ in range(N)]
        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, N):
            self.fac[i] = self.fac[i - 1] * i % MOD
            self.inv[i] = MOD - self.inv[MOD % i] * (MOD // i) % MOD
            self.finv[i] = self.finv[i - 1] * self.inv[i] % MOD

        self.MOD = MOD

    def comb(self, n, k):
        if n < k:
            return 0
        if (n < 0 or k < 0):
            return 0

        return self.fac[n] * (self.finv[k] * self.finv[n - k] %
                              self.MOD) % self.MOD
