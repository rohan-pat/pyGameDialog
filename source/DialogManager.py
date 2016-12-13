class DialogManager:
    def __init__(self):
        # self.fs=FrameSlot()
        # self.w=watson()
        # self.intent,self.entity=self.w.watsonspeech()
        # print(self.intent)
        # print(self.entity)
        self.keyState=0
        self.hammerState=1
        self.wallState=0
        self.swordState=1
        self.treasureState=0
        self.dragonState=0
        self.greetingSate=0
        self.goodbyeState=0
        self.value=" "
        #self.entity="key"

    def manager(self,intent):
        if(intent=="possession"):
            self.possession(self.entity)
        elif(intent=="break"):
            self.breaks(self.entity)
        elif(intent=="cry"):
            self.kill(self.entity)
        elif(intent=="unlock"):
            self.unlock(self.entity)
        elif(intent=="use"):
            self.use(self.entity)
        elif(intent=="release"):
            self.release(self.entity)
        elif(intent=="movement"):
            self.movement()
        elif(intent=="undefined"):
            self.undefined()
        elif(intent=="light"):
            self.light()
        elif(intent=="goodbye"):
            self.goodbye()
        elif(intent=="greeting"):
            self.greeting()

    def possession(self,entity) :
        if(entity=="key"):
            print(entity)
            self.key()
        elif(entity=="hammer"):
            self.hammer()
        elif(entity=="weapon"):
            self.weapon()
        else:
            self.pundefined()

    def breaks(self,enitiy):
        if(entity=="wall"):
            self.wall()
        else:
            self.bundefined()

    def kill(self,entity):
        if(entity=="dragon"):
            self.dragon()
        else:
            self.ukill()

    def unlock(self,entity):
        if(entity=="treasure"):
            self.treasure()
        else:
            self.uundefined()

    def release(self,entity):
        if(entity=="key"):
            self.rkey()
        elif(entity=="hammer"):
            self.rhammer()
        elif(entity=="weapon"):
            self.rweapon()
        else:
            self.rundefined()

    def use(self,entity):
        if(entity=="key"):
            self.ukey()
        elif(entity=="hammer"):
            self.uhammer()
        elif(entity=="weapon"):
            self.uweapon()
        else:
            self.usundefined()

    def movement(self):
        self.move()

    def light(self):
        self.lights()

    def undefined(self):
        self.unundefined()

    def greeting(self):
        self.greetings()

    def goodbye(self):
        self.goodbyes()

    def key(self):
        entity = "key"
        if(self.keyState==0):
            self.keyState=1
            self.action="PickUp"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.keyState==1):
            self.value="pickedUpAlready"
            self.fs.frameSlot(self.action,self.entity)

    def hammer(self):
        entity = "hammer"
        if(self.hammerState==0):
            self.hammerState=1
            self.action="PickUp"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.hammerState==1):
            self.value="pickedUpAlready"
            self.fs.frameSlot(self.action,self.entity)

    def weapon(self):
        enitiy = "sword"
        if(self.swordState==0):
            self.swordState=1
            self.action="PickUp"
            self.fs.frameSlot(self.action,entity)
        elif(self.swordState==1):
            self.value="pickedUpAlready"
            self.fs.frameSlot(self.action,entity)

    def pundefined(self):
        self.action = "entityUndefined"
        self.fs.frameSlot(self.action,self.entity)

    def wall(self):
        enitiy = "hammer"
        if(self.hammerState==1 and self.wallState==0):
            self.wallState=1
            self.action="wallBroke"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.hammerState==1 and self.wallState==1):
            self.action="wallAlreadyBroke"
            self.fs.frameSlot(self.action,self.entity)
        else:
            self.action="donotPossess"
            self.fs.frameSlot(self.action,self.entity)

    def bundefined(self):
        self.action = "entityUndefined"
        self.fs.frameSlot(self.action,self.entity)

    def dragon(self):
        entity = "sword"
        if(self.swordState==1 and self. dragonState==0):
            self.dragonState=1
            self.action="dragonKilled"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.swordState==1 and self. dragonState==0):
            self.action="dragonAlreadyKilled"
            self.fs.frameSlot(self.action,entity)
        else:
            self.action = "donotPossess"
            self.fs.frameSlot(self.action,entity)

    def ukill(self):
        self.action = "entityUndefined"
        self.fs.frameSlot(self.action,self.entity)

    def treasure(self):
        entity = "key"
        if(self.keyState==1):
            self.action="treasueUnlocked"
            self.fs.frameSlot(self.action,self.entity)
        else:
            self.action="donotPossess"
            self.fs.frameSlot(self.action,entity)

    def uundefined(self):
        self.action="entityUndefined"
        self.fs.frameSlot(self.action,self.entity)

    def rkey(self):
        entity="key"
        if(self.keyState==1):
            self.keyState=0
            self.action="releaseEntity"
            self.fs.frameSlot(self.action,self.entity)
        elif(keyState==0):
            self.action="donotPossess"
            self.fs.frameSlot(self.action,entity)

    def rhammer(self):
        entiy="hammer"
        if(self.hammerState==1):
            self.hammerState=0
            self.action="releaseEntity"
            self.fs.frameSlot(self.action,self.entity)
            self.fs.dropEntity(entity)
        elif(self.hammerState==0):
            self.action="donotPossess"
            self.fs.frameSlot(self.action,entity)

    def rweapon(self):
        entity="sword"
        if(self.swordState==1):
            self.swordState=0
            self.action="releaseEntity"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.swordState==0):
            self.action="donotPossess"
            self.fs.frameSlot(self.action,entity)

    def rundefined(self):
        self.action="entityUndefined"
        self.fs.frameSlot(self.action,self.entity)

    def ukey(self):
        entity="key"
        if(self.keyState==1):
            self.action="treasueUnlocked"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.keyState==0):
            self.action="donotPossess"
            self.fs.frameSlot(self.action,entity)

    def uhammer(self):
        entity="hammer"
        if(self.hammerState==1 and self.wallState==0):
            self.wallState=1
            self.action="wallBroke"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.hammerState==1 and self.wallState==1):
            self.action="wallAlreadyBroke"
            self.fs.frameSlot(self.action,self.entity)
        else:
            self.action="donotPossess"
            self.fs.frameSlot(self.action,self.entity)

    def uweapon(self):
        entity="sword"
        if(self.swordState==1 and self. dragonState==0):
            self.dragonState=1
            self.action="dragonKilled"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.swordState==1 and self. dragonState==0):
            self.action="dragonAlreadyKilled"
            self.fs.frameSlot(self.action,entity)
        else:
            self.action="donotPossess"
            self.fs.frameSlot(self.action,entity)

    def usundefined(self):
        self.action="entityUndefined"
        self.fs.frameSlot(self.action,self.entity)

    def move(self):
        self.action="illegalMove"
        self.fs.frameSlot(self.action,self.entity)

    def lights(self):
        self.action="lightsOn"
        self.fs.frameSlot(self.action,self.entity)

    def unundefined(self):
        self.action="errorIntent"
        self.fs.frameSlot(self.action,self.entity)

    def greetings(self):
        if(self.greetingSate==0):
            self.greetingSate=1
            self.action="greetings"
            self.fs.frameSlot(self.action,self.entity)
        elif(self.greetingSate==1):
            elf.action="greetingsAgain"
            self.fs.frameSlot(self.action,self.entity)

    def goodbyes(self):
        self.action="goodBye"
        self.fs.frameSlot(self.action,self.entity)
