import discord
from discord.ext import commands, tasks
import json

Admins = ["replacethiswithyour user#1234"]
BOT_TOKEN = ""
#This bot sends announcement messages throughout all servers automatically
#must include a data.json file


client = commands.Bot(command_prefix= '!')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Fiverr"))
    print('Announcement Bot now active and running')
    f = open('data.json')
    data = json.load(f)
    for i in data:
        print(i)
@client.command(pass_context=True)
async def setchannel(ctx):
    if str(ctx.message.author) in Admins:
        id = ctx.message.channel.id
        f = open('data.json')
        data = json.load(f)
        if str(id) in data:
            print(str(id) + " is already in data.json")
            await ctx.send("Channel ID:" + str(id))
            await ctx.send("This Channel has already been added")
        else:
            print("added server id into json")
            with open("data.json", "r+") as file:
                data = json.load(file)
                data.update({id: id})
                file.seek(0)
                json.dump(data, file)
            await ctx.send("Channel ID:" + str(id))
            await ctx.send("This Channel has been added to this bot's Announcements")
    else:
        await ctx.send("error: user permissions")
@client.command(pass_context=True)
async def removechannel(ctx):
    if str(ctx.message.author) in Admins:
        id = ctx.message.channel.id
        try:
            obj = json.load(open("data.json"))
            for i in obj:
                if obj[i] == str(id):
                    obj.pop(i)
                    break
            del obj[str(id)]
            open("data.json", "w").write(
                json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
            )
            print("removed data")
            await ctx.send("Successfully removed channel from database")
        except:
            await ctx.send("Error Unable to remove channel from database")
    else:
        await ctx.send("error: user permissions")
@client.command()
async def send(ctx,text):
    if str(ctx.message.author) in Admins:
        f = open('data.json')
        data = json.load(f)
        try:
            for i in data:
                channel = client.get_channel(int(i))
                await channel.send(text)
        except:
            await ctx.send("error")
    else:
        await ctx.send("error: user permissions")
client.run(BOT_TOKEN)
