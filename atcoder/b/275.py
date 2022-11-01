
def run():
    A, B, C, D, E, F = [int(n) for n in input().split()]

    return ((A * B * C) - (D * E * F)) % 998244353

if __name__ == "__main__":
    print(run())
