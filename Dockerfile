FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /schmsoft

WORKDIR /schmsoft

ADD . /schmsoft/

RUN pip install -r requirements.txt

RUN mkdir -p /root/.ipython/profile_default/startup
COPY ./config/ipython_startup_conf.py /root/.ipython/profile_default/startup/startup.py

RUN ./manage.py collectstatic --noinput

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE 'schmsoft.settings.prod'
