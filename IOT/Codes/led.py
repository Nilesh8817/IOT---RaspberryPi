import RPi.GPIO as G

from time import sleep

G.setmode(G.BOARD)

ledPin = 3

G.setup(ledPin, G.OUT)

G.output(ledPin, False)

while True:
    G.output(ledPin, True)
    sleep(1)
    G.output(ledPin, False)
    sleep(0.05)
G.cleanup()
