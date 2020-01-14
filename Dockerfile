FROM python:3.7


MAINTAINER Caroline <caroline.fang.cc@gmail.com>

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app/main.py" ]