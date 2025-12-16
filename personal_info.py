# Personal Information Manager

# Static information
name = "Sanjyoti Patil"
age = 23
city = "Pune"
hobby = "Cooking"

# Input from user with validation
favorite_food = input("Enter your favorite food: ").strip()
if favorite_food == "":
    favorite_food = "Not Provided"

favorite_color = input("Enter your favorite color: ").strip()
if favorite_color == "":
    favorite_color = "Not Provided"

# Age calculation
age_in_months = age * 12

# Display formatted output
print("\n" + "=" * 35)
print("      PERSONAL INFORMATION")
print("=" * 35)
print(f"Name          : {name}")
print(f"Age           : {age} ({age_in_months} months old)")
print(f"City          : {city}")
print(f"Hobby         : {hobby}")
print(f"Favorite Food : {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print("=" * 35)
print("Thank you for using the program!")