#####################################
# Login System for The LATech Esports Center
# Made By: Nicholas Cervantes
# Version 1.2.1
#####################################

#Import Statements
from time import sleep
from datetime import datetime
import csv
import os

#Initialization
#Collect Date and Time and attempt to create a log folder if one does not already exist
starttime = datetime.now()
starttime = datetime.isoformat(starttime)
try:
    os.mkdir("./logs")
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
while(True):
    os.system('cls')

    print("Welcome to the LA Tech Esports Center!")
    print("______________________________")
    print()
    print("Please Enter Your Tech/Moodle Login (abc123) and press Enter:")
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
    else:
        print("Invalid ID, please try again")
        sleep(1)
        continue

    print()
    print("Thank you for using the esports Center!")
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
