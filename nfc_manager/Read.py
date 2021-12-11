import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Read:
    def __init__(self):
        self.reader = SimpleMFRC522()

    def lectura(self):
        try:
                id, text = self.reader.read()
                print(id)
                print(text)
        finally:
                GPIO.cleanup()