import psycopg2
from psycopg2.extras import execute_values

DB_CFG = dict(host="postgres", dbname="weatherdb", user="user", password="pass")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    temp_c DOUBLE PRECISION,
    windspeed DOUBLE PRECISION,
    weathercode INT
);
CREATE INDEX IF NOT EXISTS idx_weather_ts ON weather_data(timestamp);
"""

INSERT_SQL = (
    "INSERT INTO weather_data (city, timestamp, temp_c, windspeed, weathercode) VALUES %s"
)

def insert_weather_to_db(record: dict):
    """Create table if needed and insert a single weather record."""
    conn = psycopg2.connect(**DB_CFG)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(SCHEMA_SQL)
                execute_values(cur, INSERT_SQL, [(
                    record["city"],
                    record["timestamp"],
                    record["temp_c"],
                    record["windspeed"],
                    record["weathercode"],
                )])
    finally:
        conn.close()
