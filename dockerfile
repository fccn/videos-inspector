FROM python:3.13-slim

WORKDIR project

RUN apt update -y && apt upgrade -y

COPY requirements.txt /project

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

COPY app /project

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]