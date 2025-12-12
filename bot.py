import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

with open("config.json", "r") as f:
    config = json.load(f)
token = config["TELEGRAM_TOKEN"]
api = config["OWM_API_KEY"]
g = "Khujand,TJ"
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={g}&appid={api}&units=metric&lang=ru"
    try:
        r = requests.get(url, timeout=10)
        data = response.json()
        if r.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"Погода в Худжанде: {temp}°C, {description}"
        else:
            return f"Ошибка API ({response.status_code}): {data.get('message')}"
    except requests.RequestException as e:
        return f"Ошибка запроса: {e}"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    weather = get_weather()
    await update.message.reply_text(weather)
if __name__ == "__main__":
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
