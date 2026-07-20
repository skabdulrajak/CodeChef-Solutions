# cook your dish here
t=int (input())
while t:
    x,y,n,m=map(int,input().split())
    if x+y <= n+m:
        print (x+y)
    else:
        print(n+m)
    t=t-1