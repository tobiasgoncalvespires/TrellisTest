FROM python:3.9

COPY ./trellis/requirements.txt ./

RUN apt-get -qq update
RUN apt-get install -y python3.9 python-setuptools supervisor libaio1 nginx libnss3
RUN pip3 install --upgrade pip setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

ENV TRELLIS_DJANGO_SECRET_KEY="Any django secret key"
ENV DJANGO_DEBUG=False

WORKDIR /trellis
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
EXPOSE 80

CMD ["supervisord", "-n", "--logfile", "/log_supervisor.txt"]
