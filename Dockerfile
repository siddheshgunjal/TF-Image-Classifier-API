FROM python:3.10-slim

RUN apt-get update \
 && apt-get install -y locales \
 && apt-get update \
 && dpkg-reconfigure -f noninteractive locales \
 && locale-gen C.UTF-8 \
 && /usr/sbin/update-locale LANG=C.UTF-8 \
 && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
 && locale-gen \
 && apt-get install -y curl unzip \
 && apt-get clean \
 && apt-get autoremove

# Creating Application Source Code Directory
RUN mkdir -p /usr/src/app

# Setting Home Directory for containers
WORKDIR /usr/src/app

# Copying src code to Container
COPY . /usr/src/app

# install all dependancies
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod -R 777 /usr/src/app/Data/npy_train_data
RUN chmod -R 777 /usr/src/app/Data/Train_Data
RUN chmod -R 777 /usr/src/app/Input
RUN chmod -R 777 /usr/src/app/Model
RUN chmod -R 777 /usr/src/app/static
RUN chmod -R 777 /usr/src/app/templates
RUN chmod -R 777 /usr/src/app/test_images
RUN chmod -R 777 /usr/src/app
RUN chmod -R 777 /usr/src

# Application Environment variables
#ENV APP_ENV development
ENV PORT 8188

# Exposing Ports
EXPOSE $PORT

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application
CMD gunicorn -b :$PORT -c gunicorn.conf.py app:app
