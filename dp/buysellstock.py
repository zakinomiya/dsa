testcases = [
    {
        "in": [7, 1, 5, 3, 6, 4],

        "expected": 5,
    },
    {
        "in": [7, 6, 4, 3, 1],
        "expected": 0,
    },
]

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# -- very simple solution will be just to iterate over i and j where i is the day to sell and j is the day to buy, but time comlexity is O(n^2), so must be a better one
# track the minimum price and max profit
def main(prices: list[int]) -> int:
    maxp, minp = 0, 10**5 + 1
    for p in prices:
        minp = min(minp, p)
        maxp = max(maxp, p - minp) 
    return maxp


if __name__ == "__main__":
    f = False
    for t in testcases:
        r = main(t["in"])
        if (r != t["expected"]):
            print(f"test failed. expected {t['expected']}, but actual {r}")
            f = True

    print("All the test cases passed!" if not f else "test failed.")
