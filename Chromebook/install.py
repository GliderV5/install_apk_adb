import sys
import os
import time
import subprocess

try:
    output = subprocess.check_output(["adb", "version"])
except subprocess.CalledProcessError as e:
    print("adb is not installed or there is a problem. Try the command <sudo apt-get install android-sdk-platform-tools>")
    print("press enter to exit ...")
    input()
    exit()

try:
    os.system("clear")
    file = sys.argv[1]
    os.system("adb reconnect")
    time.sleep(2)
    os.system("clear")
    os.system("adb install "+str(file))
    os.system("clear")
    print()
    print("Your application has been installed")
except:
    print("there was an error during installation, the file could not be installed correctly")