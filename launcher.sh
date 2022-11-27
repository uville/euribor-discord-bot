#!/bin/bash
activate()  {
    cd ./home/ville/git/euribor-discord-bot/
    . ".venv/bin/activate"
    echo "Activated venv"
    python --version
    echo "Starting the program..."
    python bot.py
}
activate