#
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./server /code/server

# cmd to run uvicorn server in container, would be typed in CLI, import server from server.main
CMD ["uvicorn", "server.main:server", "--host", "0.0.0.0", "--port", "80"]


# building the docker image
# run in app path, docker build -t EEAimage .

# start docker container
# docker run -d --name EEAcontainer -p 80:80 EEAimage

# navigate to api docs
# http://192.168.99.100/docs
