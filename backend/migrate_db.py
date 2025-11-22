"""
Database migration script to rename username column to email
"""
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "culture_coach.db")

if os.path.exists(db_path):
    print(f"Migrating database at {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if email column exists
        cursor.execute("PRAGMA table_info(users)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'email' not in columns and 'username' in columns:
            print("Renaming username column to email...")
            # SQLite doesn't support ALTER COLUMN, so we need to recreate the table
            cursor.execute("""
                CREATE TABLE users_new (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email VARCHAR UNIQUE NOT NULL,
                    hashed_password VARCHAR NOT NULL
                )
            """)
            
            # Copy data from old table
            cursor.execute("""
                INSERT INTO users_new (id, email, hashed_password)
                SELECT id, username, hashed_password FROM users
            """)
            
            # Drop old table and rename new one
            cursor.execute("DROP TABLE users")
            cursor.execute("ALTER TABLE users_new RENAME TO users")
            
            conn.commit()
            print("Migration completed successfully!")
        elif 'email' in columns:
            print("Database already has email column. No migration needed.")
        else:
            print("Database structure unexpected. Creating fresh database.")
            cursor.execute("DROP TABLE IF EXISTS users")
            conn.commit()
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()
else:
    print(f"Database not found at {db_path}. Will be created on first run.")
