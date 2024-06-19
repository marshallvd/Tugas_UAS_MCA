import mysql.connector
from mysql.connector import errorcode

# Koneksi ke database MySQL
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_tele'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Membuat tabel tb_inbox
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_inbox (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id VARCHAR(100) NOT NULL,
        message TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Membuat tabel tb_outbox
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_outbox (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id VARCHAR(100) NOT NULL,
        message TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Commit perubahan
    conn.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    conn.close()
