FROM python:3.11.11

COPY . /srv/www

WORKDIR /srv/www

RUN pip install -r requirements.txt

CMD ["gunicorn","-w","4","app:app","--bind=0.0.0.0:5001"]
