import random

# Define character sets
capchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spchar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', ',', '.']
smallchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user input for password parameters
passlen = int(input("Enter the desired length of password: "))
capans = str(input("Are CAPITAL Alphabets allowed? (Y/N): "))
smallans = str(input("Are lowercase Alphabets allowed? (Y/N): "))
digans = str(input("Are Digits allowed? (Y/N): "))
spans = str(input("Are Special Characters allowed? (Y/N): "))

print("Way 1 is meant for Minimal Resource Usage and Way 2 for more secure generation.")
rep = input("Way 1 or Way 2? (1/2): ")

# Format user input
capans, smallans, digans, spans = capans.title(), smallans.title(), digans.title(), spans.title()

# Validate user input
if not (capans == 'Y' or capans == 'N') or not (smallans == 'Y' or smallans == 'N') or not (digans == 'Y' or digans == 'N') or not (spans == 'Y' or spans == 'N'):
    print("Invalid input. Please enter 'Y' or 'N' for each question.")
    quit()

# Combine character sets based on user input
comblis = []
comblis.extend(capchar) if capans == 'Y' else None
comblis.extend(dig) if digans == 'Y' else None
comblis.extend(spchar) if spans == 'Y' else None
comblis.extend(smallchar) if smallans == 'Y' else None

# Check if any character set is allowed
if not comblis:
    print("Error, You denied the usage of all possible characters.")
    quit()

# Generate password
password = ""
if rep == '1':
    for _ in range(passlen):
        password += random.choice(comblis)
else:
    random.shuffle(comblis)
    password = ''.join(random.sample(comblis, passlen))

# Display generated password
print("\nGenerated Password is:", password)