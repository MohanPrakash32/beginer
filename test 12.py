bx=input()
bx=ax.split()
bx=list(map(int,bx))
cx=bx[0]
dx=bx[1]
for i in range(cx+1,dx):
    if i%2!=0:
        print(i,"",end="")
