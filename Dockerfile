FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code
ADD ./requirements/* /code/requirements/
ADD ./requirements* /code/
RUN pip install -r requirements.txt
RUN pip install -r requirements/development.txt
ADD . /code/
