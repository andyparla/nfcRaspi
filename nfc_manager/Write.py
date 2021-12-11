import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class Write:
    def __init__(self):
        self.reader = SimpleMFRC522()

    def grabado(self):
        try:
            text = input('New data:')
            print("Now place your tag to write")
            self.reader.write(text)
            print("Written")
        finally:
            GPIO.cleanup()
