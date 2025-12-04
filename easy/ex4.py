list1=input("Enter numbers separed by space:").split()
list1=[int(x) for x in list1]
n=int(input("Enter a number to check if it's found"))
def order(list_to_search,n):
     for i in list_to_search:
          if i==n:
               return True
     return False
result=order(list1,n)
print("The number is found ",result)