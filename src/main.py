from discord.ext import commands
import discord
from random import randint

intents = discord.Intents.default()
intents.members = True
intents.presences = True
#intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 364460789412921344  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):

    #WARMUP - STEP ONE
    if message.content.startswith('!name'):
        await message.channel.send(message.author + "🥵") #we just send a basic message
    
    #WARMUP - STEP 2
    if message.content.startswith('!d6'):
        n = randint(1,6) #we get a random number
        if (n == 1):
            await message.channel.send("1️⃣") #we print a corresponding emoji
        if (n == 2):
            await message.channel.send("2️⃣")
        if (n == 3):
            await message.channel.send("3️⃣")
        if (n == 4):
            await message.channel.send("4️⃣")
        if (n == 5):
            await message.channel.send("5️⃣")
        if (n == 6):
            await message.channel.send("6️⃣")
    
    #WARMUP - STEP 3
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul" + message.author.mention + "💀")

    #ADMINISTRATION - ADMIN ( spoiler : it does not work 🤷‍♂️)
    if message.content.startswith('!admin'):
        themember = ""
        for member in bot.get_all_members(): #we see chich member display name matches the one in the message
           if member.display_name == message.content[7:]:  #7 cause !admin is 6 letters + the space
                themember = member 

        guild = await bot.create_guild("whatever")
        role = await guild.create_role(name = "Admin")
        #await themember.add_roles(role)

    #ADMINISTRATION - ban
    if message.content.startswith('!ban'):
        themember = ""
        for member in bot.get_all_members():
           if member.display_name == message.content[5:]:  
                themember = member
        await themember.ban()
        await message.channel.send("see you never " + message.content[5:] + " 👋")

    #ADMINISTRATION - count
    if message.content.startswith('!count'):
        for member in bot.get_all_members(): #iterate over members and get their status
            await message.channel.send(member.name + " is " + str(member.status))

    #GAMES - poll
    if message.content.startswith('!poll'):
        await message.channel.send("@here") #ping
        themessage = await message.channel.send(message.content[6:]) #print the message
        await themessage.add_reaction("👍") #add the reactions
        await themessage.add_reaction("👎")

token = ""
bot.run(token)  # Starts the bot

