'''

Raymond Nault
Chapter 5: If Statements

'''

# this program will list usernames and greet the admin if present

usernames = ['admin', 'ray', 'john', 'bob']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello {}, thank you for logging in again.".format(username))