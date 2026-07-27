# cook your dish here
n=int (input())
arr=list (map(int,input().split()))
s=[]
for i in range (len(arr)):
   for j in range (i+1,len(arr)):
    if arr[i]!=arr[j]:
        s.append(arr[i])
        break
print (len(s))