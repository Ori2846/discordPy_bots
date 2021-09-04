import discord
from discord.ext import commands, tasks
from pycoingecko import CoinGeckoAPI
import json
from bs4 import BeautifulSoup
import requests
import json


cg = CoinGeckoAPI()
test = cg.get_price(ids='ethereum', vs_currencies='usd')
url = json.loads(json.dumps(test))
#print(url['ethereum']['usd'])
client = commands.Bot(command_prefix= '.')
# importing the libraries
from bs4 import BeautifulSoup
import requests
price = 1
@client.event
async def on_ready():
    global pricetarget
    global total
    pricetarget = 300
    total = 21297068.75
    await client.change_presence(activity=discord.Game(name="DHO tracking"))
    print('bot is ready')
    global price
    price = 1
    BalanceETH.start()
    BalanceETH2.start()
@tasks.loop(seconds=5)
async def BalanceETH():
    global price
    global pricetarget
    global total
    target_channel_id = '862125499471233024'
    channel = client.get_channel(int(target_channel_id))
    url = "https://api.pancakeswap.info/api/v2/tokens/0x2a5613db7a024eb52392ac87f8a71a28d696940c"
    html_content = requests.get(url).text
    # print(html_content)
    y = json.loads(html_content)
    x = json.dumps(y)
    #print(y["data"]["price"])
    pricenow = float(y["data"]["price"])*float(total)
    print(round(pricenow,30))
    price = float(y["data"]["price"])
    pricetarget2 = float(pricetarget)
    embed = discord.Embed(title="DHO Price", description="https://poocoin.app/tokens/0x2a5613db7a024eb52392ac87f8a71a28d696940c")
    embed.add_field(name="Price", value=y["data"]["price"], inline=False)
    embed.add_field(name="Total Owned DHO", value=total, inline=False)
    embed.add_field(name="Total Owned DHO converted to USD", value=pricenow, inline=False)
    embed.add_field(name="PriceTargetSet?", value=pricetarget, inline=False)
    if pricenow > pricetarget2:
        embed.add_field(name="Price surpass TargetPrice?", value="OUI SELL SELL SELL", inline=False)
        target_channel_id2 = '862464053049163848'
        channel2 = client.get_channel(int(target_channel_id2))
        await channel2.send("Price has surpassed " + str(pricetarget2) + " Sell now @everyone . Current DHO-USD " + str(pricenow))
    else:
        embed.add_field(name="Price surpass TargetPrice?", value="Non", inline=False)
    msg = await channel.send(embed=embed)
@tasks.loop(seconds=4)
async def BalanceETH2():
    global price
    global pricetarget
    global total
    target_channel_id = '863644535002497045'
    channel = client.get_channel(int(target_channel_id))
    url = "https://api.pancakeswap.info/api/v2/tokens/0x2a5613db7a024eb52392ac87f8a71a28d696940c"
    await channel.purge(limit=1)
    html_content = requests.get(url).text
    # print(html_content)
    y = json.loads(html_content)
    x = json.dumps(y)
    #print(y["data"]["price"])
    pricenow = float(y["data"]["price"])*float(total)
    print(round(pricenow,30))
    price = float(y["data"]["price"])
    pricetarget2 = float(pricetarget)
    embed = discord.Embed(title="DHO Price", description="https://poocoin.app/tokens/0x2a5613db7a024eb52392ac87f8a71a28d696940c")
    embed.add_field(name="Price", value=y["data"]["price"], inline=False)
    embed.add_field(name="Total Owned DHO", value=total, inline=False)
    embed.add_field(name="Total Owned DHO converted to USD", value=pricenow, inline=False)
    embed.add_field(name="PriceTargetSet?", value=pricetarget, inline=False)
    if pricenow > pricetarget2:
        embed.add_field(name="Price surpass TargetPrice?", value="OUI SELL SELL SELL", inline=False)
        target_channel_id2 = '862464053049163848'
        channel2 = client.get_channel(int(target_channel_id2))
        await channel2.send("Price has surpassed " + str(pricetarget2) + " Sell now @everyone . Current DHO-USD " + str(pricenow))
    else:
        embed.add_field(name="Price surpass TargetPrice?", value="Non", inline=False)
    msg = await channel.send(embed=embed)
@client.command()
async def test(ctx):
    await ctx.send("Converted to USD : " + str(url['ethereum']['usd']))
@client.command()
async def pricetarget(ctx, arg):
    global pricetarget
    target_channel_id = '862125499471233024'
    channel = client.get_channel(int(target_channel_id))
    pricetarget = arg
    print(pricetarget)
    await ctx.send("Price Target has been set to " + pricetarget )
@client.command()
async def dhoowned(ctx, arg):
    global total
    target_channel_id = '862125499471233024'
    channel = client.get_channel(int(target_channel_id))
    total = arg
    print(pricetarget)
    await ctx.send("Total DHO owned has been set to " + total )
@client.command()
async def support(ctx):
    await ctx.send(".pricetarget to set Price Alerts")
    await ctx.send(".dhoowned to set Amount of DHO owned")
client.run('KEY')