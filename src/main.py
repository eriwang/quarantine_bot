import json

import nextcord

config = json.load(open('config.json'))
guild_ids = config['guild_ids'] if 'guild_ids' in config else None

client = nextcord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    print('This bot is part of the following guilds:')
    print('\n'.join([f'  - {g.name} ({g.id})' for g in client.guilds]))


@client.event
async def on_message(message: nextcord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


_SIMP_UNICODE = ['🇸', '🇮', '🇲', '🇵']


@client.message_command(name='Simp', guild_ids=guild_ids)
async def react_with_simp(interaction: nextcord.Interaction, msg: nextcord.Message):
    for s in _SIMP_UNICODE:
        await msg.add_reaction(s)

    await interaction.response.send_message(f'Called {msg.author.name} a simp', ephemeral=True)


@client.message_command(name='Unsimp', guild_ids=guild_ids)
async def unreact_simp(interaction: nextcord.Interaction, msg: nextcord.Message):
    for s in _SIMP_UNICODE:
        await msg.remove_reaction(s, client.user)

    await interaction.response.send_message(f'Hm, I guess {msg.author.name} isn\'t a simp', ephemeral=True)


client.run(config['token'])