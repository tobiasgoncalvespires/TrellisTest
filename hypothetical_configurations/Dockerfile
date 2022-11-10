FROM python:3.9

WORKDIR /usr/app

RUN git clone https://github.com/tobiasgoncalvespires/TrellisTest.git
RUN apt-get -qq update
RUN apt-get -y install supervisor 
RUN apt-get -y install python3.9
RUN apt-get -y install python-setuptools 
RUN apt-get -y install nginx 

RUN pip3 install --upgrade pip setuptools
RUN pip3 install --no-cache-dir -r /usr/app/trellis/requirements.txt

COPY ./supervisor.conf /etc/supervisor/conf.d/supervisor.conf
COPY ./nginx.conf /etc/nginx/sites-available/default

ENV TRELLIS_DJANGO_SECRET_KEY="Any django secret key"
ENV DJANGO_DEBUG=False

RUN mkdir /logs
EXPOSE 8081

CMD ["supervisord", "-n", "--logfile", "/logs/supervisor_log.txt"]
