FROM node:5
RUN mkdir /code
WORKDIR /code
RUN npm install -g angular-cli
ADD ./package.json /code/package.json
RUN npm install
ADD . /code/
# RUN python manage.py collectstatic
