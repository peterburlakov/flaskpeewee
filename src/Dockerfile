FROM python:3.6-alpine

RUN mkdir /src
WORKDIR /src

# Install pip reqs as separate step for caching
COPY requirements.txt /src/
RUN pip3 install -r requirements.txt

COPY . /src/