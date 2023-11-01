##########################################################################
# Bot for The LATech Esports Center
# Made By: Nicholas Cervantes
# Built in tandem with: esports.py                                                       
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

import nextcord
from nextcord.ext import commands
from nextcord.ext import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from time import sleep
import hashlib

#read the bot token from a file to keep code open source

try:
    with open("token.txt", "r") as f:
            token = f.read()
except:
    print("Please create a file called token.txt and put your bot token in it.")
    sleep(5)
    exit()

#setup the bot and scheduler
scheduler = AsyncIOScheduler()
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

#set the bot's activity to "Powering up..."
activity = nextcord.Activity(type=nextcord.ActivityType.playing, name="Powering up...")

authorizedusers = ['70d75bd53bf1ca47162ec61db050dc370c5148975b9ec77410bc8a3cdff7ca21', 'dd958c4b23f9882abdbf8455b87db9772b320b5277c6d41ec5065d1cc257a1db', '2bb013f17da2a4a11a91cb7cc653a7bc11b9175108b8e8e1facc9f0b9253e4a0', 'd57f87c3e937f0864d898bbe64c78cc2e6eefac470eaca213c81a4ec78ff4b51', '722b9662ce4c60c5f0dd4acf9a9ef8fe13eea6c9b1eba8c76b593720e5755a73']


def channelcheck(mssg):
    mssg = str(mssg)
    varlist = mssg.split(" ")
    if varlist[0] == "Direct" and varlist[1] == "Message":
        return True
    else:
        return False

def isofficer(name):
    hashedname = hashlib.sha256(name.encode()).hexdigest()
    if hashedname in authorizedusers:
        return True
    else:
        return False



async def main():
    #read num.txt and assign it to a counter variable
    with open("num.txt", "r") as f:
        counter = f.read()


    with open("offset.txt", "r") as f:
        offset = f.read()
        
    count = int(counter) - int(offset)
    
    #set the bot's current activity to "with {counter} in the center!"
    activity = nextcord.Activity(type=nextcord.ActivityType.playing, name=f"with {count} in the center!")
    await pandabot.change_presence(activity=activity)

#final init for the bot, will now refer to it as pandabot
pandabot = commands.Bot(command_prefix='!', intents=intents, activity=activity)

#when the bot is ready, start the scheduler
@pandabot.event
async def on_ready():
    #add job to scheduler to run every 30 seconds
    scheduler.add_job(main, 'interval', seconds=30)
    scheduler.start()

#when the bot receives a message
@pandabot.event
async def on_message(message):
    try:
        ifdm = channelcheck(message.channel)
        if(ifdm == True and message.author != pandabot.user and isofficer(message.author.name) == True):
            mssg = str(message.content)
            #test if the message is a integer
            if(mssg.isnumeric()):
                mint = int(mssg)
                with open("num.txt", "r") as f:
                    counter = f.read()
                offset = int(counter) - mint
                with open("offset.txt", "w") as f:
                    f.write(str(offset))
                await message.channel.send("Offset set! :3")
            else:
                await message.channel.send("Hello Mr Admin! To change the number of people in the center just send me a number and ill take care of the rest :3")

        elif(ifdm == True and message.author != pandabot.user):
            await message.add_reaction("🐼")
            await message.channel.send("Hi! Idk why you are DMing me as I'm currently busy keeping track of the people logging in and out of the center :3")


    except:
        print("error")
    
#run the bot
pandabot.run(token)

