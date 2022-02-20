# Quarantine Bot

A repo for pretty specific functionality I'm adding to a personal discord server. Built using the
(nextcord)[https://github.com/nextcord/nextcord] library.

## Set up for Development

This project uses `pipenv` to manage dependencies (I used 2022.1.8). Once `pipenv` is installed:

- `pipenv install`
- Copy `example.config.json` to `config.json`
    - Change the token to your discord bot's token
    - Change the guild ID list to the list of guild IDs (servers) you want to add the bot to (otherwise it'll add to
      all servers it's registered to)
- `pipenv run python src/main.py` will run the bot