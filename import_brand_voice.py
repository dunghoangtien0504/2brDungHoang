import sqlite3
import re
import os

def import_brand_voice():
    db_path = 'brain.db'
    md_path = 'Brand_Voice.md'
    
    if not os.path.exists(md_path):
        print(f"File {md_path} not found.")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data_to_insert = []

    # 1. Try to parse the specific payload block if it exists
    # Looking for the code block after BRAND VOICE PAYLOAD
    payload_match = re.search(r'BRAND VOICE PAYLOAD.*?```(.*?)```', content, re.DOTALL | re.IGNORECASE)
    if payload_match:
        payload_text = payload_match.group(1)
        # Split by === TITLE: ... ===
        entries = re.split(r'===\s*TITLE:\s*(.*?)\s*===', payload_text)
        # The first element is usually intro text
        for i in range(1, len(entries), 2):
            title = entries[i].strip()
            body = entries[i+1].strip()
            if title and body:
                data_to_insert.append((title, body))
        print("Found and processed 'BRAND VOICE PAYLOAD' section.")

    # 2. Grab main sections for detail
    main_sections = re.split(r'###\s+', content)
    existing_titles_lower = {t.lower() for t, b in data_to_insert}
    
    for section in main_sections:
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        full_title = lines[0].strip()
        # Clean title for comparison
        clean_title = re.sub(r'[^\w\s]', '', full_title).strip()
        
        # Skip internal payload references
        if "BRAND VOICE PAYLOAD" in full_title.upper():
            continue
            
        body = '\n'.join(lines[1:]).strip()
        
        # Add if not already roughly covered
        if clean_title and body:
            # Check if title is already in data_to_insert
            if clean_title.lower() not in existing_titles_lower:
                body = re.sub(r'\n{3,}', '\n\n', body)
                data_to_insert.append((full_title, body))
                existing_titles_lower.add(clean_title.lower())

    if not data_to_insert:
        print("No suitable data found in markdown file.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS brand_voice (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute("DELETE FROM brand_voice")
    cursor.executemany("INSERT INTO brand_voice (title, content) VALUES (?, ?)", data_to_insert)
    
    conn.commit()
    conn.close()
    print(f"Success: Imported {len(data_to_insert)} items into brand_voice table.")

if __name__ == "__main__":
    import_brand_voice()
