<div align="center">

# 🧠 HabitBot

### Telegram Habit Tracker — Build Discipline, Track Progress, Stay Motivated

<br>

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF0000?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-3DA639?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📝 Create Habits | Add habits with title and description via step-by-step conversation |
| ✅ Daily Logging | Log time spent on each habit with one tap |
| 🔥 Streaks | Automatic streak tracking — never break the chain |
| 🏆 Records | Personal best streaks saved and displayed |
| 📊 Charts | Visual progress bars with average and total time |
| 💬 Quotes | Daily motivational quotes from external API |
| 🗑️ Manage | View, delete, or update habits anytime |

---

## 🛠️ Tech Stack

```
🐍 Python 3.9+
🤖 python-telegram-bot (v20+)
🐘 PostgreSQL + SQLAlchemy
📈 Matplotlib + Pandas
🌐 aiohttp (async API)
```

---

## 📁 Project Structure

```
HabitBot/
│
├── main.py                 # Entry point — runs the bot
├── config.py               # Tokens & configuration
├── requirements.txt        # Dependencies
│
├── database/
│   ├── models.py           # User, Habit, HabitLog models
│   └── requests.py         # Database operations
│
├── keyboards/
│   └── builders.py         # Keyboard builders
│
├── services/
│   ├── api_quote.py        # Motivational quotes API
│   └── stats_gen.py        # Chart generation with matplotlib
│
└── handlers/
    ├── start.py            # /start command & main menu
    ├── creation.py         # Habit creation (FSM)
    ├── tracking.py         # Logging & deletion
    └── statistics.py       # Stats & graphs
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/HabitBot.git
cd HabitBot
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file or update `config.py`:

```env
BOT_TOKEN=your_telegram_bot_token_here
DATABASE_URL=postgresql://username:password@localhost/habitbot
```

### 5. Run the bot

```bash
python main.py
```

---

## 📊 Key Metrics

| Metric | Description |
|--------|-------------|
| 🔥 **Streak** | Consecutive days of logging a habit |
| 🏆 **Record** | Highest streak ever achieved |
| ⏱️ **Total Time** | Sum of all minutes logged |
| 📊 **Average** | Mean minutes per session |

---

## 🧠 How It Works

1. User starts the bot with `/start` — auto-registration
2. Creates habits via interactive FSM (title + description)
3. Logs time spent each day
4. Bot automatically calculates streaks and records
5. User can view progress charts anytime
6. Motivational quotes keep the user inspired

---

## 📸 Screenshots

> *Add screenshots of your bot in action here*

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙌 Acknowledgments

- [ZenQuotes.io](https://zenquotes.io/) for free motivational quotes API
- [python-telegram-bot](https://python-telegram-bot.org/) community
- All contributors and users of HabitBot

---

<div align="center">

**⭐ Star this repo if you find it useful!**  
Made with ❤️ and Python

</div>
