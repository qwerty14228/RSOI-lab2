FROM python:3-alpine 

ARG SERVICE

RUN mkdir -p /app

WORKDIR /app

COPY src/rsoi_${SERVICE} .

RUN pip3 install -r requirements.txt && python3 manage.py migrate

CMD ["sh", "run.sh"]
