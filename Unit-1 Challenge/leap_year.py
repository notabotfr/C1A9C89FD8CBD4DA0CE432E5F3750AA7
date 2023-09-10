try:
    a=int(input("Enter year: "))
except ValueError:
    print("Enter numbers only!")
if a<0:
    print("Input positive integers only")
elif (a % 4 == 0 and a % 100 != 0) or (a% 400 == 0):
    print(a,"is a leap year: ")
else:
    print("Its not a leap year: ")