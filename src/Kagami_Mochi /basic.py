N = int(input())
D = [int(input()) for i in range(0, N)]

D.sort(reverse=True)

last = 1000
ans  = 0
for d in D:
    if last > d:
        last = d
        ans += 1

print(ans)