from gtts import gTTS
import pygame
from pygame import mixer
from tempfile import TemporaryFile

class FrameSlot:

    def textToSpeech(self, msg):
        #print(msg)
        tts = gTTS(text=msg, lang='en')
        #print(text)
        tts.save("rec.mp3")
        mixer.init()
        mixer.music.load("rec.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pygame.time.Clock().tick(2)

    def greeting(self, action):
        if(action == "gf"):
            msg = "Hello, Would "
            self.textToSpeech(msg)
        elif(action == "ga"):
            msg= "well hello again"
            self.textToSpeech(msg)

    def possesion(self, action):
        if(action == "pk"):
            msg="You picked up the key"
            self.textToSpeech(msg)
        elif(action == "pka"):
            msg="You already have the key"
            self.textToSpeech(msg)
        elif(action == "ph"):
            msg="You picked up the hammer"
            self.textToSpeech(msg)
        elif(action == "pha"):
            msg="You already have the hammer"
            self.textToSpeech(msg)
        elif(action == "pui"):
            msg="The item could not be located"
            self.textToSpeech(msg)

    def release(self, action):
         if(action == "rk"):
             msg="You dropped the key"
             self.textToSpeech(msg)
         elif(action == "rka"):
             msg="You do not have the key "
             self.textToSpeech(msg)
         elif(action == "rh"):
             msg="You dropped the hammer"
             self.textToSpeech(msg)
         elif(action == "rha"):
             msg="You do not have the hammer with you"
             self.textToSpeech(msg)
         elif(action == "rui"):
             msg="You do not have the item"
             self.textToSpeech(msg)

    def unlock(self, action):
        if(action == "ud"):
            msg="You opened the door"
            self.textToSpeech(msg)
        elif(action == "udnk"):
            msg="You do not have the key to open the door"
            self.textToSpeech(msg)
        elif(action == "dao"):
            msg="The door is already open"
            self.textToSpeech(msg)
        elif(action == "dui"):
            msg="The item cannot be found"
            self.textToSpeech(msg)

    def Break(self, action):
        if(action == "bd"):
            msg="You opened the door"
            self.textToSpeech(msg)
        elif(action == "bdnk"):
            msg="You do not have the hammer"
            self.textToSpeech(msg)
        elif(action == "dab"):
            msg="The door is already open"
            self.textToSpeech(msg)
        elif(action == "dui"):
            msg="The item cannot be found"
            self.textToSpeech(msg)

    def undefined(self, action):
        if(action == "ud"):
            msg="You cannot do that"
            self.textToSpeech(msg)

    def goodbye(self, action):
        if(action == "gb"):
            msg="Good bye"
            self.textToSpeech(msg)

if __name__ == "__main__":
    fs = FrameSlot()
    fs.Break("bd")
