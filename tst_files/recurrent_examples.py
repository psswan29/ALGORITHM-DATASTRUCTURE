# 最优化问题
# 找硬币问题
from functools import lru_cache

coinValueList = [1, 5, 10, 25]


@lru_cache(1024)
def recMC(change):
    mincoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(change - i)
            if numCoins < mincoins:
                mincoins = numCoins
    return mincoins
