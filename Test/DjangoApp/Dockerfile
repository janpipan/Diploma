FROM ubuntu:20.04
RUN apt-get update && apt-get install -y tzdata && apt install -y python3.8 python3-pip
RUN apt install python3-dev libpq-dev nginx -y
ADD djangodatabase requirements.txt run.sh /app/
WORKDIR /app/
RUN pip install -r requirements.txt
EXPOSE 8000