import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('Insert Game'))
	print('Bot Is Online')

@client.event
async def on_member_join(member):
	print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left the server.')

#.ping
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
	return

#.clear(#)
@client.command()
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)

#.kick @member#0000
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'kicked {member.mention}')

#.ban @member#0000
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'banned {member.mention}')

#.unban member#0000
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return
			
client.run("Insert Token")
