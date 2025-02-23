# WeatherDB
A Flask-based API for managing countries, cities, and temperature records.
 
 Uses a PostgreSQL database, SQLAlchemy ORM, and Docker Compose for container orchestration. 
 The API includes endpoints for creating, reading, updating, and deleting entries for countries, cities, and temperatures, all exposed via separate controller and route files. 
 The database schema is defined in SQL (with tables for “Tari,” “Orase,” and “Temperaturi”), and the Docker setup includes services for the API, PostgreSQL, and pgAdmin.
