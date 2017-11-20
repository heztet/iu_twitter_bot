# greyhouse_status
This is the code used to run [@And_IU_Sucks](https://twitter.com/And_IU_Sucks), a satiric Twitter bot that posts the status of IU daily. The bot can be configured to send Pushover notifications to a user whenever a Python exception is thrown.

## Modifications
The bot is configured so that more features can be added easily in the main section, so that in the future more "intelligence" and complexity can be added without much pain.

## Setup
### Twitter API Keys
To run the bot, download these files into a directory, then create a new file `twitter_keys.py` in the same directory that has the following information: 
```
CONSUMER_KEY = <key as string>
CONSUMER_SECRET = <secret as string>
ACCESS_TOKEN_KEY = <token as string>
ACCESS_TOKEN_SECRET = <secret as string>
```
which you can get from the [Twitter App Creation Site](https://apps.twitter.com/app/new)

### Pushover API Keys
In addition, for Pushover notifications if an error occurs, create a file `pushover_keys.py` in the same directory in the form:
```
PUSHOVER_USER = <user as string>
PUSHOVER_APP_TOKEN = <token as string>
```
which you can get from [Pushover](https://pushover.net/). If this file doesn't exist, greyhouse_status will assume you don't want to be notified of any issues, but will still raise any exceptions that occur.
