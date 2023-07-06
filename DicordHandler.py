import discord
from discord import Colour
from DataBaseHandler import coinsUser,addCoins

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!Coins") or message.content.startswith("!AddCoins"):
        if message.guild:
            user_message = message.content.split()
            channel = client.get_channel(message.channel.id)
            role_names = [role.name for role in message.author.roles]
            
            
            user_name = await client.fetch_user(user_message[1])
            
            if message.content.startswith("!Coins"):
                try:
                    if "Admin" in role_names or "Dev" in role_names or "Staff" in role_names:
                        coins = coinsUser(user_message[1])
                        if coins == 1:
                            await channel.send(f"{user_name} has 1 coin")
                        else:
                            await channel.send(f"{user_name} has {coins} coins")
                    else:
                        await channel.send(f"{user_name} has no perms")
                except:
                    await channel.send(f"Problem fetching coins")

            elif message.content.startswith("!AddCoins"):
                try:
                    if "Admin" in role_names or "Dev" in role_names or "Staff" in role_names:
                        coins = int(coinsUser(user_message[1]))
                        coinstoadd = int(user_message[2])
                        if(coins + coinstoadd >= 0):
                            addCoins(user_message[1], user_message[2])
                            if user_message[2] == 1:
                                await channel.send(f"Successfully added 1 coin to {user_name}")
                            else:
                                await channel.send(f"Successfully added {user_message[2]} coins to {user_name}")
                        else:
                            await channel.send(f"{user_name} can't have negative points") 
                    else:
                        await channel.send(f"{user_name} has no perms")  
                except:         
                    await channel.send(f"Problem fetching coins")        

                       
client.run("ODkyMDkzMTgzNDQ0NTQ5NjMy.YVH4hQ.LCg00lRAHlqAqZRd0tR--vNyd4A")