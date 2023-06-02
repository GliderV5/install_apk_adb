import sys
import os 
import time 
import subprocess

try:
    sortie = subprocess.check_output(["adb", "version"])
except subprocess.CalledProcessError as e:
    print("adb n'est pas installé ou il y a un problème. Essayez la commande <sudo apt-get install android-sdk-platform-tools>")
    print("appyez sur entrer pour quitter ...")
    input()
    exit()

os.system("clear")
file = sys.argv[1]
os.system("adb reconnect")
time.sleep(2)
os.system("clear")
os.system("adb install "+str(file))
print("")
print("Votre application est en cours d'installation, veuillez patienter ...")