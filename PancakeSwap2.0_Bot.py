
import discord
from discord.ext import commands, tasks
import json
import requests
client = commands.Bot(command_prefix= '!')
#This bot was made per request of the client
#Any offensive words have been "REDACTED"
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Tracking them *REDACTED*coins"))
    print('bot is ready')
@client.command(pass_context=True)
async def SCB(ctx, url2):
    try:
        url = "https://api.pancakeswap.info/api/v2/tokens/" + url2
        html_content = requests.get(url).text
        # print(html_content)
        y = json.loads(html_content)
        x = json.dumps(y)
        embed = discord.Embed(title=y["data"]["name"]+" / " + y["data"]["symbol"], description="")
        embed.add_field(name="💰Price💰", value=y["data"]["price"], inline=True)
        embed.add_field(name="🔍 Token Address: ", value=url2, inline=True)
        embed.add_field(name="📝 Bscscan:", value="https://bscscan.com/address/" + url2, inline=False)
        embed.add_field(name="👃 Token Sniffer:", value="https://tokensniffer.com/token/" + url2, inline=False)
        embed.add_field(name="📈 Bogged Chart:", value="https://charts.bogged.finance/" + url2, inline=False)
        embed.add_field(name="📊 Poocoin Chart:", value="https://poocoin.app/tokens/" + url2, inline=False)
        msg = await ctx.send(embed=embed)
    except:
        await ctx.send("Sorry, that coin is too REDACTED for me to locate.")
client.run("TOKEN")
