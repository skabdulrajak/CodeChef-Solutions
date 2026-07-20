# cook your dish here
t=int (input())
while t:
    x,y=map(int,input().split())
    if x*3 <=  y:
        print ("Yes")
    else:
        print ("NO")
    t=t-1