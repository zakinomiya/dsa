
def a():
    S, T, X = [ int(n) for n in input().split()]

    if S < T:
        if S <= X < T:
            return "Yes"
    else:
        if T <= X:
            if S - 24 <= X - 24 < T:
                return "Yes"
        else:
            if S - 24 <= X < T:
                return "Yes"

    return "No"

def b():
    _, X = [ int(n) for n in input().split()]
    A = [ int(n) for n in input().split()]

    d = {}
    x = X
    cnt = 0
    while x not in d:
        d[x] = 1
        x = A[x - 1]
        cnt += 1

    return cnt

import heapq

def c():
    N, K = [ int(n) for n in input().split()]
    A = [0] * N
    for i in range(N):
        s = sum([ int(n) for n in input().split()])
        A[i] = s

    top = A.copy()
    heapq.heapify(top)
    top = heapq.nlargest(K, A)

    for n in A:
        if n + 300 >= top[-1]:
            print("Yes")
        else:
            print("No")

NN = 1048576

def d():
    Q = int(input())
    A = {}
    for _ in range(Q):
        t, x = [int(n) for n in input().split()]
        if t == 2:
            print(A.get(x % NN, -1))
            continue
        if t == 1:
            h = x
            if A.get(h % NN, -1) != -1:
                keys = A.keys()
                for i in range(len(keys)-1):
                    if keys[i] < h % NN <= keys[i+1]:
                        A[] = x
                        break
            else:
                A[h%NN] = x



if __name__ == "__main__":
    d()
