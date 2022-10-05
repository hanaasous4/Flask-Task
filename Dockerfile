FROM centos:7

WORKDIR /app
RUN yum -y update
RUN yum -y install python3-pip
RUN pip3 install Flask
COPY . /app
CMD [ "python3", "./app.py" ]
