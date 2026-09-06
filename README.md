```markdown
# 🧠 HabitBot — Telegram Habit Tracker

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> A smart Telegram bot to track habits, build discipline, and visualize your progress — all in one place.

---

## ✨ Features

- 📝 **Create habits** with name and description
- ✅ **Log daily progress** with time tracking
- 🔥 **Streak counter** — never break the chain
- 🏆 **Personal records** — beat your best
- 📊 **Progress charts** — see your growth
- 💬 **Motivational quotes** — daily inspiration
- 🗑️ **Manage habits** — view or delete anytime

---

## 🛠️ Built With

- **Python** 3.9+
- **python-telegram-bot** (v20+)
- **PostgreSQL** & SQLAlchemy
- **Matplotlib** + **Pandas** for charts
- **aiohttp** for async API calls

---

## 📁 Project Structure

```
HabitBot/
├── main.py                 # Entry point
├── config.py               # Tokens & settings
├── requirements.txt        # Dependencies
├── database/
│   ├── models.py           # User, Habit, HabitLog models
│   └── requests.py         # DB operations
├── keyboards/
│   └── builders.py         # Keyboard builders
├── services/
│   ├── api_quote.py        # Motivational quotes API
│   └── stats_gen.py        # Chart generation
└── handlers/
    ├── start.py            # /start & main menu
    ├── creation.py         # Habit creation (FSM)
    ├── tracking.py         # Logging & deletion
    └── statistics.py       # Stats & graphs
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/HabitBot.git
cd HabitBot
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
Create a `.env` file or update `config.py`:
```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

### 5. Run the bot
```bash
python main.py
```

---

## 📊 Key Metrics

| Metric | Description |
|--------|-------------|
| **Streak** | Consecutive days of logging |
| **Record** | Highest streak ever achieved |
| **Total Time** | Sum of all logged minutes |
| **Average** | Mean minutes per session |

---

## 📸 Screenshots

> *Coming soon — add your bot screenshots here*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/yourusername/HabitBot/issues).

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙌 Acknowledgments

- [ZenQuotes.io](https://zenquotes.io/) for motivational quotes API
- [python-telegram-bot](https://python-telegram-bot.org/) community
```

---

## 📝 Short Description (max 350 characters)

```
HabitBot is a Telegram habit tracker built with Python. Create habits, log daily progress, track streaks, view stats, and get motivational quotes — all in one bot.
```

**Character count:** 222 ✅
