FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
ENV TIMEZONE=America/Sao_Paulo
ENV POSTGRES_PASSWORD=masterpass
ENV POSTGRES_USER=userdb
ENV POSTGRES_DB=callcenter
ENV POSTGRES_PORT=5432
ENV POSTGRES_HOST=database

RUN mkdir -p /source
WORKDIR /source
ADD requirements.txt /source/
RUN pip install -r requirements.txt