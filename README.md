# Euribor-bot

Discord bot which fetches the latest rates from [Suomen Pankki website.](https://www.suomenpankki.fi/WebForms/ReportViewerPage.aspx?report=/tilastot/markkina-_ja_hallinnolliset_korot/euribor_korot_today_xml_en&output=xml)


## Prerequisites

- Discord account
- A bot configured to a channel

## Setup

Create & activate a virtual enviroment
```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Store Discord token as an enviroment variable with name:
> DISCORD_TOKEN

## Run

Start the bot by running
```
python3 bot.py
```

## Set up Crontab

Make script executable by running command
```
chmod 755 launcher.sh
```

Open crontab by running
```
sudo crontab -e
```

Then set script to start automatically by inserting
```
@reboot sh /home/pi/git/euribor-discord-bot/launcher.sh >/home/pi/git/euribor-discord-bot/logs/cronlog 2>&1
```


## Usage

Send messages to the Discord channel using keywords from the section below.

## Implemented commands

| Command | Description  |
| ------- | --- |
| !euribor12 | Reply the latest available 12 months Euribor rate  |