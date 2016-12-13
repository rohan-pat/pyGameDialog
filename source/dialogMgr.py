from SpeechRec import init_asr, startSpeechRec
from languageClassifier import langClassifier
import threading
import multiprocessing as mp

# start of dialog manager function.
initial = True

def startDialogManager(buff):
    if initial:
        initial = False
        init_asr()

    count = 0

    while True:
        print("Start of recording")
        result = startSpeechRec()
        print(result.transcript)

        count += 1
        if count > 5:
            break

    print("end of program")

if __name__ = "__main__":
        buff = mp.Queue()
        dialogThread = threading.Thread(target=startDialogManager,args=(buff,))
        dialogThread.start()
        dialogThread.join()
        print("End")
