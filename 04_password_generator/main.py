# Predefined length password

# import random
# import string

# # Step 1: Define all characters
# letters = string.ascii_letters  # a-z and A-Z
# digits = string.digits          # 0-9
# symbols = string.punctuation    # Special characters like !@#$%^&*

# # Step 2: Combine them
# all_chars = letters + digits + symbols

# # Step 3: Set password length
# password_length = 12

# # Step 4: Generate password
# password = ''.join(random.choice(all_chars) for _ in range(password_length))

# print("Generated Password:", password)


# Custom length password

# import random
# import string

# letters = string.ascii_letters
# numbers = string.digits
# punchuations = string.punctuation
# all_charac = letters + numbers + punchuations

# def generate():
#     n=int(input("enter the length of your password, "))
#     a= input("press enter to generate password or any other key to exit: ")
#     if a=="":
#         print(''.join(random.choice(all_charac) for _ in range(n)))
#         generate()
#     elif a != "":
#         print("thanks for using me")

# generate()
