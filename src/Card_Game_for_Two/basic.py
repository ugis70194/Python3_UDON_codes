N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
Alice = sum(A[0::2])
Bob   = sum(A[1::2])
print(Alice - Bob)