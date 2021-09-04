import discord
from discord.ext import commands, tasks
import random
import flexpoolapi
from flexpoolapi import utils
from pycoingecko import CoinGeckoAPI
import json
import etherscan
from requests_cache import core

es = etherscan.Client(
    api_key='PYV76PGQXWTH44QA65ZKESYVPHAP2CUGQE',
    cache_expire_after=5,
)

eth_price = es.get_eth_price()

eth_supply = es.get_eth_supply()

eth_balance = es.get_eth_balance('0x39eB410144784010b84B076087B073889411F878')

eth_balances = es.get_eth_balances([
    '0x39eB410144784010b84B076087B073889411F878',
    '0x39eB410144784010b84B076087B073889411F879',
])
#ODMwMTQxMTYzMTg4NjUwMDU0.YHCXNA.KbmLr5rWf6VNUN7VQuijkYlRHb8 - ETH bot
miner = flexpoolapi.miner("0x72ab2e10F8694a714c39E26AB313642Fa07b6afC")
cg = CoinGeckoAPI()
print(cg.get_price(ids='ethereum', vs_currencies='usd'))
test = cg.get_price(ids='ethereum', vs_currencies='usd')
url = json.loads(json.dumps(test))
print(url['ethereum']['usd'])
x = miner.estimated_daily_revenue()
print("Round share:", miner.round_share())
print(utils.format_weis(miner.balance()))
import time
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix= '.', intents=intents)
Responses = ["hi"]
Responses_R = len(Responses)
be = 99999
y = 0
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="ETH mining"))
    print('bot is ready')
    BalanceETH.start()
@tasks.loop(seconds=120)
async def BalanceETH():
    global y
    target_channel_id = '830176402950586398'
    channel = client.get_channel(int(target_channel_id))
    cg = CoinGeckoAPI()
    print(cg.get_price(ids='ethereum', vs_currencies='usd'))
    test = cg.get_price(ids='ethereum', vs_currencies='usd')
    url = json.loads(json.dumps(test))
    print(url['ethereum']['usd'])
    x = float(url['ethereum']['usd'])
    y = float(utils.format_weis(miner.balance()).replace('ETH',''))
    bal = str(truncate((y * x),2))
    target_channel_id2 = '831658188318965830'
    channel2 = client.get_channel(int(target_channel_id2))
    gas_price = es.get_gas_price() / 1000000000
    xx = gas_price
    if xx != y:
        await channel2.send(str(xx) + " " + "gwei")
        y = xx
    target_channel_id2 = '831658188318965830'
    target_channel_id3 = '831661886519902220'
    channel2 = client.get_channel(int(target_channel_id2))
    channel3 = client.get_channel(int(target_channel_id3))
    gas_price = es.get_gas_price() / 1000000000
    if xx <= 70:
        await channel3.send("Gwei is less than 70 Gwei! || " + str(xx) + " " + "gwei")
    await channel.send((utils.format_weis(miner.balance())))
    await channel.send("Converted to USD : " + "$"+bal)



@client.command()
async def bal(ctx):
    cg = CoinGeckoAPI()
    print(cg.get_price(ids='ethereum', vs_currencies='usd'))
    test = cg.get_price(ids='ethereum', vs_currencies='usd')
    url = json.loads(json.dumps(test))
    print(url['ethereum']['usd'])
    x = float(url['ethereum']['usd'])
    y = float(utils.format_weis(miner.balance()).replace('ETH',''))
    bal = str(truncate((y * x),2))
    await ctx.send((utils.format_weis(miner.balance())))
    await ctx.send("Converted to USD : " + "$"+bal)

            #def check(m):
            #return m.content == 'hello' and m.channel == channel
            #msg = await client.wait_for('message', check=check)
            #await channel.send('Hello {.author}!'.format(msg))
@client.command()
async def test(ctx):
    await ctx.send(utils.format_weis(miner.balance()))

            #def check(m):
            #return m.content == 'hello' and m.channel == channel
            #msg = await client.wait_for('message', check=check)
            #await channel.send('Hello {.author}!'.format(msg))

client.run('TOKEN HERE')
