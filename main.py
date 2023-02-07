#imports
from VPrep import listen
from SPrep import Katya
from config import greetings, time_asks, mood_asks, bye_asks, deletings, league_asks

KNames = ["катя","екатерина","кать","катюша","катюш","катенька"]

goodbye = False
KSleep = False

katya = Katya()

while not goodbye:
    ask = listen()

    katya.start()

    if any(name in ask for name in KNames):
        

        katya.hello_say() if any(greet in ask for greet in greetings) else print('Quiet')
        
        katya.mood_say() if any(mood in ask for mood in mood_asks) else print("Quiet")

        katya.time_say() if any(time in ask for time in time_asks) else print("Quiet")

        katya.lol_turn() if any(lol in ask for lol in league_asks) else print('Quiet')

        if any(bye in ask for bye in bye_asks):
            goodbye = True

        print(ask)


    print(ask)
    print(f'quiet')

