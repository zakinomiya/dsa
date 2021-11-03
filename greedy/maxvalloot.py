
def maxValOfLoot(W, items) -> float:
    r = W
    value = 0

    for v, w in items:
        if r > w:
            value += v
            r -= w
        else:
            value += v * (r / w)
            break

    return value


if __name__ == "__main__":
    n, W = [int(n) for n in input().split()]
    items = []
    for _ in range(n):
        items.append([int(n) for n in input().split()])

    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    print(f"{maxValOfLoot(W, items):.4f}")
