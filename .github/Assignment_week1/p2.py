
crtpwd = "OpenAI123"
attempt = 0
while attempt < 3:
    pwd = input("Enter the password: ")
    if pwd == crtpwd:
        print("Login Successful")
        break
    else:
        attempt += 1 
if attempt == 3:
    print("Account locked")