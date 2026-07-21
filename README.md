# NONETWORK Discord Bot

A Discord welcome/farewell bot for the NONETWORK server.

## Features

| Event | Channel | What it sends |
|---|---|---|
| Member joins | `#welcome` (1511119087051473137) | Welcome embed with ordinal member count |
| Member leaves | `#farewell` (1529202684723331102) | Farewell embed with remaining member count |

---

## Files

```
bot.py            ← main bot code
requirements.txt  ← Python dependencies
railway.toml      ← Railway deployment config
.gitignore        ← keeps .env and __pycache__ out of git
```

---

## Local setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your token (do NOT commit this)
export DISCORD_TOKEN=your_token_here   # macOS / Linux
set DISCORD_TOKEN=your_token_here      # Windows CMD

# 3. Run
python bot.py
```

---

## Deploy to Railway via GitHub

### Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2 — Create a Railway project

1. Go to [railway.app](https://railway.app) and log in.
2. Click **New Project → Deploy from GitHub repo**.
3. Select your repository.
4. Railway will detect `railway.toml` and use `python bot.py` automatically.

### Step 3 — Add the bot token as an environment variable

1. Inside your Railway project, open the **Variables** tab.
2. Click **+ New Variable**.
3. Set:
   - **Name:** `DISCORD_TOKEN`
   - **Value:** your bot token (from the Discord Developer Portal)
4. Click **Add** — Railway redeploys automatically.

### Step 4 — Enable the Members intent on Discord

1. Open [discord.com/developers/applications](https://discord.com/developers/applications).
2. Select your application → **Bot**.
3. Under **Privileged Gateway Intents**, enable **Server Members Intent**.
4. Save changes.

The bot is now live. Every time a member joins or leaves your server it will post the correct message automatically.

---

## Configuration

To change channel IDs, edit the two constants at the top of `bot.py`:

```python
WELCOME_CHANNEL_ID = 1511119087051473137
LEAVE_CHANNEL_ID   = 1529202684723331102
```

Commit and push — Railway redeploys within seconds.
