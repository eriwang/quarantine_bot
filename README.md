# Quarantine Bot

A repo for pretty specific functionality I'm adding to a personal discord server. Built using the
[nextcord](https://github.com/nextcord/nextcord) library.

## Set up for Development

This project uses `pipenv` to manage dependencies (I used 2022.1.8). Once `pipenv` is installed:

- Create a discord bot in the [Developer Portal](https://discord.com/developers/applications)
- `pipenv install`
- Copy `example.config.json` to `config.json`
    - Change the token to your discord bot's token
    - Change the guild ID list to the list of guild IDs (servers) you want to add the bot to (otherwise it'll add to
      all servers it's registered to)
    - Alternatively, set the env vars used in `main.py` accordingly (this is what the heroku deploy uses)
- `pipenv run start` will run the bot.
- The bot will print out a URL that will let you add it to a server you have permissions for.

See `Pipfile` for useful scripts (e.g. `pipenv run lint`).

## Deployment

This is CD'd on Heroku using the `main` branch.
