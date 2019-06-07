q,w=input().split()
e=int(q)
r=int(w)
for t in range(e+1,r): 
  c=0
  for u in range(1,r):
    if(t%u==0):
      d=d+1
  if(d==2):
    print(t,end=" ")
