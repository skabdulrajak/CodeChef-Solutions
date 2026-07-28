# cook your dish here
t=int (input())
while t:
    x,y=map(int,input().split())
    if y*10  < x:
        print("YES")
    else :
        print ("NO")
    t=t-1