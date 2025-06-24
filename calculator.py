print("1. ADD")
print("2. Subtract")
print("3. multiply")
print("4. divide")
calcu = int(input("Enter what to do."))
if calcu == 1:
     sum1 = int(input("Enter 1st number:"))
     sum2 = int(input("Enter 2nd number:"))
     print(sum1 + sum2)
elif calcu == 2:
    subtract = int(input("Enter 1st number:"))
    subtract2 = int(input("Enter 2st number:"))
    print(subtract - subtract2)
elif calcu == 3:
    multi = int(input("Enter 1st number:"))
    multi2 = int(input("Enter 2st number:"))
    print(multi * multi2)
elif calcu == 4:
    divide = int(input("Enter 1st number:"))
    divide2 = int(input("Enter 2st number:"))
    print(divide / divide2)
else:
    print("Invalid")