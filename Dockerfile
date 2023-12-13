FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY .env /.
COPY ./server /code/server

WORKDIR /code/server

# cmd to run uvicorn server in container, would be typed in CLI, import server from server.main
EXPOSE 8000
CMD ["uvicorn", "main:server", "--reload", "--host", "0.0.0.0", "--port", "8000"]


## Installing Docker

# Depending on your operating system, follow the specific link at https://docs.docker.com/compose/install/

## Running Docker/API server

# After installing Docker, cd into eventexperenceapp. Run docker compose up.

# When done with testing, run docker compose down. This will free up some resources on your computer

# navigate to api docs
# http://localhost:8000/docs


