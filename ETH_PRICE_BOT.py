import discord
from discord.ext import commands, tasks
from pycoingecko import CoinGeckoAPI
import json

cg = CoinGeckoAPI()
test = cg.get_price(ids='ethereum', vs_currencies='usd')
url = json.loads(json.dumps(test))
#print(url['ethereum']['usd'])
client = commands.Bot(command_prefix= '.')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="ETH mining"))
    print('bot is ready')
    BalanceETH.start()
@tasks.loop(seconds=120)
async def BalanceETH():
    target_channel_id = '814624508706947083'
    channel = client.get_channel(int(target_channel_id))
    await channel.send("Converted to USD : " + str(url['ethereum']['usd']))
@client.command()
async def test(ctx):
    await ctx.send("Converted to USD : " + str(url['ethereum']['usd']))
client.run('TOKEN')
