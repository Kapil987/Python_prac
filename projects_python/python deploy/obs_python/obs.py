# I have used os comands for a while
# this program will try to close a firefox window every ten secounds

import os
import time

# creating a forever loop
time.sleep(10)
os.system("TASKKILL /F /IM obs64.exe")

