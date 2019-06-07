    
c,b=[int(c)  for a in input().split()]
for i in range(c,b):
        s=0
        t=i
        while(i!=0):
               d=i%10
               p=p+d*d*d
                i=i//10
        if(c==s):
                print(t,end=' ')
