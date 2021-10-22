import os
import psutil
import time
import subprocess


#                                   Check if firefox is running
#----------------------------------------------------------------------------------------------

Process_names = []
firefox_is_running = False
time_browsing = 0
minutes = 0
cooldown_minutes = 0

def is_firefox_open():
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()

            for Process_names in process_name:
                if process_name == "firefox.exe":
                    firefox_is_running = True
                    print("firefox is running")         
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return(firefox_is_running)

# I have to force it to run for now
is_firefox_open()
firefox_is_running = is_firefox_open()



#                                  Count how long firefox is running
#----------------------------------------------------------------------------------------------

def timer(minutes, time_browsing):
    while firefox_is_running == True:
        time.sleep(60)
        minutes += 1
        time_browsing = minutes
        print(time_browsing)
    return(time_browsing)


timer(minutes,time_browsing)  
time_browsing = timer(time_browsing)

#                                           Kill firefox
#----------------------------------------------------------------------------------------------


if firefox_is_running and time_browsing > 29:
    os.system("taskkill /f /im firefox.exe")
    firefox_is_running = False


#                                        Firefox Cooldown
#----------------------------------------------------------------------------------------------


while firefox_is_running == False:
    time.sleep(60)
    cooldown_minutes += 1
    if cooldown_minutes > 59:
        time_browsing = 0
