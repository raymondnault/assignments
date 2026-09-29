'''

Raymond Nault
Chapter 5: If Statements

'''

# this program will check if there are any users and print a message if the list is empty

usernames = []
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello (username), thank you for logging in again.")

if not usernames:
    print("We need to find some users!")