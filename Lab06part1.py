#student name:      Liam Foster
#student number:    40199382

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list, permission: multiprocessing.Lock()):
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks
       permission is a mutex lock associated with picking up chopsticks
       to pick up chopsticks, the philosopher must acquire the permission lock and ask permission to dine
       after picking up chopsticks, the philosopher releases the permission lock before eating
       this way only one philosopher can pick up chopsticks at a time but others can still eat at the same time
    """
    def eatForAWhile():   #simulates philosopher eating time with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
    
    def thinkForAWhile(): #simulates philosopher thinking time with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

    for _ in range(6): #to make testing easier, instead of a forever loop we use a finite loop
        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers

        #to simplify, try statement not used here
        #
        permission.acquire()
        print(f"DEBUG: philosopher{id} has asked permission to dine")
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
        chopstick[rightChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")
        permission.release()
        print(f"DEBUG: philosopher{id} has released dining permission")

        eatForAWhile()  #use this line as is

        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()

        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5
    mutex = multiprocessing.Lock()  #this lock will block philosophers from picking up chopsticks 

    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList, mutex)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()