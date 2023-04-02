FROM python:3.10

ENV PYTHONUNBUFFERED 1

ARG PORT
ENV PORT ${PORT:-8000}

WORKDIR /app

# install requirements
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY . /app

CMD ["/docker-entrypoint.sh"]
