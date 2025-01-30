def b():
    H, W, N = [int(n) for n in input().split(" ")][:]
    
    grid = [[ "." for _ in range(W)] for _ in range(H)]
    
    # 0: up, 1: right, 2: down, 3: left
    direction = 0
    i, j = 0, 0
    for _ in range(N):
        if grid[i][j] == ".":
            grid[i][j] = "#"
            direction = change_direction(direction, True)
        else:
            grid[i][j] = "."
            direction = change_direction(direction, False)
        i, j = step(H,W,i,j,direction)

    # print_grid(grid)

def print_grid(grid):
    for row in grid:
        for color in row:
            print(color, end="")
        print("")

# return tuple(i, j)
def step(H, W, h, w, direction: int):
    if direction == 0:
        return ((h-1)%H, w)
    elif direction == 1:
        return (h, (w+1)%W)
    elif direction == 2:
        return ((h+1)%H, w)
    elif direction == 3:
        return (h, (w-1)%W)


def change_direction(dir: int, clockwise: bool) -> int:
    if clockwise:
        return (dir+1) % 4
    else:
        return (dir-1) % 4


def c():
    N = int(input())
    A = [int(n) for n in input().split(" ")]

    minv = 0
    sumv = 0
    for a in A:
        sumv += a
        minv = min(minv, sumv)

    print(sumv+(-minv))


if __name__ == "__main__":
    # b()
    c()
