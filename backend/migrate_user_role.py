"""
Add role column to users table
"""
from database import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        conn.execute(text("ALTER TABLE users ADD COLUMN role VARCHAR DEFAULT 'user'"))
        conn.commit()
        print("✅ User role column added successfully")
except Exception as e:
    if "already exists" in str(e) or "duplicate column" in str(e).lower():
        print("ℹ️  Role column already exists")
    else:
        print(f"⚠️  Migration warning: {e}")
