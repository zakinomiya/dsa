# Selection Sort
# for i = 0 to N-1
#   minj = i
#   for j = i to N-1   
#       if A[j] < A[minj]   
#           minj = j   
#   swap A[i] and A[minj]
def main(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj=j
        A[i], A[minj] = A[minj], A[i]
    print(A)

if __name__ == "__main__":
    main([2,4,1,4,3,5,3,6,7], 9)
