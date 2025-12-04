


def first_last(list):
    
    return [list[0],list[-1]]
list=input("Enter numbers separed by space:").split()
num=[int(n) for n in list]

result=first_last(num)
print("The new list is",result)