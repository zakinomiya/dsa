def minRefills(m, s) -> int:
    r = 0
    d = 0

    for i in range(len(s)-1):
        if s[i] - d > m:
            return -1

        if s[i] <= d + m <= s[i+1]:
            r += 1
            d += s[i]

    return r


if __name__ == "__main__":
    d, m, _ = [int(input()) for _ in range(3)]
    stops = [int(n) for n in input().split()]
    print(minRefills(m, stops+[d]))
