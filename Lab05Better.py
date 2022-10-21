#student name: Liam Foster
#student number: 40199382

"""
    I have changed the template code in the following ways:

    - The waitForItemToBeConsumed function is changed so that "item" is no longer an argument
    - The debug messages are moved into the try block of the code so that they only print if the item is actually
    inserted or removed from the buffer
"""


import threading
import random #is used to cause some randomness 
import time   #is used to cause some delay in item production/consumption

class circularBuffer: 
    """ 
        This class implement a barebone circular buffer.
        Use as is.
    """
    def __init__ (self, size: int):
        """ 
            The size of the buffer is set by the initializer 
            and remains fixed.
        """
        self._buffer = [0] * size   #initilize a list of length size
                                    #all zeroed (initial value doesn't matter)
        self._in_index = 0   #the in reference point
        self._out_index = 0  #the out reference point

    def insert(self, item: int):
        """ 
            Inserts the item in the buffer.
            The safeguard to make sure the item can be inserted
            is done externally.
        """
        self._buffer[self._in_index] = item
        self._in_index = (self._in_index + 1) % SIZE

    def remove(self) -> int:
        """ 
            Removes an item from the buffer and returns it.
            The safeguard to make sure an item can be removed
            is done externally.
        """
        item = self._buffer[self._out_index]
        self._out_index = (self._out_index + 1) % SIZE
        return item

def producer() -> None:
    """
        Implement the producer function to be used by the producer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeProduced() -> int: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        return random.randint(1, 99)  #an item is produced

    for _ in range(SIZE * 2): #we just produce twice the buffer size for testing
        item = waitForItemToBeProduced()  #wait for an item to be produced
        #print(f"DEBUG: {item} produced")
        #complete the function below here to correctly store the item in the circular buffer
        
        mutex.acquire()                     #acquire lock
        try:
            #check if there is space in the buffer
            if empty._value != 0:
                buffer.insert(item)             #insert item into buffer
                full.release()                  #increment full
                empty.acquire()                 #decrement empty
                print(f"DEBUG: {item} produced")
        finally:
            mutex.release()                 #release lock no matter what


def consumer() -> None:
    """
        Implement the consumer function to be used by the consumer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeConsumed() -> None: #inner function; use as is
            time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
            #to simulate consumption, item is thrown away here by just ignoring it
    
    for _ in range(SIZE * 2): #we just consume twice the buffer size for testing
        #write the code below to correctly remove an item from the circular buffer
        
        mutex.acquire()                     #acquire lock
        try:
            #check that there are items to remove
            if full._value != 0:
                item = buffer.remove()          #remove item from buffer
                full.acquire()                  #decrement full
                empty.release()                 #increment empty
                print(f"DEBUG: {item} consumed")
        finally:
            mutex.release()                 #release lock no matter what
        
        #end of your implementation for this function
        #use the following code as is
        
        waitForItemToBeConsumed()  #wait for the item to be consumed
        #print(f"DEBUG: {item} consumed")

        

if __name__ == "__main__":
    SIZE = 5  #buffer size
    buffer = circularBuffer(SIZE)   #initialize the buffer

    full = threading.Semaphore(0)       #full semaphore: number of full buffers
                                        #initial value set to 0
    empty = threading.Semaphore(SIZE)   #empty semaphore: number of empty buffers
                                        #initial value set to SIZE
    mutex = threading.Lock()    #lock for protecting data on insertion or removal

    #complete the producer-consumer thread creation below
    producerThread = threading.Thread(target=producer)
    producerThread.start()
    consumerThread = threading.Thread(target=consumer)
    consumerThread.start()
    producerThread.join()
    consumerThread.join()