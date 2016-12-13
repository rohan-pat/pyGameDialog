class DialogManager:
    def __init__(self):
        self.fs=FrameSlot()
        self.keyState=0
        self.hammerSate=0
        self.wallState=0
        self.swordState=0
        self.treasureState=0
        self.dragonState=0
        self.greetingSate=0
        self.goodbyeState=0
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
            self.unlock(self.entity)
        elif(intent=="release"):
            self.release(self.entity)
        elif(intent=="movement"):
            self.movement()
        elif(intent=="undefined"):
            self.undefined()
        elif(intent=="light"):
            self.light(self.entity)
        elif(intent=="goodbye"):
            self.goodbye(self.entity)
        elif(intent=="greeting"):
            self.greeting(self.entity)

    def  possession(self,entity) :
        if(entity=="key"):
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
    def kill(self,enitiy):
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
        entity="key"
        if(self.keyState==0):
            self.keyState=1
            fs.fsPossession(entity)
        elif(self.keyState==1):
            fs.fsAgainPossesion(entity)
    def hammer(self):
        entity="hammer"
        if(self.hammerSate==0):
            self.hammerSate=1
            fs.fsPossession(entity)
        elif(self.hammerSate==1):
            fs.fsAgainPossesion(entity)
    def weapon(self):
        enitiy="sword"
        if(self.swordState==0):
            self.swordState=1
            fs.fsPossession(entity)
        elif(self.swordState==1):
            fs.fsAgainPossesion(entity)
    def pundefined(self):
        fs.entityUndefined()

    def wall(self):
        enitiy="hammer"
        if(self.hammerSate==1 and self.wallState==0):
            self.wallState=1
            fs.breakWall()
        elif(self.hammerSate==1 and self.wallState==1):
            fs.wallBroken()
        else:
            fs.donotPossess(entity)
    def bundefined(self):
        fs.entityUndefined()
    def dragon(self):
        entity="sword"
        if(self.swordState==1 and self. dragonState==0):
            self.dragonState=1
            fs.dragonKill()
        elif(self.swordState==1 and self. dragonState==0):
            fs.dragonAlreadyKilled()
        else:

            fs.donotPossess(entity)

    def ukill(self):
        fs.entityUndefined()
    def treasure(self):
        entity="key"
        if(self.keyState==1):
            fs.unlockTreasure()
        else:
            fs.donotPossess(entity)
    def uundefined(self):
        fs.entityUndefined()
    def rkey(self):
        entity="key"
        if(self.keyState==1):
            fs.dropEntity(entity)
        elif(keyState==0):
            fs.donotPossess(entity)
    def rhammer(self):
        entiy="hammer"
        if(self.hammerState==1):
            fs.dropEntity(entity)
        elif(self.hammerState==0):
            fs.donotPossess(entity)
    def rweapon(self):
        entity="sword"
        if(self.swordState==1):
            fs.dropEntity(entity)
        elif(self.swordState==0):
            fs.donotPossess(entity)
    def rundefined(self):
        fs.entityUndefined()
    def ukey(self):
        entity="key"
        if(self.keyState==1):
            fs.unlockTreasure()
        elif(self.keyState==0):
            fs.donotPossess(entity)
    def uhammer(self):
        entity="hammer"
        if(self.hammerState==1 and self.wallState==0):
            self.wallState=1
            fs.breakWall()
        elif(self.hammerSate==1 and self.wallState==1):
            fs.wallBroken()
        else:
            fs.donotPossess(entity)

    def uweapon(self):
        entity="sword"
        if(self.swordState==1 and self. dragonState==0):
            self.dragonState=1
            fs.dragonKill()
        elif(self.swordState==1 and self. dragonState==0):
            fs.dragonAlreadyKilled()
        else:

            fs.donotPossess(entity)
    def usundefined(self):
        fs.entityUndefined()
    def move(self):
        fs.illegalMove()
    def lights():
        fs.lightUp()
    def unundefined(self):
        fs.errorUndefined()
    def greetings(self):
        if(self.greetingSate==0):
            self.greetingSate=1
            fs.GreetingsInital()
        elif(self.greetingSate==1):
            fs.helloAgain()
    def goodbyes(self):
        fs.byeBye()
