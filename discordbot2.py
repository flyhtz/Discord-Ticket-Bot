import discord

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # Get the channel where you want to send the message
    channel = client.get_channel(CHANNEL_ID)  # Replace CHANNEL_ID with the ID of the channel
    
    # Send the message
    message = await channel.send("React with 🎟 to open a ticket")
    
    # Add a reaction to the message
    await message.add_reaction("🎟")  # Replace "🎟" with the emoji you want to use


async def open_ticket(user):
    # Create the ticket channel
    ticket_channel = await user.guild.create_text_channel(f"ticket-{user.id}")
    
    # Send a message to the user
    await user.send(f"Your ticket has been opened in {ticket_channel.mention}")
    
    # Add the user to the channel
    await ticket_channel.set_permissions(user, read_messages=True, send_messages=True)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🎟":  # Replace "🎟" with the emoji you want to use
        await open_ticket(user)

client.run('YOUR_BOT_TOKEN_HERE')