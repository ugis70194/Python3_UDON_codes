# Problem: https://atcoder.jp/contests/abs/tasks/abc081_b
N = int(input())
A = list(map(int, input().split()))

factor_2 = lambda a, c : c if a%2 else factor_2(a//2, c+1)
ans = min([ factor_2(a, 0) for a in A])

print(ans)