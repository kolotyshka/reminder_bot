# Telegram Reminder Bot 
A simple asynchronous Telegram bot for setting and receiving reminders. 
 
## Features 
- Add reminders with `/add <text> at <time>` (e.g., `/add Meeting at 14:30`). 
- Receive notifications at specified times. 
- Store reminders in JSON. 
 
## Installation 
1. Clone the repository: 
   ```bash 
   git clone https://github.com/kolotyshka/reminder_bot.git 
   ``` 
2. Create and activate a virtual environment: 
   ```bash 
   python -m venv .venv 
   .venv\Scripts\activate 
   ``` 
3. Install dependencies: 
   ```bash 
   pip install -r requirements.txt 
   ``` 
4. Set your bot token in `main.py` (get it from @BotFather). 
5. Run the bot: 
   ```bash 
   python main.py 
   ``` 
 
## Usage 
- `/start`: Start the bot. 
- `/add <text> at <time>`: Set a reminder (e.g., `/add Meeting at 14:30`). 
 
## Dependencies 
- aiogram==3.20.0 
- aiosqlite==0.21.0 
