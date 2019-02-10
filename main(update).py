import subprocess
import platform

# Checking for current OS
osName = platform.system()


def TimeConvert(minutes, hours):
    # Convert hours to minutes and add to original minute count
    total = minutes + (hours * 60)
    # Convert to seconds from minutes
    seconds = total * 60
    return seconds


def GetInput():

    # Grabbing minutes/hours till shutdown and returning number
    # Creates the Global variable rather than them being confined to
    # the current function

    global slp_min
    global slp_hrs

    # Error checking for input, Makes sure is actually a number.
    try:
        slp_hrs = int(input(
            "In how many hours do you want the PC to shutdown?: "))
        slp_min = int(input(
            "In how many minutes do you want the PC to shutdown?: "))
    # Exception that is thrown when entering non-integer value.
    # Restarts getinput function rather than completely stopping.
    except(ValueError):
        print("This is not a number")
        GetInput()


GetInput()

print(f"The pc will shutdown in {slp_hrs} hours and {slp_min} minutes")
print(f"Shutdown in {TimeConvert(slp_min, slp_hrs)} seconds.")

# Passing shutdown command to terminal. Will differ if it's Unix or Windows OS
if osName == "Windozs":
    subprocess.run(["shutdown", "/s", "/t", TimeConvert(slp_min, slp_hrs)])

# idea: adding Time and Date here at which time it will shutdown
# idea: maybe add wait command, so that the popup window wont show up

else:
    print("Sorry i don't support other OS's yet.")
