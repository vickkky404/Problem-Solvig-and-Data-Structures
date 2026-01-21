#A thread is a small unit of a processor, thread allow multiple task to run at the same time.


# this module is used to create and manage threads in Python..
import threading
import time

# function that will run in a thread
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)  #pause for 1 second

# fun. that will run in another thread
def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", ch)
        time.sleep(1)

# create thread obj.
thread1 = threading.Thread(target=print_numbers())
thread2 = threading.Thread(target=print_letters())


# lets start the threads
thread1.start()
thread2.start()


# waiting for both thread to cmplete
thread1.join()
thread2.join()

print("Main Program ended")