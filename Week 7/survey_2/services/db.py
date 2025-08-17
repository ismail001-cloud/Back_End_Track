import sqlite3
from config.configuration import DATABASE

def get_db_connection():
    """
    create and return a connection to the SQlite database.
    the Row_factory setting allows query results to be accessed as dictionaries.
    """

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():

    try:


        conn = get_db_connection()
        cursor = conn.cursor()

        # Create the agents table.
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS agents (
                                agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                email TEXT,
                                phone TEXT
                            )
                        """)
        print("[INFO] Agents table created successfully.")

        # Create the clients table with a foreign key reference to the agents table.
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS clients (
                                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                agent_id INTEGER,
                                name TEXT NOT NULL,
                                phone TEXT,
                                email TEXT,
                                NIN INTEGER,
                                driver_license TEXT,
                                lga TEXT,
                                address TEXT,
                                State TEXT,
                                education TEXT,
                                business TEXT,
                                gender TEXT,
                                FOREIGN KEY(agent_id) REFERENCES agents(agent_id)
                            )
                        """)
        print("[INFO] Clients table created successfully.")

        # Create the questions table with a foreign key reference to the agents table.
        cursor.execute("""
                                CREATE TABLE IF NOT EXISTS questions (
                                    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT
                                )
                            """)
        print("[INFO] Questions table created successfully.")

        # Create the answers table with a foreign key reference to the questions table.
        cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS answers (
                                        answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        question_id INTEGER,
                                        name TEXT,
                                        FOREIGN KEY (question_id) REFERENCES answers(answer_id) 
    
                                    )
                                """)
        print("[INFO] Answers table created successfully.")

        # Create the responses table with foreign keys reference to the clients table and questions table .
        cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS response (
                                        response_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        agent_id INTEGER,
                                        client_id INTEGER,
                                        question_id INTEGER,
                                        answer_id INTEGER,
                                        name TEXT,
                                        FOREIGN KEY(agent_id) REFERENCES agents(agent_id),
                                        FOREIGN KEY(client_id) REFERENCES clients(client_id),
                                        FOREIGN KEY(question_id) REFERENCES questions(question_id),
                                        FOREIGN KEY(answer_id) REFERENCES answers(answer_id)
                                    )
                                """)
        print("[INFO] Responses table created successfully.")

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"[ERROR] Database initialization failed: {e}")



