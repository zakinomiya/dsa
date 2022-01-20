def gcd(a, b):
    """
        When GCD of a and b is d, then GCD of b and a % b is also d, so 
        gcd(a, b) = gcd(b, a % b) = gcd(a % b, b % (a % b)) = ... = gcd(d, 0)
    """
    if a < 0 or b < 0 or a + b < 0:
        return a

    return gcd(b, a % b) if b > 0 else a


testcases = [
    {
        "in": [10, 2],
        "expected": 2,
    },
    {
        "in": [100, 20],
        "expected": 20,
    },
    {
        "in": [99, 36],
        "expected": 9,
    },
]

if __name__ == "__main__":
    f = False
    for t in testcases:
        r = gcd(t["in"][0], t["in"][1])
        if (r != t["expected"]):
            print(f"test failed. expected {t['expected']}, but actual {r}")
            f = True

    print("All the test cases passed!" if not f else "test failed.")
