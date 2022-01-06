import discord
import random

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  greetings = ['Hi :)', 'Bye', '...', 'Leave me alone', 'Sup dude', '안녕하세요', '.......', 'こんにちは']
  if message.author == client.user:
    return
  if message.content.startswith('-hello'):
    await message.channel.send(greetings[random.randrange(0,8,1)])
  if message.content.startswith('-toast'):
    await message.channel.send('https://www.google.com.jm/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Ftoast-bread&psig=AOvVaw1yctLUqMqHGbvrcf2P3Pfc&ust=1641594969063000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCICym4OYnvUCFQAAAAAdAAAAABAO')

client.run('OTI3NTk1ODQ3MjY3NTQ5MTk1.YdMg8w.uZz7A6i56zCb0CDdZpqtYlfQxPo')