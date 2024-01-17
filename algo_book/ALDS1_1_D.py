
# Rt is price at the time of t
# WANT: max(Rj - Ri) [j > i]
# INPUT: 
#   first line: number n 
#   following n lines: the price at the time of t (t = 0,1,2...n)
#   2 <= n <= 200,000 
#   1 <= Rt <= 10^9
# 
# PSEUDO CODE:
#   maxv = 0
#   minv = 0
#   for i=0; i<n; i++:
#       price = input[i] 
#       maxv = max(maxv, price-minv)
#       if price < minv:
#           minv = price           
#           
#   return maxv 
# 
# 
def solve():
    N = int(input())
    prices = []
    for _ in range(N):
        prices.append(int(input()))

    if len(prices) == 1:
        return 0

    maxv = -10**9
    minv = prices[0]
    for i in range(1, N):
        price = prices[i]
        maxv = max(maxv, price-minv)
        if price < minv:
            minv = price
    return maxv

if __name__ == "__main__":
    print(solve())
