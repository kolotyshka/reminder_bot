# Reminder Bot / Бот Напоминаний 
 
## English 
 
Reminder Bot is a Telegram bot designed to help users set reminders with optional dates. It supports both English and Russian languages, stores tasks in JSON, and sends notifications at the specified time. The project demonstrates Object-Oriented Programming (OOP), asynchronous programming, and a custom decorator for logging. 
 
- **Commands**: 
  - `/start`: Displays a welcome message. 
  - `/add <text> at <time> [date]` or `/add <text> в <time> [date]`: Adds a reminder (e.g., `/add Meeting at 14:30 27.05.2025` or `/add Встреча в 14:30`). 
  - `/list`: Shows all reminders with their times and dates. 
  - `/delete <index>`: Deletes a reminder by its index. 
- **Notifications**: Sends `Reminder: <text>` at the specified time and date. 
- **Storage**: Tasks are saved in `reminders.json` with UTF-8 encoding. 
- **Languages**: Supports English and Russian text. 
- **Logging**: Commands and notifications are logged in `bot.log`. 
 
- **Python**: Core programming language. 
- **aiogram**: Asynchronous Telegram Bot API framework. 
- **asyncio**: For asynchronous task checking and notifications. 
- **JSON**: For persistent storage. 
- **OOP**: Classes for tasks, task manager, and storage. 
- **Custom Decorator**: For command logging. 
 
1. Clone the repository: 
   ```bash 
   git clone https://github.com/kolotyshka/reminder_bot.git 
   cd reminder_bot 
   ``` 
2. Install dependencies: 
   ```bash 
   pip install aiogram 
   ``` 
3. Create `config.py` with your Telegram Bot API token: 
   ```python 
   API_TOKEN = "your_bot_token_here" 
   ``` 
4. Run the bot: 
   ```bash 
   chcp 65001 
   python main.py 
   ``` 
 
- Send `/start` to see the welcome message. 
- Add a reminder: `/add Meeting at 14:30` or `/add Встреча в 14:30 27.05.2025`. 
- List reminders: `/list`. 
- Delete a reminder: `/delete 1`. 
 
- GitHub: [https://github.com/kolotyshka/reminder_bot](https://github.com/kolotyshka/reminder_bot) 
 
--- 
 
## Русский 
 
Бот Напоминаний — это Telegram-бот, который помогает пользователям устанавливать напоминания с опциональной датой. Он поддерживает английский и русский языки, хранит задачи в JSON и отправляет уведомления в указанное время. Проект демонстрирует объектно-ориентированное программирование (ООП), асинхронное программирование и пользовательский декоратор для логирования. 
 
- **Команды**: 
  - `/start`: Показывает приветственное сообщение. 
  - `/add <текст> at <время> [дата]` или `/add <текст> в <время> [дата]`: Добавляет напоминание (например, `/add Meeting at 14:30 27.05.2025` или `/add Встреча в 14:30`). 
  - `/list`: Показывает все напоминания с временем и датой. 
  - `/delete <индекс>`: Удаляет напоминание по его индексу. 
- **Уведомления**: Отправляет `Reminder: <текст>` в указанное время и дату. 
- **Хранение**: Задачи сохраняются в `reminders.json` с кодировкой UTF-8. 
- **Языки**: Поддерживает английский и русский текст. 
- **Логирование**: Команды и уведомления записываются в `bot.log`. 
 
- **Python**: Основной язык программирования. 
- **aiogram**: Асинхронный фреймворк для Telegram Bot API. 
- **asyncio**: Для асинхронной проверки задач и уведомлений. 
- **JSON**: Для постоянного хранения данных. 
- **ООП**: Классы для задач, менеджера задач и хранения. 
- **Пользовательский декоратор**: Для логирования команд. 
 
1. Скопируйте репозиторий: 
   ```bash 
   git clone https://github.com/kolotyshka/reminder_bot.git 
   cd reminder_bot 
   ``` 
2. Установите зависимости: 
   ```bash 
   pip install aiogram 
   ``` 
3. Создайте файл `config.py` с вашим токеном Telegram-бота: 
   ```python 
   API_TOKEN = "ваш_токен_бота" 
   ``` 
4. Запустите бота: 
   ```bash 
   chcp 65001 
   python main.py 
   ``` 
 
- Отправьте `/start`, чтобы увидеть приветственное сообщение. 
- Добавьте напоминание: `/add Meeting at 14:30` или `/add Встреча в 14:30 27.05.2025`. 
- Просмотрите напоминания: `/list`. 
- Удалите напоминание: `/delete 1`. 
 
- GitHub: [https://github.com/kolotyshka/reminder_bot](https://github.com/kolotyshka/reminder_bot) 
### Repository 
- GitHub: [https://github.com/kolotyshka/reminder_bot](https://github.com/kolotyshka/reminder_bot) 
 
*My first project, built with neural network help, to learn OOP, async programming, decorators, and JSON. Please don’t judge too harshly :).* 
 
--- 
## English 
### Overview 
### Features 
### Technologies 
### Installation 
### Usage 
### Repository 
## Русский 
### Обзор 
### Функционал 
### Технологии 
### Установка 
### Использование 
### Репозиторий 
 
*Мой первый проект, созданный с помощью нейросети, чтобы освоить ООП, асинхронность, декораторы и JSON. Не судите строго :).* 
