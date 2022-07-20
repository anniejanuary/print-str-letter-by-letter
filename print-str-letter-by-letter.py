#ma wyswietlac kolejne litery tekstu z danym opoznieniem

import time

def str(text,delay=0.5):
    for x in text: 
        print(x,end=' ' )
        time.sleep(delay)
napis("Hello")
