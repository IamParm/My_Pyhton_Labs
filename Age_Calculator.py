#getting inputs for name and age
name = input("What is your name? ")
birth_Year = input("What is your birth year? ")

#Importing datetime to calculate the age
from datetime import datetime
current_year = datetime.now().year
age = current_year - int(birth_Year)

#greeting with name and age and saying goodbye!
print(f"Hello {name}")
print(f"You must be {age} years old.")
print("Goodbye!")