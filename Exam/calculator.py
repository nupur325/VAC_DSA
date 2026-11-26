try:
    a = int(input("ENter one number:"))
    b = int(input("Enter another num:"))
    result  = a/b
    print(result)
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Enter a positive number")
else:         #executes if no exception occured
    print("Program completed")
finally:        #runs despite error occured or not
    print("Program completed")

