#! python3
import threading
import time
import logging

def sleep(gap,iteration):
    for i in range(iteration):
        logging.info("start sleeping")
        time.sleep(gap)
        logging.info("slept for {0}s".format(gap))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format='[%(levelname)s] (%(threadName)-10s) %(message)s')
    t1 = threading.Thread(target = sleep, args=(1,10)) # default to not daemon
    t2 = threading.Thread(target = sleep, args=(2,5))
    t1.start()
    t2.start()
