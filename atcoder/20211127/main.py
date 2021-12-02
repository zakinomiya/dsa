
def a():
    s1, s2 = input(), input()

    if s1[0] == "." and s2[1] == ".":
        return "No"
    elif s1[1] == "." and s2[0] == ".":
        return "No"

    return "Yes"

def b():
    s1,s2 = input().split()

    if len(s1) > len(s2):
        s2 = "0"*(len(s1)-len(s2)) + s2
    else:
        s1 = "0"*(len(s2)-len(s1)) + s1

    for i in range(len(s1)):
        if int(s1[i]) + int(s2[i]) >= 10:
            return "Hard"

    return "Easy"

from heapq import heappush, heappop

def c():
    N, W = [int(n) for n in input().split()]

    h = []
    for _ in range(N):
        A, B = [int(n) for n in input().split()]
        heappush(h, (-A,B))

    w = 0
    ans = 0
    while len(h) > 0 and w < W:
        (a, b) = heappop(h) 
        a = -a
        if b + w > W:
            ans += a * (W-w)
            break

        ans += a * b
        w+=b

    return ans

def d():
    S = input()
    K = int(input())

    m = 0
    dotCounts = [0] * len(S)

    for i in range(len(S)):
        if S[i] == ".":
            dotCounts[i] = dotCounts[i-1] + 1
        else:
            dotCounts[i] = dotCounts[i-1]

    c = 0
    for i in range(len(S)):
        while c < len(S)-1 and dotCounts[c+1] - dotCounts[i] <= K:
            c += 1

        m = max(m, c-i)

    return m

if __name__ == "__main__":
    print(d())
