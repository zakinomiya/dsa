testcases = [
    {
        "in": [7, 1, 5, 3, 6, 4],
        "expected": 7,
    },
    {
        "in": [1, 2, 3, 4, 5],
        "expected": 4,
    },
]

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


def main(prices: list[int]) -> int:
    dp = [0] * len(prices)
    minp = 10 ** 4 + 1
    for i, p in enumerate(prices):
        minp = min(minp, p)
        dp[i] = max(dp[i-1], dp[i-1] + p - minp)
        if dp[i] != dp[i-1]:
            minp = p

    return max(dp)


if __name__ == "__main__":
    f = False
    for t in testcases:
        r = main(t["in"])
        if (r != t["expected"]):
            print(f"test failed. expected {t['expected']}, but actual {r}")
            f = True

    print("All the test cases passed!" if not f else "test failed.")
