##########################################################################
# Login System for The LATech Esports Center
# Made By: Nicholas Cervantes
# Version 1.4.0                                                       
#                                 WNXXXNW                              
#                              W0xollccloxONNXK000KXNW                 
#                             Xo;;;::;;;;,:dkkkkOOkkkkkOKW WX000KNW    
#                            No',,,,,'':oOXW         WXOkxoc::;;:cd0W  
#                            Nc..''',ckN                 Nkc,,,;;;;;xN 
#                            Wk'..,xKN                     Nx;',,,,';O 
#                             Nx';0      NKOOO0NW           W0;.'''.'k 
#                  WXXXNW      Oo0     Nkl;,,,;lOW   WKOkO0NW O,....lX 
#               W0o:;;;:cldkKWNodW    Xo;,,..',;xN  Nx:,',;cxXNo..;dX  
#               K;.',,,,,,'';cc;xW   Wk;,,,'';d0NW  Nk:...,,;dXk:dX    
#               Xl..'',,,,,,,,.'dKW  Wk:,,,,cOWM0c:dXWO:'',,,:OkoK     
#                Xo'..'',,,,,,''lO0NWWNkl:;cOWMM0:'oX No;,,,,ckdoN     
#                 W0o;...''',,,.,dkOO0XXXKKXWMMMMNNWMMWk:,,;:dxckW     
#                    Xkl;.....''.,lkkkkO0KXXNNWWWWWMMMWXOdooxxcdN      
#                      WXko;...''..,:ldkkkkkOOO000000000OOkko,:K       
#                          NOdc;'.....;cllodxkkkkkkkkkkkxoc;...cOW     
#                             WXd;ckkOOkdollllllllll:::;,''','..'oX    
#                               koX   WWWNNXKOkxddddc,,;,,,,,,'...:0W  
#                              WddW          WNK0Okkkd:;;;,,,,,,'..,OW 
#                              Ndx              WNXK00kl;;;;,,,,,'..,OW
#                              Xok                  WWNX0l,;;;,,,,'..:K
#                              Xok                      Wdcoc;;;,,,'.'x
#                              Ndx                      WddNXkl;;;,'.,O
#                              WdxW                     XclX  N0xolco0W
#                               xlONWWWNXXXXNNNNXXKK0kddc',O      WW   
#                               O;,cool:clodxxxxdol:,..,,,'lN          
#                               Xc.,,,,,...;dxxxxkd,..',,,';0          
#                                k'',,,,'.,O       Kc..',,''k          
#                                No......'xW        No'....,0          
#                                 Nd:,''cOW          W0o:;cOW          
#                                  WNKkON               WNW            
##########################################################################

#Import Statements
from time import sleep
from datetime import datetime
import csv
import os
import hashlib

#Initialization
#Collect Date and Time and attempt to create a log folder if one does not already exist
starttime = datetime.now()
starttime = datetime.isoformat(starttime)
try:
    os.mkdir("./logs")
except:
    pass

#init message of the day
global motd
motd = ""

try:
    #attempt to adjust the window
    import keyboard
    #attempt to go fullscreen
    keyboard.press('f11')
    keyboard.release('f11')
    #attempt to zoom in and make text bigger
    keyboard.press('ctrl')
    x = 0
    while x<7:
        keyboard.press_and_release('=')
        x+=1
    keyboard.release('ctrl')
except:
    pass

#Create a log dictionary and a csv file to store the log
logdict = [{"id": "000000", "timein": "2020-02-20T12:00:00.000000", "timeout": "2020-02-20T12:00:00.000000"}]
field_names = ["id", "timein", "timeout"]
csvfilename = starttime+"-log.csv"
csvfilename = csvfilename.replace(":", "")
csvfilename = "./logs/"+csvfilename
csvfile = open(csvfilename, "w")
csvfile.close()

#Create file to store the number of users logged in
with open("num.txt", "w") as f:
    f.write("0")

#Function to log hours, VERY VERY concatenated to save space/time, but it works (we love python formatting)
def loghours(id):
    x = datetime.now() 
    x = datetime.isoformat(x)

    for i in logdict:
        if i["id"] == id:
            if i["timeout"] == None:
                i["timeout"] = x
                print()
                print("User " + id+ " has been signed out")
                return

    newsignin = {"id": id, "timein": x, "timeout": None}
    print("User " + id+ " has been signed in")
    logdict.append(newsignin)
    return

#Function to check if the user is an admin
def isadmin(id):
    hashedid = hashlib.sha256(id.encode()).hexdigest()
    #decided to hash username in order to keep code open source
    if hashedid == "833d901914bf64233123da87293334038255e7979b1b44b714df76bef7d343b4":
        try:
            os.system('cls')
            print("Please enter the admin password:")
            print()
            password = input()
            hashed = hashlib.sha256(password.encode()).hexdigest()
            #decided to hash password in order to keep code open source
            if hashed == "68b80a63282e38aae95af553cf7f8dada06d627f9eed3b59976b79401207b287":
                return True
            else:
                raise Exception("Invalid Password")
        except Exception as e:
            return False
    else:
        return False
    
