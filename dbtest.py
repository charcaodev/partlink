import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="charcao",
        password="admin",
        dbname="postgres"
    )

    print("Connection successful!")

    cur = conn.cursor()
    cur.execute("SELECT 1;")
    print(cur.fetchone())

    cur.execute("SELECT * FROM users LIMIT 10;")
    print(cur.fetchall())

    conn.close()

except Exception as e:
    print("Connection failed:")
    print(e)