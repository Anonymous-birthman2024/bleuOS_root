import SystemSettings

# define openall (bootstrap)

def openall():
    accounts = open("/Users/tomli/bleuOS_root/accounts.busrpck", "r").read()
    return accounts

# define login (/lg)
def login():
    userlist = openall()
    userlist = userlist.split(":")
    return userlist[0]

# define go to app (/cda)

def cda():
    SystemSettings.app()

# define cd (/cd)

# define ls (/ls)

# define install (/bs <website of binary install script> <install path> as <name>)

def bleuOS_PATH():
    openall()
    while True:
        command = input("bleuos_root ~ ")
        if command == "/lg":
            print(login())
        if command == "/cda SystemSettings":
            cda()

bleuOS_PATH()