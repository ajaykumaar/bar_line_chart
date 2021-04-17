from python:3.7-slim-stretch


WORKDIR /bar_line_chart

ADD . /bar_line_chart

RUN pip install -r requirements.txt


