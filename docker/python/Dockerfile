FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD [ "python", "./run.py" ]
CMD [ "uwsgi", "--ini", "app.ini", "--py-autoreload", "1", "--touch-reload", "blog" ]
