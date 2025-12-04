num=""
check=""
num=int(input("Enter a number: "))
check=int(input("Enter a number to check: "))
if num%check==0:
    print(num ," is multiple of ",check)
else:
    print(num ," is not multiple of ",check)    