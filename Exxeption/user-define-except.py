class MyCustomException(Exception):     #inhertiance 
    pass
age = 5
try:
    if age<18:
        raise MyCustomException("You must be 18 or older")
    print("Eligible")
# except MyCustomException as e: -- if except is not there.. exception will come in terminal
#     print("Error:",e)
# else:
#     print("Access granted")
finally:
    print("Done")
