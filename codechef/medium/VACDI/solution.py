# cook your dish here
n=int (input())
arr=list (map(int,input().split()))
vas=list (map(int,input().split()))
count=0
for i in range (1,n):
    if arr[i]<vas[i]:
        count+=1
if count ==n:
    print ("YES")
else:
    print ("NO")
