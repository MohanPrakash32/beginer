Num = int(input("Please Enter any Num: "))
Count = 0
while(Num> 0):
    Num = Num // 10
    Count = Count + 1

print("\n Num of Digits in a Given Num = %d" %Count)
