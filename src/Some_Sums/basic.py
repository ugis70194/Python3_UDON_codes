N, A, B = map(int, input().split())

ans = 0
for n in range(0, N+1):
    s = 0
    tmp = n
    while(tmp > 0):
        s += tmp%10
        tmp //= 10

    if A <= s <= B: 
        ans += n

print(ans)
