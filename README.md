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
 
# Telegram Бот Напоминаний 
Простой асинхронный Telegram-бот для установки и получения напоминаний. 
 
## Возможности 
- Добавление напоминаний с помощью `/add <текст> at <время>` (например, `/add Встреча at 14:30`). 
- Получение уведомлений в указанное время. 
- Хранение напоминаний в JSON. 
 
## Установка 
1. Клонируйте репозиторий: 
   ```bash 
   git clone https://github.com/kolotyshka/reminder_bot.git 
   ``` 
2. Создайте и активируйте виртуальное окружение: 
   ```bash 
   python -m venv .venv 
   .venv\Scripts\activate 
   ``` 
3. Установите зависимости: 
   ```bash 
   pip install -r requirements.txt 
   ``` 
4. Укажите токен бота в `config.py` (получите у @BotFather). 
5. Запустите бота: 
   ```bash 
   python main.py 
   ``` 
 
## Использование 
- `/start`: Запустить бота. 
- `/add <текст> at <время>`: Установить напоминание (например, `/add Встреча at 14:30`). 
 
## Зависимости 
- aiogram==3.20.0 
- aiosqlite==0.21.0 
