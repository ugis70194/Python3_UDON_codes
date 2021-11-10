import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

idx = bisect.bisect_left(A, K)
if idx == len(A): idx = -1

print(idx)