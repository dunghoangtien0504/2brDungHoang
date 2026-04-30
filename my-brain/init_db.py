import sqlite3
import datetime
import os

def create_database():
    db_path = "brain.db"
    
    # Connect to SQLite (this will create the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create 'knowledge' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create 'business' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS business (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create 'brand_voice' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS brand_voice (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Sample Data for 'knowledge'
    knowledge_samples = [
        ("Mental Models", "Insight on first principles thinking: break down complex problems into basic elements and then reassemble them from the ground up."),
        ("Productivity System", "The 2-Minute Rule: If it takes less than two minutes, then do it now. A simple heuristic to avoid procrastination.")
    ]

    # Sample Data for 'business'
    business_samples = [
        ("Customer Profile: Tech Founders", "Target audience mainly consists of early-stage tech founders looking for automated productivity solutions."),
        ("Product Launch V1", "Core product features for V1 include AI-powered note-taking and seamless Notion integration. Pricing set to $10/mo.")
    ]

    # Sample Data for 'brand_voice'
    brand_voice_samples = [
        ("Professional Tone", "Use a direct, clear, and professional tone. Avoid jargon where possible. Be concise and authoritative."),
        ("Friendly Style", "When addressing support issues, adopt a warm and empathetic style. Start with acknowledging the user's frustration.")
    ]

    # Insert Sample Data function
    def insert_samples(table_name, samples):
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        if cursor.fetchone()[0] == 0:
            for sample in samples:
                cursor.execute(f'''
                    INSERT INTO {table_name} (title, content, created_at)
                    VALUES (?, ?, ?)
                ''', (sample[0], sample[1], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    insert_samples("knowledge", knowledge_samples)
    insert_samples("business", business_samples)
    insert_samples("brand_voice", brand_voice_samples)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Database '{db_path}' initialized successfully with tables and sample data.")

if __name__ == "__main__":
    create_database()
