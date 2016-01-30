FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code
ADD ./requirements/* /code/requirements/
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