#Function to display the admin menu
def adminmenu():
    os.system('cls')
    print("Welcome to the Admin Menu!")
    print("______________________________")
    print("Please select an option:")
    print("1. View Log")
    print("2. Change MOTD")
    print("3. View Number of Users")
    print("4. Exit")
    print()
    print("Enter the number of the option you would like to select and press Enter:")
    print()
    option = input()
    if option == "1":
        viewlogs()
    elif option == "2":
        changemotd()
    elif option == "3":
        viewnums()
    elif option == "4":
        return
    else:
        print("Invalid Option, please try again")
        sleep(1)
        adminmenu()
    
#Function to view the number of users logged in
def viewnums():
    os.system('cls')
    print("Number of users logged in: ")
    print()
    currcounter = 0
    overcounter = 0
    for i in logdict:
        if i["timeout"] == None:
            currcounter += 1
        overcounter += 1
    print(f"Current: {currcounter}, Overall: {overcounter}")
    print()
    print("Press 'Enter' to return to the Admin Menu")
    input()
    adminmenu()

#Function to view the logs
def viewlogs():
    os.system('cls')
    print(logdict)
    print()
    print("Press 'Enter' to return to the Admin Menu")
    input()
    adminmenu()

#Function to change the MOTD
def changemotd():
    os.system('cls')
    print("Please type the new MOTD and press 'Enter'")
    print("OR")
    print("Just press 'Enter' remove MOTD")
    print()
    global motd 
    motd = input("MOTD: ")
    adminmenu()

#Function to view the number of users logged in, but truncated to not show anything on the screen
def viewnumssmol():
    currcounter = 0
    for i in logdict:
        if i["timeout"] == None:
            currcounter += 1

    return currcounter

#checks to see if message is valid ID
def isid(id):
    try:
        if len(id) != 6:
            raise Exception("Invalid ID Length")
        counter = 0
        for i in id:
            if counter < 3:
                if not i.isalpha():
                    raise Exception("Invalid ID Alpha")
            if counter >=3:
                if not i.isdigit():
                    raise Exception("Invalid ID Num")
            counter += 1
        return True
            
    except Exception as e:
        return False
    

#Main Loop
os.startfile("bot.exe")

while(True):
    os.system('cls')
    print("Welcome to the LA Tech Esports Center!")
    if motd != "":
        print("MOTD: " + motd)
    print("______________________________")
    print()
    print("Please Enter Your Tech/Moodle Login (abc123) and press 'Enter':")
    print()
    id = input()
    print()
    os.system('cls')

    if(isid(id) == True):
        loghours(id)
        csvfile = open(csvfilename, "w",newline='')
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(logdict)
        csvfile.close()
        print()
        print("Thank you for using the esports Center!")

        #update the number of users logged in for the discord bot
        x = viewnumssmol()
        with open("num.txt", "w") as f:
            f.write(str(x))

    elif(isadmin(id) == True):
        adminmenu()
    else:
        print("Invalid ID, please try again")
        continue

    sleep(1)

# You like looking at code, don't you?

#⠀⢸⠂⠀⠀⠀⠘⣧⠀⠀⣟⠛⠲⢤⡀⠀⠀⣰⠏⠀⠀⠀⠀⠀⢹⡀
#⠀⡿⠀⠀⠀⠀⠀⠈⢷⡀⢻⡀⠀⠀⠙⢦⣰⠏⠀⠀⠀⠀⠀⠀⢸⠀
#⠀⡇⠀⠀⠀⠀⠀⠀⢀⣻⠞⠛⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠀⢸⠀
# ⡇⠀⠀⠀⠀⠀⠀⠛⠓⠒⠓⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
#⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀
#⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⢀⡟⠀
#⠀⠘⣇⠀⠘⣿⠋⢹⠛⣿⡇⠀⠀⠀⠀⣿⣿⡇⠀⢳⠉⠀⣠⡾⠁⠀
#⣦⣤⣽⣆⢀⡇⠀⢸⡇⣾⡇⠀⠀⠀⠀⣿⣿⡷⠀⢸⡇⠐⠛⠛⣿⠀
#⠹⣦⠀⠀⠸⡇⠀⠸⣿⡿⠁⢀⡀⠀⠀⠿⠿⠃⠀⢸⠇⠀⢀⡾⠁⠀
#⠀⠈⡿⢠⢶⣡⡄⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⣴⣧⠆⠀⢻⡄⠀⠀
#⠀⢸⠃⠀⠘⠉⠀⠀⠀⠠⣄⡴⠲⠶⠴⠃⠀⠀⠀⠉⡀⠀⠀⢻⡄⠀
#⠀⠘⠒⠒⠻⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠞⠛⠒⠛⠋⠁⠀
#⠀⠀⠀⠀⠀⠀⠸⣟⠓⠒⠂⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⣼⣃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠉⣹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀
