'''
Todd Hamm
SDEV 220
6-27-2026
m03-lab.py

Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
year
make
model
doors (2 or 4)
roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof

Variables: 
@ vehicle_type
@ year
@ make
@ model
@ doors
@ roof
'''

# super class Vehicle
class Vehicle:
	def __init__(self, vehicle_type):
		self.vehicle_type = vehicle_type

# child class Automobile that inherits Vehicle
class Automobile(Vehicle):
	def __init__(self, vehicle_type, year, make, model, doors, roof):
		# set the vehicle type of the parent class using the super method
		super().__init__(vehicle_type) 

		# set the child class's attributes
		self.year = year
		self.make = make
		self.model = model
		self.doors = doors
		self.roof = roof

# Get user input
user_car = input("Enter vehicle type: ")
car_year = input("Enter vehicle year: ")
car_make = input("Enter vehicle make: ")
car_model = input("Enter vehicle model: ")
car_doors = input("Enter number of doors: ")
car_roof = input("Enter vehicle roof type: ")

# set these values as obj attributes
user_car_obj = Automobile(user_car, car_year, car_make, car_model, car_doors, car_roof)

# output
print(f"Vehicle type: {user_car_obj.vehicle_type}")
print(f"Year: {user_car_obj.year}")
print(f"Make: {user_car_obj.make}")
print(f"Model: {user_car_obj.model}")
print(f"Number of doors: {user_car_obj.doors}")
print(f"Type of roof: {user_car_obj.roof}")