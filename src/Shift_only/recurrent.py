# Problem: https://atcoder.jp/contests/abs/tasks/abc081_b
N = int(input())
A = list(map(int, input().split()))

def factor_2(a, c):
    if a%2:
        return c
    else:
        return factor_2(a//2, c+1)

ans = 1e9
for a in A:
    ans = min(ans, factor_2(a, 0))

print(ans)