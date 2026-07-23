# cook your dish here
t=int (input())
for i in range (t):
    N,X,K=map(int ,input().split())
    bottles=K//X
    print (min(N,bottles))