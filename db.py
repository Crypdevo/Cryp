import sqlite3

DB_PATH = "cryp.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        telegram_user_id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT,
        is_pro INTEGER DEFAULT 0,
        paystack_customer_code TEXT,
        paystack_subscription_code TEXT,
        paystack_email_token TEXT,
        subscription_status TEXT,
        current_period_end TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference TEXT UNIQUE,
        telegram_user_id INTEGER,
        amount INTEGER,
        currency TEXT,
        status TEXT,
        event_type TEXT,
        paid_at TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
