# Weather Monitoring Data Pipeline (Open‑Meteo + Airflow)

This version uses **Open‑Meteo** and **Apache Airflow** for an **hourly extract**. Kafka has been removed for now and can be added later.

## What’s inside
- **PostgreSQL** for storage
- **Airflow** for hourly orchestration
- **Metabase** for dashboards
- **Open‑Meteo** as data source (free, no sign‑up)

## Quick start
1. Ensure Docker Desktop is running.
2. From the repo root, start everything:
   ```bash
   docker compose up --build
   ```
3. Open UIs:
   - Airflow: http://localhost:8080 (login: `admin` / `admin`)
   - Metabase: http://localhost:3000
4. In Airflow, toggle **`weather_pipeline`** on. It runs **hourly**.

## Configure Metabase
- Add a PostgreSQL connection: host `postgres`, port `5432`, db `weatherdb`, user `user`, pass `pass`.
- Explore table **`weather_data`**.

## Notes
- Open‑Meteo endpoint used: `https://api.open-meteo.com/v1/forecast?latitude=12.9716&longitude=77.5946&current_weather=true` (Bengaluru coords). Change lat/lon in `fetch_weather.py` if desired.
- Airflow container installs Python deps from `requirements.txt` on startup.

---
