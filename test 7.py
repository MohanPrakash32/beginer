number = int(input("Please Enter any Number: "))
tot = 0

for value in range(1,number+1):
    tot= tot + value

print("The Sum of Natural Number from1to{0} ={1}".format(number, tot))
