FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
ENV TIMEZONE=America/Sao_Paulo
ENV POSTGRES_PASSWORD=masterpass
ENV POSTGRES_USER=userdb
ENV POSTGRES_DB=call_project
ENV POSTGRES_PORT=5432
ENV POSTGRES_HOST=database

# Source settings
RUN rm -rf /source
RUN mkdir -p /source
COPY requirements.txt /source/

#Requirements settings
RUN apt install tzdata
RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN pip install -r /source/requirements.txt

WORKDIR /source
