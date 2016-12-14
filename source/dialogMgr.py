from SpeechRec import init_asr, startSpeechRec
from languageClassifier import langClassifier
from SpeechSynthesizer import speakText
from DialogManager import DialogManager
import threading
import multiprocessing as mp
import sys
import time

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

def startDialogManager(buff, text_buff, buff2):
    # initializing the asr.
    init_asr()
    # initializing the language classifier.
    l = langClassifier()
    d = DialogManager(buff, buff2)

    count = 0
    synthesizer_control = False
    asr_control = False
    dialog_control = True
    first_run = True
    spoken_text = ""
    action = ""
    intent = ""
    entity = ""
    confidence = ""

    while True:
        # blocking till character movements complete.
        temp = buff2.get()
        print("After returning from get")
        print("Synth control", synthesizer_control)

        if synthesizer_control:
            print("synthesizer text is",spoken_text, action)
            synthesizer_control = False
            if action in ["PickUpSword", "correctAnswer", "wrongAnswer"]:
                speakText(spoken_text, 2)
            else:
                speakText(spoken_text, 1)

            if action == "goodBye":
                break

        if asr_control:
            asr_control = False
            print("Start of recording")
            text = " "
            buff.put(81)
            result = None
            speechRecognize = True

            while speechRecognize:
                result = startSpeechRec()
                try:
                    if result:
                        print("In ASR True")
                        speechRecognize = False
                    i = 0
                    for res in result:
                        if i == 0:
                            text = res.transcript
                        print(i,". text is", res.transcript, end=",")
                        print("confidence is", res.confidence)
                        i = i + 1
                except Exception:
                    print("Error Occurred")

            text_buff.put(text)
            buff.put(82)

            # getting the intents from watson.
            intent, entity, confidence = l.getIntent(text)

        if dialog_control:
            if first_run:
                if count == 0:
                    spoken_text, action = d.manager("greeting", "0")
                    synthesizer_control = True
                    asr_control = False
                    buff2.put(1)
                    first_run = True
                    count = 1
                elif count == 1:
                    spoken_text, action = d.manager("greeting", "1")
                    synthesizer_control = True
                    asr_control = False
                    buff2.put(1)
                    first_run = True
                    count = 2
                elif count == 2:
                    spoken_text, action = d.manager("greeting", "2")
                    synthesizer_control = True
                    buff2.put(1)
                    first_run = False
                    count = 0
                    asr_control = True
            else:
                print("The value of intent, value, confidence is ", intent, entity, confidence)
                asr_control = True
                synthesizer_control = True
                print("")
                spoken_text, action = d.manager(intent, entity)
                print("text is", spoken_text, action)

    print("end of program")
    buff.put(9)

if __name__ == "__main__":
        buff = mp.Queue()
        dialogThread = threading.Thread(target=startDialogManager,args=(buff,))
        dialogThread.start()
        dialogThread.join()
        print("End")
