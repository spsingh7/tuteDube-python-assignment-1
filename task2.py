def get_name_part(part):
    while True:
        name = input(f"Enter your {part} name: ").strip()
        if name.isalpha():
            return name.capitalize()
        else:
            print(f"Invalid {part} name. Please use alphabetic characters only.")


first_name = get_name_part("first")
last_name = get_name_part("last")

# Step 2: Combine and greet
full_name = f"{first_name} {last_name}"
print(f"\nHello, {full_name}! Welcome to the Python program.")

