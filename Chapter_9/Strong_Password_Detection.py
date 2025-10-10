import re

def validate_password(password):
    checks = 0

    if re.search(r'^.{8,}$', password):
        checks += 1
    else:
        print("Password must be at least 8 characters long.")
        return

    if re.search(r'^(?=.*[a-z])(?=.*[A-Z]).+$', password):
        checks += 1
    else:
        print("Password must contain both uppercase and lowercase letters.")
        return

    if re.search(r'.*\d.*', password):
        checks += 1
    else:
        print("Password must contain at least one digit.")
        return

    if checks == 3:
        print("This is a valid password!")

user_password = "12347799nFyu"
validate_password(user_password)

