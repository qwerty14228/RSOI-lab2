FROM python:3-alpine 

ARG SERVICE

RUN mkdir -p /app

WORKDIR /app

COPY src/rsoi_${SERVICE}/requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY src/rsoi_${SERVICE} .

CMD ["sh", "run.sh"]
