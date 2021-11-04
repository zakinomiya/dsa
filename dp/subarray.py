testcases = [{
    "in": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    "expected": 6,
}, {
    "in": [1],
    "expected": 1,
}, {
    "in": [5, 4, -1, 7, 8],
    "expected": 23,
}]

# https://leetcode.com/problems/maximum-subarray/discuss/898915/Python-easy-solution-with-explanation-(two-approaches-DP-with-and-without-table)
# the main idea is to find the possible max sum at index i (dp[i] is the max sum at index i) and if dp[i] is found , then dp[i+1] can be found easily(doing it i-1 and i in this case, but nothing different).
# dp[i] is either dp[i-1] + num[i] or num[i]. I first found it difficult to get the image because dp[i] seems lacking the idea of the sum of consecutive numbers.
# it first seems dp[i-1] is the max sum of num[0] to num[i-1], but this is not the case; not only the case, more precisely.
# dp[i-1] is a product of the comparison(dp[i-2] + num[i-1] to num[i-1]) and in case where dp[i-1] = num[i-1], it means the possible maximum sum at index i is num[i] and all the numbers before i
# can be ignored. Therefore, if dp[i] = dp[i-1] + num[i], then dp[i] is sum of num[i-1] + num[i]
def main(l):
    # initialise dp array
    dp = [0] * len(l)
    for i in range(len(l)):
        dp[i] = max(dp[i-1] + l[i], l[i])

    return max(dp)


if __name__ == "__main__":
    f = False
    for t in testcases:
        r = main(t["in"])
        if (r != t["expected"]):
            print(f"test failed. expected {t['expected']}, but actual {r}")
            f = True

    print("All the test cases passed!" if not f else "test failed.")
