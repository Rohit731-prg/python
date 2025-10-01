# implement a countdown timer

import time  # time is a package that have modules related time

min = int(input("Enter Min : "))
sec = int(input("Enter Sec : "))

if (min != 0):
    total_sec = (min * 60) + sec
else:
    total_sec = sec

time.sleep(total_sec) # sleep modules tet you hold the program and works with milisec.
print("Time is end..!")