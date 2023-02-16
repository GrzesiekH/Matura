def W(j,A):
    while j > 0:
        if A[j]<A[j-1]:
            v = A[j]
            A[j] = A[j-1]
            A[j-1] = v
        j-=1
    return A