sf = open("./Users/bleuos_administrator/userconfig/UserSettings.bconfig", "r")

#print(sf.read())

settings_dict = []
def get_setting():
    print("Current Settings:")
    for i in sf:
        print(i.split(":")[0],":", i.split(":")[1].strip())
        
def app():
    while True:
        command = input("System_Settings ~ ")
        if command == "/ds":
            get_setting()
        if command == "/q":
            break


