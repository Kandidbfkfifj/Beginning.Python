print("Welcome to my tool!")
print("This tool generates random passwords for you.")
print("do you wanna start the tool? (yes/no)")
user_input = input().strip().lower()
if user_input != "yes":
    print("Exiting the tool. Goodbye from @ilvy!")
else:
    print("starting the tool...")
    import random
    import string
    def generate_password(length=12):
        """Generate a random password."""
        charachters = string.ascii_letters + string.digits + string.punctuation
        password="".join(random.choice(charachters) for i in range(length))
        return password
    print("your password is:", generate_password())
    print("Goodbye from @ilvy!")
    
