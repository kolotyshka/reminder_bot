from datetime import datetime
import functools

def log_command(func):
    """Логирует вызов команды бота в файл bot.log с временной меткой и текстом команды.
        Logs the bot command call to bot.log with timestamp and command text."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = args[0] if args else None
        command_text = message.text if hasattr(message, 'text') else "unknown"
        with open("bot.log", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Command {func.__name__} called: {command_text}\n")
        return await func(*args, **kwargs)
    return wrapper