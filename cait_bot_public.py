import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
  
f = open("token.txt", "r")

bot_prefix= "+"
client = commands.Bot(command_prefix=bot_prefix)
TOKEN = f.read() # insert token here

# I want a custom help menu here
client.remove_command('help')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
	if message.author == client.user:
		return

	await client.process_commands(message)
	
#to verify setup
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


#displays info about this bot
@client.command()
async def about(ctx):
	embed = discord.Embed(title="About Caitlyn Bot", color=0x7f00ff)
	
	embed.add_field(name="Version", value="1.0.0", inline=False)
	embed.add_field(name="Developer", value="Jack Bai", inline=False)
	embed.add_field(name="Source", value="https://github.com/bai-rongzhuo/caitlyn-bot", inline=False)
	
	
	await ctx.send(embed=embed)

	
	


#displays the current cait build; will be updated manually until I can hook this to the riot api
@client.command()
async def builds(ctx):
	embed = discord.Embed(title="Caitlyn Builds", description="Updated for Patch 8.17", color=0x7f00ff)
	
	embed.add_field(name="Skill Order", value="R > Q > W > E or R > W > Q > E")
	embed.add_field(name="Runes", value="Precision primary, Sorcery secondary.", inline=False)
	embed.add_field(name="Precision", value="**FLEET FOOTWORK**\nTriumph\nLegend: Bloodline / Legend: Alacrity\nCoup de Grace / Cut Down\n", inline=True)
	embed.add_field(name="Sorcery", value="Gathering Storm / Absolute Focus\n Celerity", inline=True)
	embed.add_field(name="Item Builds", value="This is a guideline only.  Build according to the state of your game.", inline=False)
	embed.add_field(name="Common", value="Stormrazor\nRapid Firecannon\nBerserker's Greaves\nInfinity Edge\nStatikk Shiv\nThe Bloodthirster", inline=True)
	embed.add_field(name="Situationals", value="Lord Dominik's Regards\nRunaan's Hurricane\nGuardian Angel\nMercurial Scimitar", inline=True)
	
	await ctx.send(embed=embed)

	
#displays bubba's guide on cait
@client.command()
async def guide(ctx):
	await ctx.send(file=discord.File("C:\\Users\\Jack\\Desktop\\python\\bots\\imgs\\CaitGuide.png"))

#press f to pay respects
@client.command()
async def f(ctx):
	await ctx.send( str(ctx.message.author.mention) + " has paid their respects. :regional_indicator_f:")

#help menu
@client.command()
async def help(ctx):
	embed = discord.Embed(title="Help with Caitlyn Bot", description="Prefix for this bot is \"+\".",color=0x7f00ff)
	embed.add_field(name="builds", value="Displays the builds, runes, and skill order for the current patch.")
	embed.add_field(name="f", value="Press F to pay respects. :regional_indicator_f:")
	embed.add_field(name="guide", value="Displays Bubba Dreemurr#0841's Caitlyn guide infographic.")
	embed.add_field(name="help", value="Displays this screen.", inline=False)
	embed.add_field(name="about", value="Displays information about this bot.", inline=False)
	await ctx.send(embed=embed)
	
	
client.run(TOKEN)