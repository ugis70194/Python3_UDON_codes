[NY := list(map(int, input().split())), ans := [-1,-1,-1], [ans := [x, y, NY[0]-x-y] for x in range(0, NY[0]+1) for y in range(0, NY[0]+1-x) if 10000*x + 5000*y + 1000*(NY[0]-x-y) == NY[1]], print(ans[0], ans[1], ans[2])]