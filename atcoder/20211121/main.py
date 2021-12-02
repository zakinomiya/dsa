def countNumbers(n, L ,R):
    k = 0
    count = 0 
    s = L
    while s <= R:
        if s ^ n < n:
            count += pow(2, k)
 
        k += 1
        n >>= 1
        s *= 2
 
    return count

#def a():
#    N, L, R = [int(n) for n in input().split()]
#
#    return count(R, N) - count(L, N) 

def a():
    N, L, R = [int(n) for n in input().split()]

    return countNumbers(N, L, R)

def dist(l, r, x):
    if x < l:
        return l - x
    elif l <= x <= r:
        return 0
    elif r < x:
        return x - r


def b():
    N = int(input())
    minR = 0
    maxL = 0
    for k in range(N):
        L, R = [int(n) for n in input().split()]
        if k == 0:
            maxL = L
            minR = R

        if maxL < L:
            maxL = L
        if R < minR:
            minR = R

        x = maxL
        if maxL > minR:
            x = minR + (maxL - minR) // 2

        print(dist(maxL, minR, x))


if __name__ == "__main__":
    print(a())
