from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a== stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a" ) as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    #musicloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_excercise = time()
    watersecs =5
    exesecs=10
    eyesecs=20


    while True:
        if time() - init_water >watersecs:
            print("Water drinking time.Enter 'drank ' to stop alarm.")
            musicloop("water.mp3",'drank')
            init_water = time()
            log_now("Drank water at")
            print("If you want to quit press Q else press N")
            q = input()
            if q == "q":
                exit()

        if time() - init_eyes >eyesecs:
            print("eye relief  time.Enter 'maa' to stop alarm.")
            musicloop("water.mp3",'maa')
            init_eyes = time()
            log_now("Eyes relief at")
            print("If you want to quit press Q else press N")
            q = input()
            if q == "q":
                exit()

        if time() - init_excercise >exesecs:
            print("kasarat time.Enter 'chal ' to stop alarm.")
            musicloop("water.mp3",'chal')
            init_excercise= time()
            log_now("excersice at")
            print("If you want to quit press Q else press N")
            q = input()
            if q == "q":
                exit()

