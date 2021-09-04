import discord
from discord.utils import get
from discord.ext import commands, tasks
import json
from datetime import datetime
import re
intents = discord.Intents.default()
intents.members = True
BOT_TOKEN = ""
words = ["REDACTED","REDACTEDa", "REDACTEDers", "REDACTEDas"]
client = commands.Bot(intents=intents,command_prefix= '!')
counter = 0
n = 0
#WARNING this bot was created per request of a client. I do not condone the origins of this bot
#nor the words it was initially parsing for. All offensive words have been "REDACTED"
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="redacted"))
    print('Announcement Bot now active and running')
    f = open('CounterBot.json')
    data = json.load(f)
    for i in data:
        print(i)
@client.command()
async def message_count(ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("There were {} messages in {}".format(count, channel.mention))
@client.command()
async def txtChannel(ctx):
    for text_channel in ctx.message.guild.text_channels:
        print(text_channel.id)
@client.command()
async def message(ctx, msgID: int):
    for text_channel in ctx.message.guild.text_channels:
        try:
            msg = await text_channel.fetch_message(msgID)
            then = datetime(msg.created_at.year, msg.created_at.month, msg.created_at.day, msg.created_at.hour, msg.created_at.minute, msg.created_at.second)
            now = datetime.now()  # Now
            duration = now - then  # For build-in functions
            duration_in_s = duration.total_seconds()
            days = divmod(duration_in_s, 86400)  # Get days (without [0]!)
            hours = divmod(days[1], 3600)  # Use remainder of days to calc hours
            minutes = divmod(hours[1], 60)
            c = "{} Days Ago, {} Hours Ago, {} Minutes ago".format(divmod(duration_in_s, 86400)[0]+1 ,divmod(duration_in_s, 3600)[0] + 7,minutes[0]  )
            await ctx.send("Last said {} ".format(c))
            await ctx.send("Located Here {} ".format(msg.jump_url))
        except:
            print("nothing yet")
@client.command()
async def document(ctx, *, id):
    Total_n = 0
    Total_R = 0
    last_message = 0
    AllDates = []
    for text_channel in ctx.message.guild.text_channels:
        n = 0
        R = 0
        channel = client.get_channel(text_channel.id)
        count = 0
        print("Started")
        print(id)
        #async for _ in channel.history(limit=None):
        #    count += 1
        messages = await channel.history(limit=None).flatten()
        for msg in messages:
            for word in words:
                if word in msg.content.lower() and str(msg.author.id) == str(id):
                    b = [msg.id, msg.created_at.year, msg.created_at.month, msg.created_at.day, msg.created_at.hour, msg.created_at.minute, msg.created_at.second]
                    AllDates.append((b))
                    print(b[0])
                    if word == "REDACTEDa":
                        n = n + 1
                        Total_n = Total_n + 1
                    if word == "REDACTEDer":
                        R = R + 1
                        Total_R = Total_R + 1
        await ctx.send("There were {} REDACTED words said in {} || REDACTED(a)(s) **{}** said and REDACTED(er)(s) **{}** said".format(n+R, channel.mention, n, R))
        print("ENDED")
    AllDates.sort()
    print(AllDates)
    try:
        length = len(AllDates) - 1
        print(length)
        last_message = AllDates[length][0]
        await ctx.send("Last REDACTED message ID {}".format(last_message))
    except:
        await ctx.send("No REDACTED words found")
    with open("CounterBot.json", "r") as file:
        data = json.load(file)
        data.update({str(id) + "REDACTEDer": Total_R})
        data.update({str(id) + "REDACTEDa": Total_n})
        data.update({str(id) + "MessageID": last_message})
        x = Total_n + Total_R
        data.update({str(id): x})
        file.seek(0)
    with open("REDACTEDerCounterBot.json", "w") as file:
        json.dump(data, file, sort_keys=True, indent=4)
@client.command()
async def test(ctx):
    Total_n = 0
    Total_R = 0
    for guild in client.guilds:
        for member in guild.members:
            print(member.id)
@client.command()
async def documentall(ctx):
    for guild in client.guilds:
        for member in guild.members:
            last_message = 0
            AllDates = []
            Total_n = 0
            Total_R = 0
            id = member.id
            for text_channel in ctx.message.guild.text_channels:
                n = 0
                R = 0
                channel = client.get_channel(text_channel.id)
                count = 0
                print("Started")
                print(id)
                #async for _ in channel.history(limit=None):
                #    count += 1
                messages = await channel.history(limit=None).flatten()
                for msg in messages:
                    for word in words:
                        if word in msg.content.lower() and str(msg.author.id) == str(id):
                            b = [msg.id, msg.created_at.year, msg.created_at.month, msg.created_at.day,
                                 msg.created_at.hour, msg.created_at.minute, msg.created_at.second]
                            AllDates.append((b))
                            print(b[0])
                            if word == "REDACTEDa":
                                n = n + 1
                                Total_n = Total_n + 1
                            if word == "REDACTEDer":
                                R = R + 1
                                Total_R = Total_R + 1
                await ctx.send("({})There were {} REDACTED words said in {} || REDACTED(a)(s) **{}** said and REDACTED(er)(s) **{}** said".format(id,n+R, channel.mention, n, R))
                print("ENDED")
            AllDates.sort()
            print(AllDates)
            try:
                length = len(AllDates) - 1
                print(length)
                last_message = AllDates[length][0]
                await ctx.send("Last REDACTED message ID {}".format(last_message))
            except:
                await ctx.send("No N words found")
            with open("CounterBot.json", "r") as file:
                data = json.load(file)
                data.update({str(id) + "REDACTEDer": Total_R})
                data.update({str(id) + "REDACTEDa": Total_n})
                x = Total_n + Total_R
                data.update({str(id) + "MessageID": last_message})
                data.update({str(id): x})
                file.seek(0)
            with open("CounterBot.json", "w") as file:
                json.dump(data, file, sort_keys=True, indent=4)

# @client.command()
# async def history(ctx, member: discord.Member):
#     counter2 = 0
#     nR_word_counter = 0
#     nA_word_counter = 0
#     id = member.id
#     async for message in ctx.channel.history(limit = 500):
#         if message.author == member:
#             with open("REDACTEDerCounterBot.json", "r") as file:
#                 data = json.load(file)
#                 result_ = message.content.lower()
#                 print(message.content.lower())
#                 result = result_.split()
#                 nR_word_counter = result.count("REDACTEDer") + nR_word_counter
#                 nA_word_counter = result.count("REDACTEDa") + nA_word_counter
#                 if str(id) in data:
#                     data.update({str(id) + "REDACTEDer": nR_word_counter + data[str(id)+"REDACTEDer"]})
#                     data.update({str(id) + "REDACTEDa": nA_word_counter + data[str(id)+"REDACTEDa"]})
#                     Total_NA_NR = nA_word_counter + nR_word_counter
#                     data.update({str(id): Total_NA_NR + data[str(id)]})
#                 elif str(id) not in data:
#                     data.update({str(id) + "REDACTEDer": nR_word_counter})
#                     data.update({str(id) + "REDACTEDa": nA_word_counter})
#                     Total_NA_NR = nA_word_counter + nR_word_counter
#                     data.update({str(id): Total_NA_NR})
#                 file.seek(0)
#             with open("REDACTEDerCounterBot.json", "w") as file:
#                 json.dump(data, file)
#             counter2 += 1
#     await ctx.send(f'{member.mention} ID: **{member.id}** has sent **{nR_word_counter}**  Hard Rs and **{nA_word_counter}** Easy As')

@client.command(pass_context=True)
async def counter(ctx,user):
    Level = 0
    print(user)
    inp_str = user
    num = ""
    for c in inp_str:
        if c.isdigit():
            num = num + c
    f = open('REDACTEDerCounterBot.json')
    data = json.load(f)
    print(data[num])
    user_ = await ctx.author.guild.fetch_member(num)
    print(user_)
    total = data[num+"REDACTEDer"] + data[num+"REDACTEDa"]
    embed = discord.Embed(title=str(user_)+" has used the REDACTED Word " + str(total) + " times")
    embed.add_field(name="🦍 REDACTED 🦍", value=str(data[num+"REDACTEDer"]), inline=True)
    embed.add_field(name="🐒 REDACTED 🐒", value=str(data[num+"REDACTEDa"]), inline=True)
    Levels = ["REDACTED", "REDACTED", "REDACTED", "REDACTED", "REDACTED", "REDACTED", "REDACTED"]
    if total > 80:
        Level = Levels[6]
    if total <= 80 and total > 65:
        Level = Levels[5]
    if total <= 65 and total > 40:
        Level = Levels[4]
    if total <= 40 and total > 30:
        Level = Levels[3]
    if total <= 30 and total > 20:
        Level = Levels[2]
    if total <= 20 and total > 10:
        Level = Levels[1]
    if total <= 10:
        Level = Levels[0]
    for text_channel in ctx.message.guild.text_channels:
        try:
            msg = await text_channel.fetch_message(data[num + "MessageID"])
            then = datetime(msg.created_at.year, msg.created_at.month, msg.created_at.day, msg.created_at.hour, msg.created_at.minute, msg.created_at.second)
            now = datetime.now()  # Now
            duration = now - then  # For build-in functions
            duration_in_s = duration.total_seconds()
            days = divmod(duration_in_s, 86400)  # Get days (without [0]!)
            hours = divmod(days[1], 3600)  # Use remainder of days to calc hours
            minutes = divmod(hours[1], 60)
            c = "{} Days Ago, {} Hours Ago, {} Minutes ago".format(divmod(duration_in_s, 86400)[0]+1 ,divmod(duration_in_s, 3600)[0] + 7,minutes[0]  )
        except:
            print("nothing yet")
    embed.add_field(name="REDACTED Level:", value=Level, inline=False)
    try:
        if c == ">":
            print("var")
        else:
            embed.add_field(name="Last Said:", value=c, inline=False)
        embed.add_field(name="Here:", value=msg.jump_url, inline=False)
    except:
        print("no n words found")
    await ctx.send(embed=embed)
@client.event
async def on_message(ctx):
    counter = 0
    for word in words:
        if word in ctx.content.lower():
            print(ctx.content.lower())
            counter = counter + 1
            id = ctx.author.id
            f = open('CounterBot.json')
            data = json.load(f)
            if str(id) in data and counter <= 1:
                print(str(id) + " is already in data.json")
                with open("CounterBot.json", "r") as file:
                    data = json.load(file)
                    result_ = ctx.content.lower()
                    result = result_.split()
                    y = data[str(id)+"REDACTEDer"] + result.count("REDACTEDer") + result.count("REDACTEDers")
                    data.update({str(id)+"REDACTEDer": y})
                    z = (data[str(id)+"REDACTEDa"] +(result.count("REDACTEDa"))) + result.count("REDACTEDas")
                    data.update({str(id)+"REDACTEDa": z})
                    x = (data[str(id)+"REDACTEDa"] + data[str(id)+"REDACTEDer"]) + result.count("REDACTEDas") + result.count("REDACTEDers")
                    data.update({str(id) + "MessageID": ctx.id})
                    data.update({str(id):x})
                    file.seek(0)
                with open("CounterBot.json", "w") as file:
                    json.dump(data, file, sort_keys=True, indent=4)
            elif counter <= 1 and str(id) not in data:
                with open("CounterBot.json", "r") as file:
                    data = json.load(file)
                    result = ctx.content.split()
                    data.update({str(id)+"REDACTEDer": (result.count("REDACTEDer") + result.count("REDACTEDers"))})
                    data.update({str(id)+"REDACTEDa": (result.count("REDACTEDa") + result.count("REDACTEDas"))})
                    x = result.count("REDACTEDa") + result.count("REDACTEDer") + result.count("REDACTEDers") + result.count("REDACTEDas")
                    data.update({str(id):"var"})
                    data.update({str(id) + "MessageID": ctx.id})
                    file.seek(0)
                with open("CounterBot.json", "w") as file:
                    json.dump(data, file, sort_keys=True, indent=4)
    await client.process_commands(ctx)



client.run(BOT_TOKEN)
