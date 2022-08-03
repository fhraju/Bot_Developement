import discord
import requests
import json
import random
from replit import db
import os
from server_for_running import keep_alive

client = discord.Client() # Creates a new Discord client instance

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    json_data = json.loads(response.text)
    quote = json_data["content"] +" By: " + json_data["author"]
    return quote

# updates the current message in database
def update_message(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"] #if the data in the database / accessing the old data key
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements # Adding to the database
    else:
        db["encouragements"] = [encouraging_message] # If not in database then adding the message in database

# Deleting an message
def delete_message(index):
    encouragements = db["encouragements"] #Getting the message from the database
    if len(encouragements) > index: # if given user_index is greater
        del encouragements[index]
        db["encouragements"] = encouragements # updating the database with new value



@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if msg.startswith("Hi"):
        await message.channel.send("Hello!")

    quote = get_quote()
    if msg.startswith("quote"):
        await message.channel.send(quote)
    
    if db["responding"]:
      options = starter_encouragements
      if "encouragements" in db.keys():  # if the data in the database / accessing the old data key
          options = options + list(db["encouragements"])
  
      if any(word in msg for word in sad_words):
          await message.channel.send(random.choice(options))

    if msg.startswith("#new"):  # new message for the database that start with #new
        encouraging_message = msg.split("#new ", 1)[1] # Removing the #new word and a space from massege
        update_message(encouraging_message)
        await message.channel.send("New message added tho the database") # Letting the user know

    if msg.startswith("#delete"): # deleting massege from the database by user
        encouraging_message = []
        if "encouragements" in db.keys():
            index = int(msg.split("#delete", 1)[1]) #converting to integer thats why don't need to remove space
            delete_message(index)
            encouraging_message = db["encouragements"] # getting the message from the database
        await message.channel.send(encouraging_message)

    if msg.startswith("#list"):
      encouragement_message = []
      if "encouragements" in db.keys():
        encouragement_message = db["encouragements"]
      await message.channel.send(encouragement_message)

    if msg.startswith("#responding"):
      user_message = msg.split("#responding ", 1)[1]
      
      if user_message.lower() == "true":
        db["responding"] = True
        await message.channel.send("Responding is on.")
      else:
        db["responding"] = False
        await message.channel.send("Responding is off.")

keep_alive()        
my_secret = os.environ['TOKEN']
client.run(my_secret)