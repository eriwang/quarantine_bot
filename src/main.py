import json
from typing import Union

import nextcord

with open('config.json', encoding='UTF-8') as config_file:
    config = json.load(config_file)

guild_ids = config['guild_ids'] if 'guild_ids' in config else None

client = nextcord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    print('This bot is part of the following guilds:')
    print('\n'.join([f'  - {g.name} ({g.id})' for g in client.guilds]))

    perms = nextcord.Permissions(read_messages=True, send_messages=True, manage_messages=True, add_reactions=True)
    print(f'Click the following URL to add the bot: {nextcord.utils.oauth_url(client.user.id, permissions=perms)}')


_SIMP_UNICODE = ['🇸', '🇮', '🇲', '🇵']


@client.event
async def on_message(msg: nextcord.Message):
    if msg.author == client.user:
        return

    if msg.content == '$simp':
        # If this isn't a reply, this command can't do anything
        if msg.reference is None:
            return

        await _react_with_simp(msg.channel.get_partial_message(msg.reference.message_id))
        await msg.delete()

    elif msg.content == '$unsimp':
        # If this isn't a reply, this command can't do anything
        if msg.reference is None:
            return

        await _unsimp(msg.channel.get_partial_message(msg.reference.message_id))
        await msg.delete()


@client.message_command(name='Simp', guild_ids=guild_ids)
async def react_with_simp(interaction: nextcord.Interaction, msg: nextcord.Message):
    await _react_with_simp(msg)
    await interaction.response.send_message(f'Called {msg.author.name} a simp', ephemeral=True)


@client.message_command(name='Unsimp', guild_ids=guild_ids)
async def unreact_simp(interaction: nextcord.Interaction, msg: nextcord.Message):
    await _unsimp(msg)
    await interaction.response.send_message(f'Hm, I guess {msg.author.name} isn\'t a simp', ephemeral=True)


async def _react_with_simp(msg: Union[nextcord.Message, nextcord.PartialMessage]):
    for s in _SIMP_UNICODE:
        await msg.add_reaction(s)


async def _unsimp(msg: Union[nextcord.Message, nextcord.PartialMessage]):
    for s in _SIMP_UNICODE:
        await msg.remove_reaction(s, client.user)


client.run(config['token'])
