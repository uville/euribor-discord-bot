#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pi/git/euribor-discord-bot
source ".venv/bin/activate"
echo $VIRTUAL_ENV
sudo python bot.py
cd /