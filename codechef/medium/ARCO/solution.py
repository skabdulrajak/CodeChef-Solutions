# cook your dish here
n=int (input())
arr=list (map(int,input().split()))
s=arr
for i in range (len(arr)):
  
    if arr[i]==arr[i+1]:
        s.remove(arr[i])
        
print (len(s))