#!C:\Python37\python.exe
print("Content-type: text/html\n\n")
print('<h1>Results</h1>')

import speech_recognition as sr

r = sr.Recognizer()
with sr.WavFile("C:\\Apache24\\htdocs\\speech\\myDir\\result.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("<h1>Transcription: " + str(r.recognize_google(audio,language='en-US', show_all=True))+"</h1>")   # recognize speech using Google Speech Recognition
except LookupError:                                 
    print("<h1>Could not understand audio</h1>")