# SnackBot

SnackBot is a chat bot for Discord with a mix of useful and novelty features. Using [discord.py](https://github.com/Rapptz/discord.py) at its core, SnackBot is designed to be modular; creating and adding new modules/commands is very simple.

While primarily intended to be run on a platform like Heroku, it is completely feasible to run a copy of SnackBot on your local machine.

## Getting Started

The following sections provide instructions to get a copy of the project set up and running on your local machine.

### Prerequisites

- This project uses [Python 3.6.2](https://www.python.org/downloads/) (although it _should_ work with any recent 3.x version... _no promises!_)
- [PostgreSQL](https://www.postgresql.org/download/) is required to take advantage of the !snack command. Use the most recent version unless you have some reason not to.

### Installing

- Run the following pip commands to download the required packages:

```
pip install discord.py
pip install praw
pip install psycopg2_binary
```
With these steps complete, you have downloaded everything you need to run the project on your machine.

### Setup

The account credentials in the following sections can be stored in local python files as described below (which are used when running the bot through [snackbot_local](snackbot/snackbot_local.py)) or they can be stored in the operating system's environmenal variables (which are used when running the bot through [snackbot.py](snackbot/snackbot.py)). Keep reading for storing them in python files or take a look at the [alternative setup section](#alternative-setup) for environmental variable storage.

Personally, I prefer using python files for testing new bot features locally, while using environmental variables for 

- To begin, use your existing Discord account to [create a new app](https://discordapp.com/developers/applications/me)

    Once completed, create a python file in [snackbot/discord_client](snackbot/discord_client) called discord_auth.py and format it with the relevant information generated from creating your Discord app, as follows:

```
CLIENT_ID = 'client id'
CLIENT_SECRET = 'client secret'
TOKEN = 'token'
```
    
- Similarly, to be able to use the Reddit commands, [create an app](https://www.reddit.com/prefs/apps/) using your existing Reddit account. For additional help, use [this great tutorial](http://pythonforengineers.com/build-a-reddit-bot-part-1/) as a reference, starting with the section titled *Create Reddit App*.

    Next, create a python file in [snackbot/reddit_client](snackbot/reddit_client) called reddit_auth.py and format it with the relevant information generated from creating your Reddit app, as follows:
    
```
CLIENT_ID = 'client id'
CLIENT_SECRET = 'client secret'
USERNAME = 'username'
PASSWORD = 'password'
USER_AGENT = 'user agent'
```

- To take advantage of the !snack command, perform the following steps

  - You will need to set an environmenal variable in your OS called 'DATABASE_URL' which, as you would guess, is the full URL to your PostgreSQL database containing snacks. Ensure this variable's value is of the form 'postgresql://[user[:password]@][netloc][:port][/dbname]'
    - _A future version will likely contain a better way to easily hop between local and server-hosted databases to facilitate cleaner testing, but this is the way to do it for now_
  
  - Create a table in your PostgreSQL database named snacks with the following columns and their data types:

```
id : serial, primary key
name : text, not null
url : text
```

### Alternative Setup

The alternative to storing your account credentials is to store them in the OS's environmental variables. While [snackbot_local.py](snackbot/snackbot_local.py) reads local python files for credentials, [snackbot.py](snackbot/snackbot.py) gathers credentials from environmental variables. This is primarily to facilitate testing while the bot is still live on a server (e.g. Heroku).

Following the steps in the [setup section](#setup) above, the only change is adding environmental variables for each credential that would have been stored in a python file instead.

For Discord, simply add 'DISCORD_' to each variable, keeping their values the same. For example, the original variable
```
CLIENT_ID = 'client id'
```
becomes the environmental variable
```
DISCORD_CLIENT_ID = 'client id'
```

Repeat this same procedure for the Reddit variables, adding 'REDDIT_' to each variable. In the same sense, the original variable
```
USER_AGENT = 'user agent'
```
becomes the environmental variable
```
REDDIT_USER_AGENT = 'user agent'
```

Repeat these changes for the appropriate Discord and Reddit credentials, adding them as environmental variables.

### Additional Notes

- The SnackBot instance in [snackbot_local.py](snackbot/snackbot_local.py) is invoked by prefixing each command with '.', while the SnackBot instance in [snackbot.py](snackbot/snackbot.py) is invoked by prefixing each command with '!'.
  - This can easily be changed by editing the following line in the run_bot() function:
  ```
  snackbot = bot.SnackBot(r, '<DESIRED COMMAND PREFIX GOES HERE>')
  ```

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details

## Acknowledgements

Shamelessly copied [PurpleBooth's lovely readme template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
