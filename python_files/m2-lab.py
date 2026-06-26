# Todd Hamm
# SDEV 220
# Module 2 Lab
# m2-lab.py
# The purpose of this app is to determine if a student qualifies for the Dean's List or the Honor Roll based on their GPA. 
# The app will prompt the user for a student's last and first name as strings and their GPA as a float.
# It will then test if the GPA is 3.5 or greater; if so, it will print a message saying that the student has made the Dean's List.
# Next, it will test if the GPA is 3.25 or greater; if so, it will print a message saying that the student has made the Honor Roll.
# If the GPA is less than 3.25, it will print this message: "Student did not make the Dean's list or Honor Roll"
# If the last name entered is "ZZZ", the app will quit. 

first_name = input("Enter Student's First Name: ")
last_name = input("Enter Student's Last Name or ZZZ to quit: ")
if last_name == 'ZZZ':
	exit()
gpa = float(input("Enter GPA as float: "))

if gpa >= 3.5:
	print(f"{first_name} {last_name} made the Dean's List")
elif gpa >= 3.25 and gpa < 3.5:
	print(f"{first_name} {last_name} made the Honor Roll")
else:
	print(f"{first_name} {last_name} did not make the Dean's List or Honor Roll")