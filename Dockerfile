FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./server /code/server

WORKDIR /code/server

# cmd to run uvicorn server in container, would be typed in CLI, import server from server.main
EXPOSE 8000
CMD ["uvicorn", "main:server", "--reload", "--host", "0.0.0.0", "--port", "8000"]

# building the docker image
# run in app path, docker build -t eeaimage .
# start docker container
# docker run -d --name eeacontainer -p 8000:8000 eeaimage
# navigate to api docs
# http://localhost:8000/docs
