FROM python:3

WORKDIR /usr/src/app


COPY requirements.txt /usr/src/app/
COPY config/config.ini /usr/src/app/
COPY config/dns-binding.conf /usr/src/app/
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV REPEAT_TIMER 60
ENV CONF_FILE  /usr/src/app/config.ini

CMD [ "/usr/src/app/docker-entrypoint.sh", "/usr/src/app/dns-binding.conf" ]

