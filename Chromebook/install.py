import sys
import os
import time
import subprocess

try:
    output = subprocess.check_output(["adb", "version"])
except subprocess.CalledProcessError as e:
    answer = input("adb is not installed on your computer. Do you want to install it now ? (y,n) >>> ")
    if answer == "yes":
        try:
            os.system("sudo apt-get install android-sdk-platform-tools -y")
            print()
            print("adb is now installed on your computer your app will be installed soon, please wait ...")
            time.sleep(5)
            os.system("clear")
        except:
            print()
            print("there was an error during installation")
            exit()
    else:
        exit()

try:
    os.system("clear")
    file = sys.argv[1]
    os.system("adb reconnect")
    time.sleep(2)
    os.system("clear")
    os.system("adb install "+str(file))
except:
    print("there was an error during installation, the file could not be installed correctly")