######################
# Yokan Party（★4）
######################
def solve(A, m, k):
    l = 0
    cnt = 0
    for i in range(len(A)):
        if A[i] - A[l] >= m:
            l = i
            cnt += 1

    return cnt >= k + 1


def q1():
    _, L = [int(n) for n in input().split()]
    K = int(input())
    A = [int(n) for n in input().split()]
    a = [0] + A + [L]

    left, right = 0, L
    while right - left > 1:
        mid = (right + left) // 2
        if solve(a, mid, K):
            left = mid
        else:
            right = mid

    return left

######################
# Encyclopedia of Parentheses（★3）
######################

# - full search
# - criteria of a right-closed parentheses
#  1. the number of "(" and ")" is the same
#  2. when counting the number from left to right, the number of ")" never be greater than that of "("
# - bit representation: 0 -> "(", 1 -> ")". the order of the original numbers is the same as the order of parentheses (when the order is defined as ")" > "(" )



def pad(i, s):
    if len(s) < i:
        return ("0" * (i - len(s))) + s

    return s


def q2():
    N = int(input())
    if N % 2 != 0:
        return

    for i in range((2 ** N) -1):
        bstr = pad(N, bin(i)[2:])
        cnt = 0
        ans = ""
        for s in bstr:
            if s == "0":
                cnt += 1
                ans += "("
            else:
                cnt -= 1
                ans += ")"

            if cnt < 0:
                break

        if cnt == 0: 
            print(ans)


if __name__ == "__main__":
    q2()
