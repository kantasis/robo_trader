FROM python:3.11

RUN apt-get update
RUN pip install alpaca-py
RUN pip install --upgrade openai

CMD ["tail", "-f", "/dev/null"]
