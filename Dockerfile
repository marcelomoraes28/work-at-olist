 FROM python:3
 ENV PYTHONUNBUFFERED 1
 MKDIR source
 WORKDIR /source
 ADD requirements.txt /source/
 RUN pip install -r requirements.txt
 ADD . /source/