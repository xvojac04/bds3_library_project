from passlib.hash import argon2


def hashmypassword(user_password):
    # generate new salt, hash password
    hashed_password = argon2.hash(user_password)
    print(hashed_password)


# MAIN PART OF THIS FUNCTION
user_input = input("Insert your password: ")
hashmypassword(user_input)
