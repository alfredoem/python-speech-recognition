FROM python:3

WORKDIR /usr/src/app

RUN apt-get update

RUN apt-get install -y portaudio19-dev python3-pyaudio python3-tk

RUN apt-get install -y pulseaudio

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./scripts/command.py" ]