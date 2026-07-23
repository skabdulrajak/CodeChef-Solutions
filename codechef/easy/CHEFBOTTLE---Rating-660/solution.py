# cook your dish here
t=int (input())
while t:
   n=int (input())
   s=input()
   result=[]
   mapping ={'A':'T','T':'A','C':'G','G':'C'}
   for char in s:
       result.append(mapping[char])
   print ("".join(result))
   t=t-1