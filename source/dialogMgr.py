from SpeechRec import init_asr, startSpeechRec
from languageClassifier import langClassifier
import threading
import multiprocessing as mp

# start of dialog manager function.

def lev_dist(source, target):
    if source == target:
        return 0

    # Prepare a matrix
    slen, tlen = len(source), len(target)
    dist = [[0 for i in range(tlen+1)] for x in range(slen+1)]
    for i in range(slen+1):
        dist[i][0] = i
    for j in range(tlen+1):
        dist[0][j] = j

    # Counting distance, here is my function
    for i in range(slen):
        for j in range(tlen):
            cost = 0 if source[i] == target[j] else 1
            dist[i+1][j+1] = min(
                            dist[i][j+1] + 1,   # deletion
                            dist[i+1][j] + 1,   # insertion
                            dist[i][j] + cost   # substitution
                        )
    return dist[-1][-1]

def startDialogManager(buff):
    # initializing the asr.
    init_asr()
    # initializing the language classifier.
    l = langClassifier()

    count = 0

    while True:
        print("Start of recording")
        text = None
        result = startSpeechRec()
        i = 0
        for res in result:
            if i == 0:
                text = res.transcript
            print(i,". text is", res.transcript, end=",")
            print("confidence is", res.confidence)
            i = i + 1

        # getting the intents from watson.
        intent, value, confidence = l.getIntent(text)
        print("The value of intent, value, confidence is ", intent, value, confidence)

        count += 1
        if count > 5:
            break

    print("end of program")

if __name__ == "__main__":
        buff = mp.Queue()
        dialogThread = threading.Thread(target=startDialogManager,args=(buff,))
        dialogThread.start()
        dialogThread.join()
        print("End")
