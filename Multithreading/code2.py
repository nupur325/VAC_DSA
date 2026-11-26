#create thread here
import threading
import time

def greet1():
    time.sleep(3)
    print("Helloooooooooooo")
    
def greet2():
    print("Helloooooooooooo Surabhiiiiiiiiii")
    # time.sleep(1)

def greet3():
    print("Helloooooooooo Shivammmmmm")
    time.sleep(2)

t1 = threading.Thread(target=greet1)
t1.start()
t1.join()
t2 = threading.Thread(target=greet2)
t2.start()
t2.join()
t3 = threading.Thread(target=greet3)
t3.start()
print("Main program continue")