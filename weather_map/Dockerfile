FROM python:3.8

RUN apt-get update && apt-get install -y firefox-esr

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz
RUN tar -x geckodriver -zf geckodriver-v0.23.0-arm7hf.tar.gz -O > /usr/bin/geckodriver
RUN chmod +x /usr/bin/geckodriver
RUN rm geckodriver-v0.23.0-arm7hf.tar.gz

COPY . /app
WORKDIR /app/weather_map
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["start.py"]
ENTRYPOINT ["python3"]
