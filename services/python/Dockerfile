FROM python:3.11

# Don't use the 3.12 version. It's new and doesn't work well with kafka.
# FROM python:3.12

# COPY *.py /scripts/

ARG ALPACA_ENDPOINT
ENV ALPACA_ENDPOINT ${ALPACA_ENDPOINT}

ARG ALPACA_KEY
ENV ALPACA_KEY ${ALPACA_KEY}

ARG ALPACA_SECRET
ENV ALPACA_SECRET ${ALPACA_SECRET}

RUN apt-get update
RUN pip install alpaca-py

CMD ["tail", "-f", "/dev/null"]
