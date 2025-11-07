correct_password = "56734" 

print("Hello! This program will ask you for the password.")
print("Type the password and press Enter. I'll let you know when it's right.\n")

while True:
    user_input = input("Please enter the password: ").strip()

    if user_input == correct_password:
      print("\n Access granted — welcome! You entered the correct password.")
      break
    else:
       print(" That's not the correct password. No worries — try again.\n")
