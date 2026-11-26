#threading not used
import time
def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 complete")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 complete")
def task3():
    print("Task 3 started")
    time.sleep(1)
    print("Task 3 complete")
task1()
task2()
task3()