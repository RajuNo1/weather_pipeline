def insert_weather_to_db(data):
    conn = psycopg2.connect(host='localhost', dbname='weatherdb', user='user', password='pass')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR,
            timestamp TIMESTAMP,
            temp_c FLOAT,
            humidity INT,
            weather VARCHAR
        )
    """)
    cur.execute("""
        INSERT INTO weather_data (city, timestamp, temp_c, humidity, weather)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['city'], data['timestamp'], data['temp_c'], data['humidity'], data['weather']))
    conn.commit()
    cur.close()
    conn.close()
