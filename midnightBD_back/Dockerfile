FROM python:3.11-alpine

WORKDIR /server

COPY requirements.txt /server
RUN pip install -r requirements.txt

RUN ls -lah

ENTRYPOINT [ "flask", "--app", "new_server", "run", "--host=0.0.0.0", "--port=7900", "--debug"]
