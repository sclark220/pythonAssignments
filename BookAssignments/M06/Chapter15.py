import multiprocessing
import time
import random

def worker():
    # Wait a random number of seconds between 0 and 1
    waitTime = random.random()
    time.sleep(waitTime)

# Create and start three separate processes
processes = []
for _ in range(3):
    queue = multiprocessing.JoinableQueue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.daemon = True
    p.start()
    processes.append(p)

# Wait for all processes to finish
for p in processes:
    p.join()

print("All processes finished!")