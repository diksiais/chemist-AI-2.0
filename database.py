# database.py
import sqlite3
import os

DATABASE_FILE = "data/search_history.db" # Database file will be in a 'data' subfolder

def init_db():
    """
    Initializes the SQLite database and creates the search_history table if it doesn't exist.
    """
    # Ensure the 'data' directory exists
    os.makedirs(os.path.dirname(DATABASE_FILE), exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            topic TEXT NOT NULL,
            goal TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_search_history(topic, goal, data):
    """
    Saves a new search entry to the database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO search_history (topic, goal, data) VALUES (?, ?, ?)",
        (topic, goal, data)
    )
    conn.commit()
    conn.close()

def load_search_history():
    """
    Loads all search history entries from the database, ordered by timestamp descending.
    Returns a list of dictionaries.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, timestamp, topic, goal, data FROM search_history ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            "id": row[0],
            "timestamp": row[1],
            "topic": row[2],
            "goal": row[3],
            "data": row[4]
        })
    return history

def delete_search_history_entry(entry_id):
    """
    Deletes a specific search history entry by its ID.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM search_history WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

def clear_all_search_history():
    """
    Deletes all entries from the search_history table.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM search_history")
    conn.commit()
    conn.close()
