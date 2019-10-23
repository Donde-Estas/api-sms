FROM python:3.8
RUN apt-get update -qq && apt-get install -y postgresql-client
RUN mkdir /myapp
WORKDIR /myapp
COPY requirements.txt /myapp/requirements.txt
RUN pip install -r requirements.txt
COPY . /myapp

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
