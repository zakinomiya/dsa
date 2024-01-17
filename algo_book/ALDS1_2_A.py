# Bubble sort
def main(A, N):
    flag = True
    while flag:
        flag = False
        for i in range(N-1, 0, -1):
            if A[i] > A[i-1]:
                A[i-1], A[i] = A[i], A[i-1]
                flag = True
    print(A)

if __name__ == "__main__":
    main([2,3,1,4,6,3,4], 7)

def main():
    print("hello")

if __name__ == "__main__":
    main()
