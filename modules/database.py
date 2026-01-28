import sqlite3

class DatabaseManager:
    def __init__(self, db_name="siem.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_ip TEXT,
            event_type TEXT,
            timestamp TEXT,
            raw_message TEXT
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def insert_log(self, data):
        query = "INSERT INTO logs (source_ip, event_type, timestamp, raw_message) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (
            data['source_ip'], 
            data['event_type'], 
            data['timestamp'], 
            data['raw']
        ))
        self.conn.commit()