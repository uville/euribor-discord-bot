#!/usr/bin/env bash
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pi/git/euribor-discord-bot
set -e
source /home/pi/git/euribor-discord-bot/.venv/bin/activate
sudo python bot.py
deactivate
cd /
