# cook your dish here
t=int (input())
while t:
    n=int (input())
    s=input()
    s = s.replace("A", "x")
    s = s.replace("T", "y")
    s = s.replace("C", "z")
    s = s.replace("G", "w")
    
    s = s.replace("x", "T")
    s = s.replace("y", "A")
    s = s.replace("z", "G")
    s = s.replace("w", "C")
    
   

  
    print (s)
    t=t-1
