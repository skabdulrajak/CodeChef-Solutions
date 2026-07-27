# cook your dish here
n=int (input())
arr=list (map(int,input().split()))
vas=list (map(int,input().split()))
arr.sort()
vas.sort()
for i in range (n):
    if arr[i]<vas[i]:
        print ("No")
        break
else:
    print ("YES")