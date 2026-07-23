# cook your dish here
t=int (input())
for i in range (t):
    x,y=map(int ,input().split())
    score=y-x
    if score==0:
        print ("0")
    elif score >0 and score <= 8:
        print ("1")
    elif score %8==0:
        print (score//8)
    else:
        print ((score //8 )+1)
