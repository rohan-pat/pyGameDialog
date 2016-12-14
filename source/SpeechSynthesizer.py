import subprocess
from nltk.tokenize import sent_tokenize

def speakText(text, selection=1):
    sentList = sent_tokenize(text)
    for sent in sentList:
        if selection == 1:
            cmdText = "say --voice=samantha " + sent
            x = subprocess.check_call(cmdText, shell=True)
        elif selection == 2:
            cmdText = "say --voice=daniel " + sent
            x = subprocess.check_call(cmdText, shell=True)
        elif selection == 3:
            cmdText = "say --voice=kate " + sent
            x = subprocess.check_call(cmdText, shell=True)
        else:
            cmdText = "say --voice=samantha " + sent
            x = subprocess.check_call(cmdText, shell=True)

if __name__ == "__main__":
    # speakText("Let me ", 1)
    speakText("Welcome to Find The Treasure", 1)
    speakText("Your aim is to use the objects in the room to find the treasure", 1)
    speakText("Welcome to Find The Treasure. Your aim is to use the objects in the room to find the treasure", 3)
    speakText("who wants the key")
