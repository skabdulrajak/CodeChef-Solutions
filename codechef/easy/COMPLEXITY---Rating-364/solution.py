# cook your dish here
t=int (input())
while t:
    n,m=map(int ,input().split())
    if n<=m:
        print ("NO")
    else:
        print ("YES")
    t=t-1