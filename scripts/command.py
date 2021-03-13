import speech_recognition as sr
import os
import unicodedata
import pyaudio
import wave

r = sr.Recognizer()
speech_lang = 'en-US'


def normalize(value):
    if not value:
        return value

    return unicodedata.normalize('NFKD', value.lower()).encode('ASCII', 'ignore')


def command(value):
    complete = True
    normalized = normalize(value).decode('ASCII')
    print('Normalized voice command: ' + normalized)
    if normalized == 'computadora abre opera':
        os.system("/usr/bin/opera")
    elif normalized == 'computadora abre el editor de texto':
        os.system("/usr/bin/gedit")
    elif normalized == 'computadora abre la calculadora':
        os.system("/usr/bin/gnome-calculator")
    else:
        comm = normalized.split(' ')[-1]
        print('Trying to open program: ' + comm)
        if not (os.path.exists('/usr/bin/' + comm)):
            complete = False
            computer_unable()

        os.system('/usr/bin/' + comm)

    return complete


def computer_unable():
    chunk = 1024

    wf = wave.open('./media/computer-unable2.wav', 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)

    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()


while True:
    print('Channel open...')
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=4)
        print("Listening finish...")
        text = r.recognize_google(audio_data, language=speech_lang, show_all=True)
        print('Google recognized text')
        print(text)
        if not text:
            computer_unable()

        for alt in text['alternative']:
            speech = alt['transcript']
            print('Speech alternative: ' + speech)
            if speech and command(speech):
                break
