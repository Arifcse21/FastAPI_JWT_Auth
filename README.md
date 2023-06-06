# FastAPI with JWT Auth
In this project, PostgreSQL database is used. I deployed the database on docker. you can do so by:

`docker run -d --name psql_fastapi -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_DB=postgres -p 5432:5432 postgres`

### Create and activate virtual environment(if you don't have already)

`python -m venv venv`

`source venv/bin/activate`

### Install required packages

`pip install -r requirements.txt`

