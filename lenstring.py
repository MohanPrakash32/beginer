b=input()
b=int(b)
X=[]
for i in range(0,b):  
    y=input()
    X.append(y)
C=[]
for i in zip(*X):
    if i.count(i[0])==len(i): 
        C.append(i[0])
    else:
        break
print(''.join(C))
