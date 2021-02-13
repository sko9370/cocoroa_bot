FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir discord python-dotenv

COPY . .

CMD [ "python3", "bot.py" ]
