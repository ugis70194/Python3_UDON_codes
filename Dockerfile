FROM python:3.9.7

ARG UID=1000
RUN useradd -m -u ${UID} docker
USER docker
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /home/docker/work
EXPOSE 8080
