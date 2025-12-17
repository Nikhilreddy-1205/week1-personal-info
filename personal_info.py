print("hello world")
print("this is nikhil reddy")
print("    PERSONAL INFORMATION MANAGER")

print()
name = "nikhil"
age = 21      
city = "Bengaluru"
print("basic information:")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print()

favourite_food=input("enter your favourite food?")
while favourite_food=="":
    print("emter your favourite-food")
    favourite_food=input("enter your favourite food?")


favourite_place=input("enter favourite_place?")
while favourite_place=="":
    print("enter the place")
    favourite_place=input("enter favourite_place?")

age_in_months = age * 12

print("\nYour information:")
print("----------------------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Favourite food: {favourite_food}")
print(f"Favourite place: {favourite_place}")
