#parameter passed 
import threading
def greet(name,age):
    print("Hello",name)
    print(age)

t1 = threading.Thread(target=greet, args=("Nupur",15))
t1.start()
t1.join()