#imports
import sounddevice as sd
import torch
import os
import time
import numpy

from config import nums
from datetime import datetime
from phrases import get_hello, get_mood, get_bye, get_league

#main preparations
device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                   local_file)  

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

example_text  = 'Привет, Петя. Программа запущена.'
sample_rate   = 48000

#functions to import

class Katya:
    speaker      = 'baya'
    sample_rate  = 48000
    greet = "Программа запущена. Сигнал микрофона обрабатывается."

    def start(self):
        audio = model.apply_tts(text        = greet,
                                speaker     = self.speaker,
                                sample_rate = self.sample_rate)
    
        sd.play(audio, sample_rate)
        time.sleep(len(audio)/sample_rate)
        sd.stop()

    def hello_say(self):
        audio = model.apply_tts(text        = get_hello(),
                                speaker     = self.speaker,
                                sample_rate = self.sample_rate)
    
        sd.play(audio, sample_rate)
        time.sleep(len(audio)/sample_rate)
        sd.stop()



    def mood_say(self):
        audio = model.apply_tts(text        = get_mood(),
                                speaker     = self.speaker,
                                sample_rate = self.sample_rate)
    
        sd.play(audio, sample_rate)
        time.sleep(len(audio)/sample_rate)
        sd.stop()
    
    def bye_say(self):
        audio = model.apply_tts(text        = get_bye(),
                                speaker     = self.speaker,
                                sample_rate = self.sample_rate)
    
        sd.play(audio, sample_rate)
        time.sleep(len(audio)/sample_rate)
        sd.stop()

    def time_say(self):

        ctime  = datetime.now()
        hour   = nums.get(str(ctime.hour))
        minute = nums.get(str(ctime.minute))

        print(hour)
        print(minute)

        text = f'Сейчас {hour} часов {minute} минут'
        print(text)

        audio = model.apply_tts(text        = text,
                                speaker     = self.speaker,
                                sample_rate = self.sample_rate)

        sd.play(audio, sample_rate)
        time.sleep(len(audio)/sample_rate)
        sd.stop()

    def lol_turn(self):
        os.startfile('D:\LOL\Riot Games\Riot Client\RiotClientServices.exe')

        audio = model.apply_tts(text        = get_league(),
                                speaker     = self.speaker,
                                sample_rate = self.sample_rate)

        sd.play(audio, sample_rate)
        time.sleep(len(audio)/sample_rate)
        sd.stop()
