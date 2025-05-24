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
4. Set your bot token in `config.py` (get it from @BotFather). 
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
 
# Telegram ��� ����������� 
���⮩ �ᨭ�஭�� Telegram-��� ��� ��⠭���� � ����祭�� �����������. 
 
## ���������� 
- ���������� ����������� � ������� `/add <⥪��> at <�६�>` (���ਬ��, `/add ����� at 14:30`). 
- ����祭�� 㢥�������� � 㪠������ �६�. 
- �࠭���� ����������� � JSON. 
 
## ��⠭���� 
1. �������� ९����਩: 
   ```bash 
   git clone https://github.com/kolotyshka/reminder_bot.git 
   ``` 
2. ������� � ��⨢���� ����㠫쭮� ���㦥���: 
   ```bash 
   python -m venv .venv 
   .venv\Scripts\activate 
   ``` 
3. ��⠭���� ����ᨬ���: 
   ```bash 
   pip install -r requirements.txt 
   ``` 
4. ������ ⮪�� ��� � `config.py` (������ � @BotFather). 
5. ������� ���: 
   ```bash 
   python main.py 
   ``` 
 
## �ᯮ�짮����� 
- `/start`: �������� ���. 
- `/add <⥪��> at <�६�>`: ��⠭����� ����������� (���ਬ��, `/add ����� at 14:30`). 
 
## ����ᨬ��� 
- aiogram==3.20.0 
- aiosqlite==0.21.0 
