class FrameSlot:
    def __init__(self):
        self.msg=" "
    def frameSlot(self,action,entity):
        if(action=="greeting"):
            self.msg="Hi, You are a brave knight on a mission to find the treasure located within this castle. Your objective is to obtain the treasure"
            "by interacting with various objects within the game.To understand this better,lets walk through a tutorial"."You need not tell the character to move around it will find its way towards the object"
            "Now You outside a castle and there is a hammer near you .Lets pick up the hammer"
        elif(action=="PickUp"):
            value=randint(0,2)
            if(value==0):
                self.msg="you picked up the "+" "+entity
            elif(value==1):
                self.msg="The"+" "+entity+ "has been picked up"
            elif(value==2):
                self.msg="you took the"+" "+entity
        self.texttospeech(self.msg)
        elif(action=="pickUpHammer"):
            self.msg="Good Now that you have the hammer lets break the wall"
            self.texttospeech(self.msg)
        elif(action=="entityUndefined"):
            self.msg="I am sorry  the object you specified could not be found in the castle Please try again"
        elif(action=="noKillDragon"):
            self.msg="you do not want to go near the dragon unarmed"
            self.texttospeech(self.msg)
        elif(action=="donotPossessKey"):
            self.msg="The key to the chest is guarded by the dragon"
            self.texttospeech(self.msg)
        elif(action=="PickUpSword"):
            self.msg="Who dares to enter my castleYou think you deserve this sword? If you're really worthy of it,you'll be able to answer my riddle first.
            "How many components does a Dialog system have?"
            self.texttospeech(self.msg)
        elif(action=="correctAnswer"):
            self.msg="You are here is your sword go kill the dragon"
            self.texttospeech(self.msg)
        elif(action="wrongAnswer"):
            self.msg="You answer is wrong try again "
