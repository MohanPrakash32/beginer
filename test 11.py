num=int(input("enter a num:"))
temp=num
rev=0
while temp!=0:
	rev=(rev*10)+(temp%10)
	temp=temp//10
 
if num==rev:
	print("num is yes")
else:
	print("num is not no")
