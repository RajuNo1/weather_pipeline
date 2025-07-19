# Weather Monitoring Data Pipeline

This project builds a real-time weather monitoring data pipeline using:
- OpenWeatherMap API
- Kafka for streaming
- PostgreSQL for storage
- Metabase for visualization

## Features
- Streams weather data via Kafka every 5 minutes
- Stores processed data in PostgreSQL
- Visualizes trends using Metabase

## Setup Instructions
1. Clone the repo
2. Add your OpenWeatherMap API key in `producer.py`
3. Run the stack:
```bash
docker compose up --build
