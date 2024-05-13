# Date Written: April 16th, 2024
# Date Modified: May 12th, 2024
# Name: Days old Program.
# Language: Python 2 / 3.

firstName = ""
middleName = ""
lastName = ""
age = 0
mon = 0
day = 0
yer = 0
answer = 0

print("")
print("===================")
print("Days Old Calculator")
print("By: Dan Uff")
print("Version 1.2")
print("")
print("(c) 2024 CPS CO.")
print("===================")
print("https://www.cpsoft.us/")
print("")


firstName = input("Enter your FIRST Name: ")                # Enter FIRST name.
lastName = input("Enter your LAST Name: ")                  # Enter LAST name.
age = input("How OLD are you (AA): ")
mon = input("Enter the MONTH you were Born (M) or (MM):")
day = input("Enter the DATE you were Born (D) or (DD):")
yer = input("Enter the YEAR you were born: (YYYY):")

answer = (int(yer)) * 365.24

print("----------------------------------------------------------------------------------------------------")
print(firstName,lastName,"who is",int(age),"years old is",int(answer),"days old, since",int(mon),int(day),int(yer))
print("----------------------------------------------------------------------------------------------------")

exiMeB = input("Press ENTER to Exit :")

