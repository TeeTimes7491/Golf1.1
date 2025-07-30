# ⛳ Golf Tee Time Booking Agent

This Python automation agent books a golf tee time on [https://fox.tenfore.golf/mcggolf](https://fox.tenfore.golf/mcggolf) at a scheduled time using Playwright.

---

## 🚀 Features

- Automates login, course/date/time selection, and booking
- Uses environment variables for secure credentials
- Can run manually or be hosted using Render (Cron Job)

---

## 🧩 Files

- `book_tee_time.py`: Main automation logic using Playwright
- `config.json`: Customize booking date, time, course, players
- `requirements.txt`: Python dependencies
- `.env.example`: Template for secret login credentials
- `README.md`: Setup and deployment instructions
- `.gitignore`: Prevents committing sensitive files

---

## 🖥️ Local Setup

1. **Install dependencies**
```bash
pip install -r requirements.txt
playwright install
```

2. **Create `.env` file**
```bash
cp .env.example .env
```

Edit `.env` and add:
```
GOLF_USERNAME=your_email@example.com
GOLF_PASSWORD=your_secure_password
```

3. **Run script manually**
```bash
python book_tee_time.py
```

---

## ☁️ Deploy to Render (Recommended)

1. Push this repo to GitHub.
2. Go to [https://render.com](https://render.com).
3. Create a **Cron Job** service.
4. Connect your GitHub repo.
5. Set:
   - **Build Command**: `playwright install`
   - **Start Command**: `python book_tee_time.py`
6. Add environment variables in the dashboard:
   - `GOLF_USERNAME`
   - `GOLF_PASSWORD`
7. Set schedule (e.g., Fridays at 6:58 AM):
   ```
   58 6 * * 5
   ```

You're set!

---

## 📄 License

MIT License
