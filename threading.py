from datetime import datetime
import threading
from time import sleep
stop_timer = False

def my_timer(timer_name):
    print (f"Timer {timer_name} started")
    while True:
        if stop_timer: break
        print(f"Timer {timer_name}\t{datetime.now()}")
        sleep(1)
  


threading.Thread(target=my_timer, args=("My first timer",)).start()
threading.Thread(target=my_timer, args=("TIMER II", )).start()


sleep(5)
print ("MAIN: stopping timers")
stop_timer = True
