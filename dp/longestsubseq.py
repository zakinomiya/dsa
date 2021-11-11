testcases = [
    {
        "in": 0,
        "expected": 0,
    },
]

# https://leetcode.com/problems/longest-increasing-subsequence/
def main(nums) -> int:
    dp = [1] * len(nums)


    return max(dp)

if __name__ == "__main__":
    f = False
    for t in testcases:
        r = main(t["in"])
        if (r != t["expected"]):
            print(f"test failed. expected {t['expected']}, but actual {r}")
            f = True

    print("All the test cases passed!" if not f else "test failed.")
