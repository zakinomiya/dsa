
def run():
    N = input()
    arr = [ int(n) for n in input().split()]

    m = (-1,-1)
    for n in enumerate(arr):
        m = max(m, n, key=lambda x: x[1])

    return m[0]+1


if __name__ == "__main__":
    print(run())
