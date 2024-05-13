# Milage Calculator
# Begin Date: 04/25/2024
# Mod.  Date: 05/11/2024
# Version 1.1

from datetime import datetime   #Import datetime Module.

if __name__ == "__main__":      #Enterance point to the Python Program.

        driversName = ""
goalPlace = ""
startPlace = ""
endPlace = ""
startMilage = 0
endMilage = 0
total = 0

print("")
print("======================")
print("Milage Calculator")
print("By: Dan Uff")
print("Version 1.1")
print("")
print("(c) 2024 CPS CO.")
print("======================")
print("https://www.cpsoft.us/")
print("======================")
print("")

driversName = input("Driver's FULL Name :")
goalPlace = input("Where are you going :")
startPlace = input("Where did you START:")
endPlace = input("Where you STOP :")
startMiliage = input("STARTING Milage :")
endMilage = input("ENDING Milage :")
showDat = datetime.now()

total = (int(startMiliage) + int(endMilage))

print("===================================================")
print("Driver's Name :",str(driversName))
print("You're going to: ",str(goalPlace))
print("You're coming from: ",str(startPlace))
print("You stopped at: ",str(endPlace))
print("Starting Milage: ",int(startMiliage))
print("Ending Milage: ",int(endMilage))
print("")
print("You drove a total of ",int(total),"miles today.")
print("===================================================")
print("")
print("*** END OF INFORMATION ***")
print("")
print(str(driversName)+"'s information as of:",showDat)
print("===================================================")

