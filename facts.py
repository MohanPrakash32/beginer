from itertools import combinations
a,b=map(int,input().split())
s=len(str(a))
L=list(combinations(str(a),s-b))
L=(sorted(L))
z="".join(L[0])
print(z)
