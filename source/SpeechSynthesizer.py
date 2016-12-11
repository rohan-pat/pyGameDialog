import subprocess

def speakText(text, selection=1):
    if selection == 1:
        cmdText = "say --voice=samantha " + text
        x = subprocess.check_call(cmdText, shell=True)
    elif selection == 2:
        cmdText = "say --voice=daniel " + text
        x = subprocess.check_call(cmdText, shell=True)
    else:
        cmdText = "say --voice=samantha " + text
        x = subprocess.check_call(cmdText, shell=True)

if __name__ == "__main__":
    # speakText("Let me ", 1)
    speakText("Welcome to Find The Treasure", 1)
    speakText("Your aim is to use the objects in the room to find the treasure", 1)
    speakText("Welcome to Find The Treasure, Your aim is to use the objects in the room to find the treasure", 2)
    speakText("who wants the key")
