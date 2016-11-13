class Fas(object):
    def texttospeech(msg):
        #print(msg)
        tts = gTTS(text=msg, lang='en')
        #print(text)
        tts.save("rec.mp3")
        mixer.init()
        mixer.music.load("rec.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pygame.time.Clock().tick(2)


    def Greeting(action):
        if(action=="gf"):
            msg="Hi,"
            Fas.texttospeech(msg)
        elif(action=="ga"):
            msg="well Hello again"
            Fas.texttospeech(msg)
    def Possesion(action):
        if(action=="pk"):
            msg="You picked up the key"
            Fas.texttospeech(msg)
        elif(action=="pka"):
            msg="You already have the key with you "
            Fas.texttospeech(msg)
        elif(action=="ph"):
            msg="You picked up the hammer"
            Fas.texttospeech(msg)
        elif(action=="pha"):
            msg="You already have the hammer with you"
            Fas.texttospeech(msg)
        elif(action=="pui"):
            msg="The item could not be located"
            Fas.texttospeech(msg)
    def Release(action):
         if(action=="rk"):
             msg="You dropped the key"
             Fas.texttospeech(msg)
         elif(action=="rka"):
             msg="You do not have the key "
             Fas.texttospeech(msg)
         elif(action=="rh"):
             msg="You dropped the hammer"
             Fas.texttospeech(msg)
         elif(action=="rha"):
             msg="You do not have the hammer with you"
             Fas.texttospeech(msg)
         elif(action=="rui"):
             msg="You do not possess the item which you want to drop"
             Fas.texttospeech(msg)

    def Unlock(action):
        if(action=="ud"):
            msg="You opened the door"
            Fas.texttospeech(msg)
        elif(action=="udnk"):
            msg="You do not have the key to open the door"
            Fas.texttospeech(msg)
        elif(action=="dao"):
            msg="The door is already open"
            Fas.texttospeech(msg)
        elif(action=="dui"):
            msg="The item which you want cannot be found"
            Fas.texttospeech(msg)

    def Break(action):
        if(action=="bd"):
            msg="You opened the door"
            Fas.texttospeech(msg)
        elif(action=="bdnk"):
            msg="You do not have the hammer to break the door"
            Fas.texttospeech(msg)
        elif(action=="dab"):
            msg="The door is already open"
            Fas.texttospeech(msg)
        elif(action=="dui"):
            msg="The item which you want cannot be found"
            Fas.texttospeech(msg)

    def undefined(action):
        if(action=="ud"):
            msg="You cannot do that"
            Fas.texttospeech(msg)
    def Goodbye(action):
        if(action=="gb"):
            msg="Good bye"
            Fas.texttospeech(msg)
class Dialogobject(object):

    def Dialogmanger():
        intent,entity=watson.watsonspeech()
        print(intent)
        #print(intent)
        key=1
        door=0
        hammer=0
        greetingvar=0
        if(intent=="possession"):
            if(entity=="key"):
                if(key==0):
                    key=1
                    action="pk"
                    Fas.Possesion(action)
                elif(key==1):
                    action="pka"
                    Fas.Possesion(action)
            elif(entity=="hammer"):
                if(hammer==0):
                    hammer=1
                    action="ph"
                    Fas.Possesion(action)
                elif(hammer==1):
                    action="pha"
                    Fas.Possesion(action)
            elif(entity=="empty"):
                action="pui"
                Fas.Possesion(action)

        elif(intent=="release"):
            if(entity=="key"):
                if(key==1):
                    key=0
                    action="rk"
                    Fas.Release(action)
                elif(key==0):
                    action="rka"
                    Fas.Release(action)
            elif(entity=="hammer"):
                if(hammer==1):
                    hammer=0
                    action="rh"
                    Fas.Release(action)
                elif(hammer==0):
                    action="rha"
                    Fas.Release(action)
            elif(entity=="empty"):
                action="rui"
                Fas.Release(action)
            else:
                action="rui"
                Fas.Release(action)

        elif(intent=="unlock"):
            if(entity=="door"):
                if(door==0):
                    if(key==1):
                        door=1
                        action="ud"
                        Fas.Unlock(action)
                    elif(key==0):
                        action="udnk"
                        Fas.Unlock(action)
                elif(door==1):
                    action="dao"
                    Fas.Unlock(action)
            elif(enitiy=="empty"):
                action="dui"
                Fas.Unlock(action)

        elif(intent=="break"):
            if(entity=="door"):
                if(door==0):
                    if(hammer==1):
                        door=1
                        action="bd"
                        Fas.Break(action)
                    elif(hammer==0):
                        action="bdnk"
                        Fas.Break(action)
                elif(door==1):
                    action="dab"
                    Fas.Break(action)
            elif(entity=="empty"):
                action="dui"
                Fas.Break(action)
        elif(intent=="undefined"):
            action="ud"
            Fas.undefined(action)
        elif(intent=="greeting"):
            if(greetingvar==0):
                greetingvar=1
                action="gf"
                Fas.Greeting(action)
            elif(greetingvar==1):
                action="ga"
                Fas.Greeting(action)
        elif(intent=="goodbye"):
            action="gb"
            Fas.Goodbye(action)
