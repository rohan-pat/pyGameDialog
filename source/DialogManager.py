from SpeechRec import getSpeechText
from FrameSlot import FrameSlot
from LanguageClassifier import langClassifier
from GameUI import start_thread

import threading
from multiprocessing import Queue

class DialogManager:

    def __init__(self):
        # initalizing all components of Dialog Systems.
        self.classifier = langClassifier()
        self.fs = FrameSlot()
        self.keyState = 0
        self.doorState = 0
        self.hammerState = 0
        self.greetingVar = 0
        self.action = ""
        self.buff = Queue()
        self.gameThread = threading.Thread(
        target=start_thread, args=(self.buff,))
        self.gameThread.start()

    def dialogManager(self):
        count = 0
        while True:
            #greet the user.
            if(self.greetingVar == 0):
                self.fs.greeting("gf")
                self.greetingVar = 1

            #talking input from the user.
            gotText = True
            while(gotText):
                text = getSpeechText()
                if(text not in [' ', '']):
                    gotText = False
                print("text is ", text)

            # getting the intent
            intent, entity = self.classifier.getIntent(text)
            print("Intent is ", intent, "Entity is ", entity)

            #changing the state.
            self.changeState(intent, entity)

            count = count + 1
            if(count == 5):
                break

        # killing the game thread
        self.gameThread.join()

    def changeState(self, intent, entity):
        # checking for picking stuff.
        print("Intent is ", intent, "Entity is ", entity)

        if(intent == "possession"):
            if(entity == "key"):
                if(self.keyState == 0):
                    self.keyState=1
                    self.action="pk"
                    self.fs.possession(self.action)
                elif(self.keyState == 1):
                    self.action="pka"
                    self.fs.possession(self.action)
            elif(entity == "hammer"):
                if(self.hammerState == 0):
                    self.hammerState=1
                    self.action="ph"
                    self.fs.possession(self.action)
                elif(self.hammerState == 1):
                    self.action="pha"
                    self.fs.possession(self.action)
            elif(entity == "empty"):
                self.action="pui"
                self.fs.possession(self.action)

        # checking for dropping stuff.
        elif(intent == "release"):
            if(entity == "key"):
                if(self.keyState == 1):
                    self.keyState=0
                    self.action="rk"
                    self.fs.release(self.action)
                elif(self.keyState == 0):
                    self.action="rka"
                    self.fs.release(self.action)
            elif(entity == "hammer"):
                if(self.hammerState == 1):
                    self.hammerState=0
                    self.action="rh"
                    self.fs.release(self.action)
                elif(self.hammerState == 0):
                    self.action="rha"
                    self.fs.release(self.action)
            elif(entity == "empty"):
                self.action="rui"
                self.fs.release(self.action)
            else:
                self.action="rui"
                self.fs.release(self.action)
        # checking for unlocking door.
        elif(intent == "unlock"):
            if(entity == "door"):
                if(self.doorState == 0):
                    if(self.keyState == 1):
                        self.doorState=1
                        self.action="ud"
                        self.fs.unlock(self.action)
                    elif(self.keyState == 0):
                        self.action="udnk"
                        self.fs.unlock(self.action)
                elif(self.doorState == 1):
                    self.action="dao"
                    self.fs.unlock(self.action)
            elif(entity == "empty"):
                self.action="dui"
                self.fs.unlock(self.action)

        # break the door.
        elif(intent == "break"):
            if(entity == "door"):
                if(self.doorState == 0):
                    if(self.hammerState == 1):
                        self.doorState=1
                        self.action="bd"
                        self.fs.Break(self.action)
                    elif(self.hammerState == 0):
                        self.action="bdnk"
                        self.fs.Break(self.action)
                elif(self.doorState == 1):
                    self.action="dab"
                    self.fs.Break(self.action)
            elif(entity == "empty"):
                self.action="dui"
                self.fs.Break(self.action)

        # undefined action.
        elif(intent == "undefined"):
            self.action="ud"
            self.fs.undefined(self.action)

        elif(intent == "greeting"):
            if(self.greetingVar == 1):
                self.action="ga"
                self.fs.greeting(self.action)

        elif(intent == "goodbye"):
            self.action="gb"
            self.fs.goodbye(self.action)
        else:
            print("Unrecognized Intent!")

        self.buff.put(self.action)

# testing functions.
if __name__ == '__main__':
    d = DialogManager()
    d.dialogManager()
    del d
