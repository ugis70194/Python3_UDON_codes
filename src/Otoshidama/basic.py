N, Y = map(int, input().split())

a, n, s = [-1, -1, -1]
for x in range(0, N+1):
    for y in range(0, N+1-x):
        z = N - (x + y)
        if 10000*x + 5000*y + 1000*z == Y:
            a, n, s = [x, y, z]

print(a, n, s)