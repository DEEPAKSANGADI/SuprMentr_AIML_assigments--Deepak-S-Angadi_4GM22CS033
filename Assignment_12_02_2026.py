name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 13:
    category = "child"
elif age < 18:
    category = "teenager"
elif age < 65:
    category = "adult"
else:
    category = "senior"

print(f"Hello {name}! You are a {category} who enjoys {hobby}.")