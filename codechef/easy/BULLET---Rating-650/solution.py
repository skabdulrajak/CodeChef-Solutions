# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    travel = y // x
    wait = z - travel
    print(max(0, wait))