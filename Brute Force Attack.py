correct_password = 12345
allowed_attemps = 5
attempts = 0
while attempts < allowed_attemps:
    entered_password = int(input("Please enter your password: "))
    if entered_password == correct_password:
        print("Access has been granted!")
        break
    else:
        attempts += 1
        remaining_attemps = allowed_attemps - attempts

        if remaining_attemps > 0:
            print(f"Incorrect password. You have {remaining_attemps} attempts left.")
        else:
            print("You have been reached the maximum number of attempts. Try again later!")
            break 