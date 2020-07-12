FROM python:3.6
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install nodejs -y
RUN apt-get install npm -y
COPY requirements/ /usr/src/app/requirements/
RUN pip install -r requirements/common.txt  -r requirements/jenkins.txt
COPY . /usr/src/app
RUN npm install
RUN npm install -g bower