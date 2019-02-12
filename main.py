import subprocess
from datetime import datetime
import platform

#Checking for current OS
osName = platform.system()


#Grabbing minutes/hours till shutdown and printing
sleepMinutes = input("In how many minutes do you want the PC to shutdown?: ")
sleepHours = input("In how many hours do you want the PC to shutdown?: ")

print("The PC will shutdown in " + str(sleepMinutes) + " minutes and " + str(sleepHours) + " hours.")


#Passing shutdown command to terminal. Will differ if it's Unix or Windows OS
if osName == "Windows":
    timeToSeconds = sleepMinutes * 60 + sleepHours * 60 * 60
    subprocess.run(["shutdown", "/s", "/t", timeToSeconds])
    #idea: adding Time and Date here at which time it will shutdown
    #idea: maybe add wait command, so that the popup window wont show up
else:
    subprocess.run(["shutdown", sleepMinutes])