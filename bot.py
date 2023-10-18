import nextcord
from nextcord.ext import commands
from nextcord.ext import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from time import sleep

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
    #add job to scheduler to run every 30 seconds, start
    scheduler.add_job(main, 'interval', seconds=5)
    scheduler.start()
    
#run the bot
pandabot.run(token)

