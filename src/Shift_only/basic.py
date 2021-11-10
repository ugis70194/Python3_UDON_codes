# Problem: https://atcoder.jp/contests/abs/tasks/abc081_b
N = int(input())
A = list(map(int, input().split()))

ans = 1e9
for a in A:
    factor_2 = 0
    while(a % 2 == 0):
        factor_2 += 1
        a //= 2
    ans = min(ans, factor_2)

print(ans)