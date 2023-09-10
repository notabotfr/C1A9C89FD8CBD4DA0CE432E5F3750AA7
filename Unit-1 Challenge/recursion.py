def fact(n):
    if n == 0:
        return 1
    elif n < 1:
        print("Enter whole numbers only: ")
        return None  
    else:
        return n * fact(n-1)

while True:
    try: 
        n = int(input("Enter a number: "))
    except Exception:
        print("Input proper values only")
    else:  
        result = fact(n)
        if result is not None:
            print("The factorial of",n,'is',result)
    a = input("Continue? (y/n): ")
    if a.lower() == 'n':
        break
