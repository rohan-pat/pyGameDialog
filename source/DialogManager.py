from FrameSlot import FrameSlot

class DialogManager:
    def __init__(self, buff, buff2):
        self.keyState=0
        self.hammerState=0
        self.wallState=0
        self.swordState=0
        self.treasureState=0
        self.dragonState=0
        self.greetingState=0
        self.goodbyeState=0
        self.answerState=0
        self.movementState = 0
        self.lightState = 0
        self.value=" "
        self.fs = FrameSlot()
        self.buff = buff
        self.buff2 = buff2
        #entity="key"

    def manager(self, intent, entity):
        print("intent, entity is", intent, entity)
        if(intent == "greeting"):
            return self.greeting(entity)
        elif(intent == "possession"):
            return self.possession(entity)
        elif(intent=="break"):
            return self.breaks(entity)
        elif(intent=="cry"):
            return self.kill(entity)
        elif(intent=="unlock"):
            return self.unlock(entity)
        elif(intent=="use"):
            return self.use(entity)
        elif(intent=="release"):
            return self.release(entity)
        elif(intent=="movement"):
            return self.movement()
        elif(intent=="undefined"):
            return self.undefined()
        elif(intent == "light"):
            return self.lights()
        elif(intent=="goodbye"):
            return self.goodbye()
        # elif(intent=="What"):
        #     self.what()
        elif(intent == "answer"):
            return self.answer(entity)

    def greeting(self, entity):
        print("in greeting functon")
        if(self.greetingState == 0):
            if entity == "0":
                self.action = "greeting"
                return self.fs.frameSlot(self.action, entity)
            elif entity == "1":
                self.action = "tutorial1"
                return self.fs.frameSlot(self.action, entity)
            elif entity == "2":
                self.action = "tutorial2"
                self.greetingState = 1
                return self.fs.frameSlot(self.action, entity)
        elif(self.greetingState == 1):
            self.action = "greetingAgain"
            return self.fs.frameSlot(self.action,entity)

    def possession(self,entity) :
        print("entity is", entity)
        if(entity == "key"):
            return self.key()
        elif(entity == "hammer"):
            print("hammer entity selected")
            return self.hammer()
        elif(entity == "weapon"):
            return self.weapon()
        elif(entity == "armor"):
            return self.armor()
        else:
            return self.pundefined()

    def breaks(self,entity):
        if(entity=="wall" or entity == "hammer"):
            return self.wall()
        else:
            return self.bundefined()

    def kill(self,entity):
        if(entity=="dragon"):
            return self.dragon()
        else:
            return self.ukill()

    def unlock(self,entity):
        if(entity=="treasure"):
            return self.treasure()
        else:
            return self.uundefined()

    def release(self,entity):
        if(entity=="key"):
            return self.rkey()
        elif(entity=="hammer"):
            return self.rhammer()
        elif(entity=="weapon"):
            return self.rweapon()
        else:
            return self.rundefined()

    def use(self,entity):
        if(entity=="key"):
            return self.ukey()
        elif(entity=="hammer"):
            return self.uhammer()
        elif(entity=="weapon"):
            return self.uweapon()
        else:
            return self.usundefined()

    def answer(self,entity):
        if(entity=="Yes"):
            if self.answerState == 1:
                self.answerState = 0
                self.swordState = 1
                self.action = "correctAnswer"
                self.buff.put(42)
                return self.fs.frameSlot(self.action,entity)
            else:
                return self.usundefined()
    #
    # def What(self):
    #     if(self.hammerState==1):
    #         if(self.wallState==1):
    #             self.wlight()
    #
    def movement(self):
        if self.movementState == 0:
            entity = "empty"
            self.action="illegalMove"
            self.buff2.put(1)
            self.movementState = 1
            return self.fs.frameSlot(self.action,entity)
        else:
            entity = "empty"
            self.action="illegalMove2"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def armor(self):
        return self.weapon()

    def undefined(self):
        entity = "empty"
        if(self.answerState == 1):
            self.action="wrongAnswer"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)
        else:
            self.action="errorIntent"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def goodbye(self):
            entity = "empty"
            self.action = "goodBye"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def key(self):
        entity = "key"
        if(self.keyState==0):
            if self.dragonState == 0:
                self.action = "dragonNotDead"
                self.buff2.put(1)
                return self.fs.frameSlot(self.action,entity)
            elif self.dragonState == 1:
                self.keyState=1
                self.action="PickUp"
                self.buff.put(61)
                return self.fs.frameSlot(self.action,entity)
        elif(self.keyState == 1):
            self.action="pickedUpAlready"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def hammer(self):
        entity = "hammer"
        print("hammer function")
        if(self.hammerState == 0):
            self.hammerState = 1
            self.action = "pickUpHammer"
            print("adding 1 to buffer")
            self.buff.put(1)
            return self.fs.frameSlot(self.action,entity)
        elif(self.hammerState==1):
            self.action="pickedUpAlready"
            self.buff.put(1)
            return self.fs.frameSlot(self.action,entity)

    def weapon(self):
        entity = "sword"
        if(self.swordState==0):
            if self.lightState == 0:
                self.action="PickUpDarkSword"
                self.buff2.put(1)
                return self.fs.frameSlot(self.action,entity)
            elif self.lightState == 1:
                # self.swordState=1
                self.answerState=1
                self.action="PickUpSword"
                self.buff.put(41)
            return self.fs.frameSlot(self.action,entity)
        elif(self.swordState==1):
            self.action="pickedUpAlready"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def pundefined(self):
        return self.usundefined()

    def wall(self):
        entity = "hammer"
        if(self.hammerState==1 and self.wallState==0):
            self.wallState=1
            self.action="wallBroke"
            self.buff.put(2)
            return self.fs.frameSlot(self.action,entity)
        elif(self.hammerState==1 and self.wallState==1):
            self.action="wallAlreadyBroke"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)
        else:
            self.action="donotPossess"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def bundefined(self):
        return self.usundefined()

    def dragon(self):
        entity = "sword"
        if(self.swordState==1 and self. dragonState==0):
            self.dragonState=1
            self.action="dragonKilled"
            self.buff.put(5)
            return self.fs.frameSlot(self.action,entity)
        elif(self.swordState==1 and self. dragonState==0):
            self.action="dragonAlreadyKilled"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)
        else:
            self.action = "noKillDragon"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)
    #
    # def armorSuit(self):
    #     entity="sword"
    #     if(self.swordState==0):
    #         self.swordState=1
    #         self.answerState=1
    #         self.action="PickUpSword"
    #         return self.fs.frameSlot(self.action,entity)
    #
    def ukill(self):
        return self.usundefined()

    def treasure(self):
        entity = "key"
        if(self.keyState==1):
            self.action="treasureUnlocked"
            self.buff.put(7)
            return self.fs.frameSlot(self.action,entity)
        else:
            if self.dragonState == 0:
                self.action = "donotPossessKey"
                self.buff2.put(1)
                return self.fs.frameSlot(self.action,entity)
            elif self.dragonState == 1:
                self.action = "dragonNoKey"
                self.buff2.put(1)
                return self.fs.frameSlot(self.action,entity)

    def uundefined(self):
        return self.usundefined()

    def rkey(self):
        entity="key"
        if(self.keyState==1):
            self.action="releaseEntity"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)
        elif(self.keyState==0):
            self.action="donotPossess"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def rhammer(self):
        entity="hammer"
        if(self.hammerState==1):
            self.action="releaseEntity"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)
        elif(self.hammerState==0):
            self.action="donotPossess"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def rweapon(self):
        entity="sword"
        if(self.swordState==1):
            self.action="releaseEntity"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)
        elif(self.swordState==0):
            self.action="donotPossess"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    def rundefined(self):
        return self.usundefined()

    def ukey(self):
        return self.treasure()

    def uhammer(self):
        return self.wall()

    def uweapon(self):
        return self.dragon()

    def usundefined(self):
        entity = "empty"
        self.action="entityUndefined"
        self.buff2.put(1)
        return self.fs.frameSlot(self.action,entity)

    def lights(self):
        entity = "lights"
        if self.lightState == 0:
            if self.wallState == 1:
                self.action="lightsOn"
                self.buff.put(3)
                self.lightState = 1
                return self.fs.frameSlot(self.action,entity)
            elif self.wallState == 0:
                self.action="lightsOnWall"
                self.buff2.put(1)
                return self.fs.frameSlot(self.action,entity)
        elif self.lightState == 1:
            self.action = "lightsAlreadyOn"
            self.buff2.put(1)
            return self.fs.frameSlot(self.action,entity)

    # def wlight(Self):
    #     self.action="lightHint"
    #     return self.fs.frameSlot(self.action,entity)
