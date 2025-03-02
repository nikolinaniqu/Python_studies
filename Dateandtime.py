import time
import datetime
while True:
    print("Exact time is:")
    my_time=time.localtime(time.time())
    print(my_time.tm_hour,"hours",my_time.tm_min,"minutes")
    time.sleep(60)
