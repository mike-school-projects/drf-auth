# LAB - Class 33

## Project: Authentication and Production Server

### Features - Django
- Add JWT Authentication to your API
- Keep any pre-existing authentication so DRF Browsable API still usable. 
- Install needed libraries in project configuration and/or site settings.

### Features - Docker
- Switch to using Gunicorn instead of Django's built-in development server 
- Mind the number of workers to avoid sluggishness
- On Django side you'll need to properly handle static files using Whitenoise

### Storage Options
- Your choice of SQLite or PostgreSQL
- Adjust docker-compose.yml so that data is persisted in a volume outside of container
- These steps are different depending on whether SQLite or PostgreSQL is being used


## Author: Mike Shen

## Links and Resources
N/A 

##  Setup

docker compose up --build

Need to set up .env file in project folder for Django secret key.  See .env.sample

# How to initialize/run your application (where applicable)

1. Build docker container: docker compose up --build
2. With docker running: docker compose run web python manage.py migrate
3. With docker running: docker compose run web python manage.py createsuperuser


Routes:
1. Get a token: http post localhost:8000/api/token/ username=admin password=YOUR_PASSWORD 
2. Refresh token: http post localhost:8000/api/refresh/ refresh=REFRESH_TOKEN_HERE 
3. Roster list: http localhost:8000/api/v1/app/ "Authorization: Bearer ACCESS_TOKEN_HERE"
4. Roster detail: http localhost:8000/api/v1/app/{pk} "Authorization: Bearer ACCESS_TOKEN_HERE"
- where {pk} is the primary key of the player
5. Admin: http://localhost:8000/admin



## How to use your library (where applicable)

## Tests

None required
