import random, pyperclip, webbrowser, json, sys

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_']
passwords = {}

def escape():
    with open("data.json", "w") as data:
        res = json.dumps(passwords)
        data.write(res)
    print("Everything's saved!")
    # exit()
    sys.exit()

def generate():
    password = ''
    random.shuffle(chars)
    for i in range(15):
        password += random.choice(chars)
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password
        
def guide_tour():
    print()
    print()
    print("  This program can save and generate password for different websites.")
    print("  Press escape to save all changes and exit.")
    print()
    print("  Commands:")
    print("  help            outputs this message")
    print("  generate        generates a password")
    print("  add             asks the resource's name and data and remembers them")
    print("  get             asks resource's name and outputs saved password")
    print("  print           outputs all saved resources with passwords")
    print("  open            asks for a website's URL and opens it")
    print("  clear           removes all saved passwords")
    print("  remove          removes saved password")
    print("  exit            saves everything and exits")
    print()

def get():
    website = input("  Which website's data do you want to get?: ")
    try:
        print("  Login: " + passwords[website][0])
        print("  Password: " + passwords[website][1])
    except KeyError:
        print(f"  You didn't save any passwords for {website}")

def add():
    website = input("  Type the website you want to save the password for: ")
    login = input("  Input your login (username): ")
    password = input("  Input your password: ")
    passwords[website] = [login, password]

def edit():
    website = input(" Which website's password do you want to change?: ")
    try:
        check = passwords[website]
    except KeyError:
        print("  You don't have a saved password for this website")
        return
    password = input("  Which password do you want to set for this website?: ")
    if password == "":
        print("  Password can't be empty")
    else:
        passwords[website] = password

def sign_up():
    print("You are new to PasswordKeeper, so you need to create an account.")
    print("This version of PasswordKeeper works with only one user, so you only need to create a password that would be asked when you log in")
    key = input("Input your password: ")
    key2 = input("Confirm your password: ")
    if key == key2:
        pass
    else:
        print("Your passwords do noot match. Try again.")
    while key != key2:
        key = input("Input your password: ")
        key2 = input("Confirm your password: ")
    print("Success!")
    with open("data.json", "w") as js:
        print("Your account is initialized")
    return key

def remove():
    website = input("  Password for which sebsite you want to delete?: ")
    try:
        del passwords[website]
    except KeyError:
        print(f"  Wrong URL or the password for {website} isn't saved. Try again, please")


acess = True
print("Welcome to the PasswordKeeper!")
print("Do you need an overview? y/n: ", end="")
ans = input()
ans.lower()
match ans:
    case "y":
        guide_tour()
    case "n":
        print("You can always return to the overview by typing help")
try:
    with open("data.txt", "r") as data_file:
        content = data_file.read()
except FileExistsError:
    password = sign_up()
    with open("data.txt", "w") as new_data_file:
        new_data_file.write(password)
except FileNotFoundError:
    password = sign_up()
    with open("data.txt", "w") as new_data_file:
        new_data_file.write(password)
else:
    password = input("Enter your password: ")
    if content != password:
        print(f"Wrong password. You have 2 more tries")
        password = input("Enter your password: ")
        if content != password:
            print(f"Wrong password. You have 1 more try")
            password = input("Enter your password: ")
            if content != password:
                print(f"Wrong password. Sorry, but you can't acess this data without password")
                acess = False
    with open("data.json", "r") as data:
        res = data.read()
        if not res == "":
            passwords = json.loads(res)
if acess:
    print("> ", end="")
    while True:
        command = input().lower()
        match command:
            case "help":
                guide_tour()
            case "remove":
                remove()
            case "clear":
                do = input("  Are you sure you want to delete all saved passwords? y/n: ").lower()
                if do == "y":
                    passwords = {}
            case "exit":
                escape()
            case "generate":
                res = generate()
                print(f"  Your password is: {res}")
                cp = input("  Do you want to copy it to clipboard? y/n: ").lower()
                if cp == 'y':
                    pyperclip.copy(res)
                    print("  Successfully copied!")
            case "get":
                get()
            case "open":
                url = input("  What website do you want to open?: ")
                webbrowser.open(url=url, new = 1)
            case "add":
                add()
            case "print":
                if passwords == {}:
                    print("  You didn't save any passwords")
                for i in passwords:
                    print("  ", end="")
                    print(i, end="       ")
                    print(passwords[i][0], end="       ")
                    print(passwords[i][1])
            case _:
                print("  Unknown command. Try again")
        print("> ", end="")
