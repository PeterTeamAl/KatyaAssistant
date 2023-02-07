#imports
import pyaudio

from vosk import Model, KaldiRecognizer

#Making Vosk preparations
model = Model('vosk-model-small-ru-0.22')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, 
                channels = 1, 
                rate = 16000,
                input=True,
                frames_per_buffer=8000)
stream.start_stream()

#making functions to import



def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if(rec.AcceptWaveform(data)) and (len(data)>0):
            answer = rec.Result()
            return answer



