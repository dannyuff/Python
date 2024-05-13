# Number of Hours Worked.
# Created: 05-04-2024
# Modified: 05-11-2024

name = input("Enter your FULL Name :")
beginHour = input("What time did you BEGIN work (HH) :")
endingHour = input("What time did you END work : (HH) :")

from datetime import datetime

calculate = int(beginHour * int(endingHour)) / 60

print(int(calculate))
print("-------------------------------------------")

endProgrm = input("Press ENTER to Exit :")
