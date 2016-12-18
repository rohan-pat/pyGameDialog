from random import randint

class FrameSlot:
    def __init__(self):
        self.msg = ""

    def frameSlot(self,action,entity):
        print("action is", action)
        if(action == "greeting"):
            self.msg = "Hi, You are a brave knight on a mission. Your objective is to find the treasure by interacting with objects in the game."

        if(action == "tutorial1"):
            self.msg = "To understand this better, lets walk through a tutorial. Remember, you need not tell the character to move around."

        if(action == "tutorial2"):
            self.msg = "He can find his way around. You are outside a castle and there is a hammer near you. Say get the hammer to pick up the hammer."

        elif(action == "PickUp"):
            value = randint(0,2)
            if(value == 0):
                self.msg = "you picked up the "+" "+entity
            elif(value == 1):
                self.msg = "The"+" "+entity+ "has been picked up"
            elif(value == 2):
                self.msg = "you took the"+" "+entity

        elif(action == "pickUpHammer"):
            self.msg="Good, now that you have the hammer, lets break the wall. What would you like to do?"

        elif(action == "pickedUpAlready"):
            self.msg = "You already have it. What to do next?"

        elif(action == "wallBroke"):
            self.msg = "Alright, that was good. Hope you got the hang of it.You should explore the castle but it seems to be pretty dark inside. What to do next?"

        elif(action == "donotPossess"):
            self.msg = "you do not have " + entity

        elif(action == "wallAlreadyBroke"):
            self.msg = "The wall is already broken"

        elif(action == "lightsOn"):
            self.msg="You have switched on the lights. The treasure is in the room, but unfortunately the key to unlock the treasure is guarded by the dragon. What would you like to do next?"

        elif(action == "lightsAlreadyOn"):
            self.msg = "The lights are already on"

        elif(action == "lightsOnWall"):
            self.msg = "You cannot enter the castle until you break the wall."

        elif(action=="entityUndefined"):
            self.msg="I am sorry the object you specified could not be found in the castle. Please try again"

        elif(action=="noKillDragon"):
            self.msg="you do not want to go near the dragon unarmed."

        elif(action=="donotPossessKey"):
            self.msg="The key to the chest is guarded by the dragon"

        elif(action == "dragonNoKey"):
            self.msg = "You do not have the key"

        elif(action=="PickUpSword"):
            self.msg = "Who dares to enter my castle. You think you deserve this sword? If you are really worthy of it, you should be able to answer my question. The dialog system has 5 components. Yes or No?"

        elif(action == "PickUpDarkSword"):
            self.msg = "The room is dark. You cannot see anything."

        elif(action=="correctAnswer"):
            self.msg="You are correct. Here is your sword, go kill the dragon and claim your treasure. What do you want to do next?"

        elif(action == "wrongAnswer"):
            self.msg="You answer is wrong. Try again"

        elif(action == "dragonKilled"):
            self.msg="Victory is yours. The dragon left the key behind."

        elif(action == "dragonAlreadyKilled"):
            self.msg="You have already scared the dragon away"

        elif(action == "noKillDragon"):
            self.msg="you do not want to go near the dragon unarmed. What to do next?"

        elif(action == "dragonNotDead"):
            self.msg = "The dragon is guarding the key. you do not want to go near the dragon unarmed. What to do next?"

        elif(action == "treasureUnlocked"):
            self.msg="Well done, You have unlocked the treasure and you have succeeded in your quest. Thank you for playing the game"

        elif(action == "errorIntent"):
            self.msg="I could not get that. Could you say that again?";

        elif(action=="illegalMove"):
            self.msg = "You dont need to tell the character to move around. He can do that by himself."

        elif(action=="illegalMove2"):
            self.msg = "You dont need to tell the character to move around. You can directly say something like Get the Hammer"

        elif(action=="releaseEntity"):
            self.msg = "You cannot drop it"

        elif(action == "goodBye"):
            self.msg="Goodbye."

        return self.msg, action
