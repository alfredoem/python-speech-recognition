import speech_recognition as sr

filename = "media/audio1.wav"
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language='en-US', show_all=True)
    # response = json.loads(text)
    print(text)
    print('Stract')
    print(text['alternative'][0]['transcript'])
