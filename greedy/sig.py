def maxProfit(a,b) -> int:
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]

    return s

if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(maxProfit(sorted(a), sorted(b)))
