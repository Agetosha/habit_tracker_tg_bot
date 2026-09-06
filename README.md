<div align="center">

# 🧠 HabitTracker Bot

### Telegram Habit Tracker — Build Discipline, Track Progress, Stay Motivated

<br>

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF0000?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

---

## 📖 About

**HabitTracker Bot** is a Telegram bot built with Python that helps users build discipline, track daily habits, and stay motivated. It features habit creation, progress tracking, streak counting, visual statistics, and motivational quotes — all in one bot.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📝 Create Habits | Add habits with title and description via step-by-step FSM |
| ✅ Daily Logging | Log time spent on each habit with one tap |
| 🔥 Streaks | Automatic streak tracking — never break the chain |
| 🏆 Records | Personal best streaks saved and displayed |
| 📊 Charts | Visual progress bars with average and total time |
| 💬 Quotes | Daily motivational quotes from external API |
| 🗑️ Manage | View and delete habits anytime |

---

## 🛠️ Tech Stack

```
🐍 Python 3.9+
🤖 python-telegram-bot (v20+)
📦 SQLite + SQLAlchemy
📈 Matplotlib + Pandas
🌐 aiohttp (async API)
```

---

## 📁 Project Structure

```
HabitBot/
│
├── main.py                      # Entry point — runs the bot
├── config.py                    # Tokens & configuration
├── requirements.txt             # Dependencies
│
├── database/
│   ├── models.py                # User, Habit, HabitLog models
│   └── requests.py              # Database operations (CRUD)
│
├── keyboards/
│   └── builders.py              # Keyboard builders (main, cancel, inline)
│
├── services/
│   ├── api_quote.py             # Motivational quotes API (aiohttp)
│   └── stats_gen.py             # Chart generation with matplotlib
│
└── handlers/
    ├── start.py                 # /start command & main menu
    ├── creation.py              # Habit creation (FSM: title, description)
    ├── tracking.py              # Logging & deletion
    └── statistics.py            # Stats & graphs
```

---

## 🧠 How It Works

1. User starts the bot with `/start` — auto-registration
2. Creates habits via interactive FSM (title + description)
3. Logs time spent each day
4. Bot automatically calculates streaks and records
5. User can view progress charts anytime
6. Motivational quotes keep the user inspired

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Telegram Bot Token (from @BotFather)
- Internet connection for quotes API

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/HabitBot.git
cd HabitBot
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate          # Linux/Mac
# venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file or update `config.py`:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

### 5. Initialize database

```bash
python -c "from database.models import init_db; init_db()"
```

### 6. Run the bot

```bash
python main.py
```

---

## 📊 Database Models

### User
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| telegram_id | Integer | Telegram user ID |
| username | String | Telegram username |
| created_at | DateTime | Registration date |

### Habit
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| user_id | Integer | Foreign key to User |
| title | String | Habit name |
| description | Text | Habit description |
| created_at | DateTime | Creation date |
| streak | Integer | Current consecutive days |
| record | Integer | Best streak ever |

### HabitLog
| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| habit_id | Integer | Foreign key to Habit |
| date | Date | Log date |
| minutes | Integer | Time spent in minutes |

---

## 📊 Key Metrics

| Metric | Description |
|--------|-------------|
| 🔥 **Streak** | Consecutive days of logging a habit |
| 🏆 **Record** | Highest streak ever achieved |
| ⏱️ **Total Time** | Sum of all minutes logged |
| 📊 **Average** | Mean minutes per session |

---

## 🔌 API Integration

### Motivational Quotes
- Source: [ZenQuotes.io](https://zenquotes.io/)
- Method: GET request via aiohttp
- Fallback: Local quotes if API fails

---

## 🎮 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and show main menu |
| `/new` | Create a new habit |
| `/track` | Log time for a habit |
| `/stats` | View statistics and charts |
| `/delete` | Delete a habit |
| `/cancel` | Cancel current operation |

---

## 🧪 Running Tests

```bash
python -m pytest
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙌 Acknowledgments

- [python-telegram-bot](https://python-telegram-bot.org/) community
- [ZenQuotes.io](https://zenquotes.io/) for free motivational quotes API
- All contributors and users

---

<div align="center">

**⭐ Star this repo if you find it useful!**  
Made with ❤️ and Python

</div>
