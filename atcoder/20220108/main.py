import math
import heapq


def c():
    K = int(input())
    s = bin(K)[2:]
    ss = ""

    for c in s:
        ss += str(int(c) * 2)

    return int(ss)

    

def distance(a,b):
    y = float(abs(b[1] - a[1]))
    x = float(abs(b[0] - a[0]))

    return math.sqrt(x** 2 +  y **2)


def b():
    N = int(input())
    arr = []

    for i in range(N):
        (x,y) = input().split()
        arr.append((int(x), int(y)))

    d = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            l = distance(arr[i], arr[j])
            if d < l:
                d = l
        
    return d


##########
def f(x):
    return x ** 2 + 2 * x + 3

def a():
    t = int(input())
    return f(f(f(t) + t) + f(f(t)))

    
