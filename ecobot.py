import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

from ecobot_dictionary import tree_facts, environment_facts, waste_facts
from ecobot_dictionary import organic_trash, recyclable_trash, hazardous_trash
from ecobot_dictionary import tree_pass
from ecobot_dictionary import common_trees, tree_hints
import random

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ecobot(ctx):
    help_message = """
**👋 Hi! I\'m Ecobot! How can I assist you today?**

🛠️ **Available Commands**
- `$ecobot` → Shows this command list.
- `$funfact [type:tree|environment|waste]` → Displays a random fun fact about anything envirnonment related.
- `$trash [type:organic|recyclable|hazardous]` → Provides information about different types of trash.
- `$password [length]` → Generates a secure tree-themed password of the specified length.
- `$guesstree` → Starts a fun guessing game about trees with hints!
"""
    await ctx.send(help_message)

@bot.command()
async def funfact(ctx, facttype: str):
    if facttype.lower() == "tree":
        fact = tree_facts[random.randint(1, 20)]
    elif facttype.lower() == "environment":
        fact = environment_facts[random.randint(1, 20)]
    elif facttype.lower() == "waste":
        fact = waste_facts[random.randint(1, 20)]
    else:
        fact = "Please specify a valid fact type: 'tree', 'environment', or 'waste'."
    await ctx.send(fact)

@bot.command()
async def trash(ctx, trash_type: str):
    if trash_type.lower() == "organic":
        await ctx.send(organic_trash)
    elif trash_type.lower() == "recyclable":
        await ctx.send(recyclable_trash)
    elif trash_type.lower() == "hazardous":
        await ctx.send(hazardous_trash)
    else:
        await ctx.send("Please specify a valid trash type: 'organic', 'recyclable', or 'hazardous'.")
        
@bot.command()
async def password(ctx, length: int = 10):
    if length < 1 or length > 40:
        await ctx.send("Please specify a length between 1 and 40 for the password.")
        return

    password_text = tree_pass(length)
    await ctx.send(f"Your random tree-themed password is: {password_text}")

@bot.command()
async def guesstree(ctx):
    tree = random.choice(common_trees)
    hint = tree_hints[tree]
    tries = 3

    await ctx.send(f"Guess the tree from this hint:\n**{hint}**\nYou have **3 tries**.")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    while tries > 0:
        guess_msg = await bot.wait_for("message", check=check)
        guess = guess_msg.content.strip().lower()

        if guess == tree.lower():
            await ctx.send(f"Correct! The tree was **{tree}**.")
            return

        tries -= 1
        if tries > 0:
            await ctx.send(f"Wrong guess. You have **{tries}** tries left.")
        else:
            await ctx.send(f"Out of tries! The correct answer was **{tree}**.")

bot.run("TOKEN")
