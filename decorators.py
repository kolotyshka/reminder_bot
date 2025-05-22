from datetime import datetime
import functools

def log_command(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("bot.log", 'a', encoding="utf-8") as f:
            f.write(f"{timestamp} Command {func.__name__} called\n")
        return await func(*args, **kwargs)
    return wrapper