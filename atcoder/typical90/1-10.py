######################
# Yokan Party（★4）
######################


def solve(k, a, thres):
    l = 0 
    cnt = 0
    for r in a:
        if thres <= r - l:
            cnt += 1
            l = r
    ret = k <= cnt
    return ret


def q1():
    N, L = [int(n) for n in input().split()]
    K = int(input())
    A = [int(n) for n in input().split()]
    A.append(L)

    l, r = 0, L
    while r - l > 1:
        mid = (l + r) // 2

        if solve(K+1, A, mid):
            l = mid
        else:
            r = mid

    return l

def pad(n: int, o: str) -> str:
    return "0" * (n - len(o)) + o

def q2():
    N = int(input())
    if N % 2 != 0:
        return 

    for i in range((2**N)-1):
        bstr = pad(N, bin(i)[2:])
        count = 0
        for s in bstr:
            if s == "0":
                count += 1
            else:
                count -= 1

            if count < 0:
                break

        if count == 0:
            print(bstr.replace("0", "(").replace("1", ")"))
                


######################
# Encyclopedia of Parentheses（★3）
######################

# - full search
# - criteria of a right-closed parentheses
#  1. the number of "(" and ")" is the same
#  2. when counting the number from left to right, the number of ")" never be greater than that of "("
# - bit representation: 0 -> "(", 1 -> ")". the order of the original numbers is the same as the order of parentheses (when the order is defined as ")" > "(" )


if __name__ == "__main__":
    # print(q1())
    q2()
