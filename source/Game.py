import pygame
from pygame.locals import *
from os.path import abspath, expanduser
import threading
import multiprocessing as mp
import time
from dialogMgr import startDialogManager
import nltk

class GameInstance:
    def __init__(self):
        pygame.init()

        #initialize the font.
        self.myfont = pygame.font.SysFont("Helvetica", 30)

        # setting clock for the game.
        self.clock = pygame.time.Clock()
        self.gameLoop = False

        # display window properties.
        self.display_width = 1265
        self.display_height = 550
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Find The Treasure")

        # colors for the same.
        self.black = (0,0,0)
        self.white = (255,255,255)

        # game images.
        filepath = abspath(expanduser("~/") + "/Documents/Studies/NLP/Project/pyGameDialog/images/")

        # background image.
        self.background = pygame.image.load(filepath+"/backWithDialog.png")
        self.background = pygame.transform.scale(self.background, (self.display_width, self.display_height))

        # avatar images.
        self.avatar = pygame.image.load(filepath+"/herodown.png")
        self.avatar = pygame.transform.scale(self.avatar, (40,40))
        self.avatar_down = pygame.image.load(filepath+"/herodown.png")
        self.avatar_down = pygame.transform.scale(self.avatar_down, (40,40))
        self.avatar_down1 = pygame.image.load(filepath+"/herodown1.png")
        self.avatar_down1 = pygame.transform.scale(self.avatar_down1, (40,40))
        self.avatar_down2 = pygame.image.load(filepath+"/herodown2.png")
        self.avatar_down2 = pygame.transform.scale(self.avatar_down2, (40,40))
        self.avatar_left = pygame.image.load(filepath+"/heroleft.png")
        self.avatar_left = pygame.transform.scale(self.avatar_left, (40,40))
        self.avatar_left1 = pygame.image.load(filepath+"/heroleft1.png")
        self.avatar_left1 = pygame.transform.scale(self.avatar_left1, (40,40))
        self.avatar_left2 = pygame.image.load(filepath+"/heroleft2.png")
        self.avatar_left2 = pygame.transform.scale(self.avatar_left2, (40,40))
        self.avatar_right = pygame.image.load(filepath+"/heroright.png")
        self.avatar_right = pygame.transform.scale(self.avatar_right, (40,40))
        self.avatar_right1 = pygame.image.load(filepath+"/heroright1.png")
        self.avatar_right1 = pygame.transform.scale(self.avatar_right1, (40,40))
        self.avatar_right2 = pygame.image.load(filepath+"/heroright2.png")
        self.avatar_right2 = pygame.transform.scale(self.avatar_right2, (40,40))
        self.avatar_up = pygame.image.load(filepath+"/heroup.png")
        self.avatar_up = pygame.transform.scale(self.avatar_up, (40,40))
        self.avatar_up1 = pygame.image.load(filepath+"/heroup1.png")
        self.avatar_up1 = pygame.transform.scale(self.avatar_up1, (40,40))
        self.avatar_up2 = pygame.image.load(filepath+"/heroup2.png")
        self.avatar_up2 = pygame.transform.scale(self.avatar_up2, (40,40))
        self.avatar_right_sword = pygame.image.load(filepath+"/herorightsword.png")
        self.avatar_right_sword = pygame.transform.scale(self.avatar_right_sword, (40,40))

        # initial ava
        self.avatar_pos_x = 320
        self.avatar_pos_y = 490
        self.x_movement = True
        self.y_movement = True
        self.player_move = False
        self.x_image = 0
        self.y_image = 0

        # dragon image.
        self.dragon = pygame.image.load(filepath+"/dragon.png")
        self.dragonc1 = pygame.image.load(filepath+"/dragonCry1.png")
        self.dragonc2 = pygame.image.load(filepath+"/dragonCry2.png")
        self.dragonc3 = pygame.image.load(filepath+"/dragonCry3.png")

        self.dragon_x = 580;
        self.dragon_y = 200;
        self.dragon_move = False

        # hammer object.
        self.hammer=pygame.image.load(filepath+"/hammer.png")
        self.hammer=pygame.transform.scale(self.hammer,(100,100))
        self.hammer_x = 465
        self.hammer_y = 485
        self.hammer_display = True

        # broken wall.
        self.brokenWall = pygame.image.load(filepath+"/scratchwall.png")
        self.brokenWall = pygame.transform.scale(self.brokenWall,(62,71))
        self.brokenWall_x = 432
        self.brokenWall_y = 427
        self.brokenWall_display = True

        # kapow image.
        self.kapow = pygame.image.load(filepath+"/kapow.png")
        self.kapow = pygame.transform.scale(self.kapow, (60,50))
        self.kapow1 = pygame.transform.scale(self.kapow, (120,100)) # 2.0
        self.kapow_x = 410
        self.kapow_y = 423
        self.kapow_display1 = False
        self.kapow_display2 = False

        # switch image.
        self.switchon = pygame.image.load(filepath+"/switchon.png")
        self.switchoff = pygame.image.load(filepath+"/switchoff.png")
        self.switch_x = 383
        self.switch_y = 395
        self.switch_display = 0
        self.darkroom = pygame.image.load(filepath+"/darkroom.png")
        self.darkroom = pygame.transform.scale(self.darkroom, (435,363)) # 418, 343
        self.darkroom_x = 243
        self.darkroom_y = 20
        self.darkroom_display = True

        # Knight Object.
        self.knight = pygame.image.load(filepath+"/armor1.png")
        self.knight = pygame.transform.scale(self.knight, (79,73))
        self.knight_x = 420
        self.knight_y = 40
        self.swordRock = pygame.image.load(filepath+"/swordRock.png")
        self.swordRock = pygame.transform.scale(self.swordRock, (79,73))
        self.swordNorock = pygame.image.load(filepath+"/rockwithoutsword.png")
        self.rock_x = 440
        self.rock_y = 90
        self.rock_display = 0

        # key object.
        self.key = pygame.image.load(filepath+"/key5.png")
        self.key_x = 600
        self.key_y = 230
        self.key_display = False

        # treasure object.
        self.ctreasure = pygame.image.load(filepath+"/closedTreasure.png")
        self.otreasure = pygame.image.load(filepath+"/openTreasure.png")
        self.treasure_x = 250
        self.treasure_y = 220
        self.treasure_display = 1

        # text positions.
        self.text_y1 = 0
        self.text_y2 = 0
        self.text_array = ""
        self.red1 = pygame.image.load(filepath+"/red1.png")
        self.red2 = pygame.image.load(filepath+"/red2.png")

        # custom user events for controlling the game.
        self.player_hammer_pick = pygame.USEREVENT + 1
        self.hammer_control = True
        #self.player_hammer_drop = pygame.USEREVENT + 2
        self.player_break_wall = pygame.USEREVENT + 2
        self.brokenWall_control = 0
        self.player_switch_on = pygame.USEREVENT + 3
        #self.player_switch_off = pygame.USEREVENT + 5
        self.switch_control = 0
        self.player_goto_knight = pygame.USEREVENT + 4
        self.goto_control = 0
        self.knight_event_control = 1
        # self.player_get_sword = pygame.USEREVENT + 5
        # self.get_sword_control = 0
        self.dragon_action = pygame.USEREVENT
        self.dragon_control = 0
        self.key_action = pygame.USEREVENT + 5
        self.key_event_control = 1
        self.treasure_action = pygame.USEREVENT + 6
        self.treasure_control = 0
        self.text_action = pygame.USEREVENT + 7
        self.text_event_control = 1

    # image related functions.
    def displayObject(self, image, x, y):
        """This method is used to load the image on the screen."""
        self.gameDisplay.blit(image, (x,y))

    def movePlayer(self, object, final_x, final_y, final_side):
        """Move object from one place to another."""
        if self.x_movement:
            # movement to positive x-direction.
            if (self.avatar_pos_x < (final_x-10)):
                self.avatar_pos_x = self.avatar_pos_x + 10
                if(self.x_image == 0):
                    #print("right")
                    self.avatar = self.avatar_right1
                    self.x_image = 1
                elif(self.x_image == 1):
                    #print("right1")
                    self.avatar = self.avatar_right
                    self.x_image = 2
                elif(self.x_image == 2):
                    #print("right2")
                    self.avatar = self.avatar_right2
                    self.x_image = 0
            # movement to negative x-direction.
            elif (self.avatar_pos_x > (final_x-10)):
                self.avatar_pos_x = self.avatar_pos_x - 10
                if(self.x_image == 0):
                    #print("left")
                    self.avatar = self.avatar_left1
                    self.x_image = 1
                elif(self.x_image == 1):
                    #print("left1")
                    self.avatar = self.avatar_left
                    self.x_image = 2
                elif(self.x_image == 2):
                    #print("left2")
                    self.avatar = self.avatar_left2
                    self.x_image = 0
            else:
                #print("x movement done")
                self.x_movement = False
        elif self.y_movement:
            if (self.avatar_pos_y < (final_y-10)):
                self.avatar_pos_y = self.avatar_pos_y + 10
                if(self.y_image == 0):
                    #print("down")
                    self.avatar = self.avatar_down1
                    self.y_image = 1
                elif(self.y_image == 1):
                    #print("down1")
                    self.avatar = self.avatar_down
                    self.y_image = 2
                elif(self.y_image == 2):
                    #print("down2")
                    self.avatar = self.avatar_down2
                    self.y_image = 0
            # movement to negative y-direction.
            elif (self.avatar_pos_y > (final_y-10)):
                self.avatar_pos_y = self.avatar_pos_y - 10
                if(self.y_image == 0):
                    #print("left")
                    self.avatar = self.avatar_up1
                    self.y_image = 1
                elif(self.y_image == 1):
                    #print("left1")
                    self.avatar = self.avatar_up
                    self.y_image = 2
                elif(self.y_image == 2):
                    #print("left2")
                    self.avatar = self.avatar_up2
                    self.y_image = 0
            else:
                #print("y movement done")
                self.y_movement = False

        # setting the final direction of the character.
        if ((not self.x_movement) and (not self.y_movement) and (not self.player_move)):
            #print("setting the final image")
            if final_side == "right":
                self.avatar = self.avatar_right
            if final_side == "left":
                self.avatar = self.avatar_left
            if final_side == "down":
                self.avatar = self.avatar_down
            if final_side == "up":
                self.avatar = self.avatar_up
            self.player_move = True

    def move_dragon(self):
        # movement to negative y-direction.
        if (self.dragon_y > (10)):
            self.dragon_y = self.dragon_y - 10
            if(self.y_image == 0):
                #print("left")
                self.dragon = self.dragonc1
                self.y_image = 1
            elif(self.y_image == 1):
                #print("left1")
                self.dragon = self.dragonc2
                self.y_image = 2
            elif(self.y_image == 2):
                #print("left2")
                self.dragon = self.dragonc3
                self.y_image = 0
        else:
            #print("Dragon movement complete")
            self.dragon_move = True

    # text related function.
    def message_display(self, text, row_no):
        self.text_y1 = 25 * row_no
        label = self.myfont.render(text, 1, self.white)
        print("y1, y2 = ", self.text_y1, self.text_y2)
        self.gameDisplay.blit(label, (940, (30 + self.text_y1)))

    def gameAction(self, selection, text_buff):
        # setting the trigger for custom events.
        #pygame.time.set_timer(self.player_hammer_pick, 250)
        print("start of gameAction")
        count = 0
        alternate = 0
        self.gameLoop = False
        print("selection is", selection)

        # setting the main event control loop.
        while not self.gameLoop:
            if selection == 1:
                pygame.time.set_timer(self.player_hammer_pick, 300)
                selection = 0
            elif selection == 2:
                pygame.time.set_timer(self.player_break_wall, 300)
                selection = 0
            elif selection == 3:
                pygame.time.set_timer(self.player_switch_on, 300)
                selection = 0
                # self.lock.release
            elif selection == 41:
                self.knight_event_control = 1
                pygame.time.set_timer(self.player_goto_knight, 300)
                # self.lock.acquire()
                selection = 0
                # self.lock.release
            elif selection == 42:
                self.knight_event_control = 2
                pygame.time.set_timer(self.player_goto_knight, 300)
                selection = 0
            elif selection == 5:
                pygame.time.set_timer(self.dragon_action, 300)
                selection = 0
            elif selection == 61:
                self.key_event_control = 1
                pygame.time.set_timer(self.key_action, 300)
                selection = 0
            elif selection == 62:
                self.key_event_control = 2
                pygame.time.set_timer(self.key_action, 300)
                selection = 0
            elif selection == 7:
                pygame.time.set_timer(self.treasure_action, 300)
                selection = 0
            elif selection == 81:
                selection = 0
                self.text_event_control = 1
                pygame.time.set_timer(self.text_action, 300)
            elif selection == 82:
                selection = 0
                self.text_array = text_buff.get()
                self.text_event_control = 2
                pygame.time.set_timer(self.text_action, 300)
            elif selection == 9:
                # end of game.
                print("Selection 9, terminate the game")
                pygame.quit()
                quit()
            elif selection == 10:
                self.gameLoop = True

            # clearing the game screen.
            # self.gameDisplay.fill(self.black, rect=None)
            self.displayObject(self.background, 0, 0)

            #if self.display_text:
            word_list = nltk.word_tokenize(self.text_array)
            word_count = 0
            display_text = ""
            row_count = 0
            for word in word_list:
                word_count = word_count + 1
                display_text = display_text + " " + word
                if word_count == 5:
                    row_count = row_count + 1
                    self.message_display(display_text, row_count)
                    word_count = 0
                    display_text = ""
            if word_count > 0:
                row_count = row_count + 1
                self.message_display(display_text, row_count)
                word_count = 0
                display_text = ""
            if self.text_event_control == 1:
                self.displayObject(self.red1, 1030, 400)
            elif self.text_event_control == 2:
                self.displayObject(self.red2, 1030, 400)

            # main event handling loop.
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pass
                    # game ends when selection 9 is passed.

                # hammer pick up.
                if event.type == self.player_hammer_pick:
                    if self.hammer_control:
                        self.x_movement = True
                        self.y_movement = False
                        self.player_move = False
                        self.hammer_control = False
                    self.movePlayer(None, 450, 490, "right")

                    # movement complete.
                    if self.player_move:
                        #print("player movement complete.")
                        pygame.time.set_timer(self.player_hammer_pick, 0)
                        self.gameLoop = True
                        self.hammer_display = False
                        self.control_hammer = True
                        # pygame.time.set_timer(self.player_break_wall, 300)

                # if event.type == self.player_hammer_drop:
                #     self.hammer_display = True
                #     pygame.time.set_timer(self.player_hammer_drop, 0)

                if event.type == self.player_break_wall:
                    if self.brokenWall_control == 0:
                        self.x_movement = False
                        self.y_movement = False
                        self.player_move = False
                        self.hammer_control = False
                        self.movePlayer(None, 450, 490, "up")
                        self.brokenWall_control = 1
                        self.kapow_control = False
                    elif self.brokenWall_control == 1:
                        self.kapow_display1 = True
                        self.kapow = self.kapow1
                        self.brokenWall_control = 2
                    elif self.brokenWall_control == 2:
                        self.kapow = self.kapow1
                        self.brokenWall_control = 3
                    elif self.brokenWall_control == 3:
                        pygame.time.set_timer(self.player_break_wall, 0)
                        self.gameLoop = True
                        self.brokenWall_control = 0
                        self.brokenWall_display = False
                        # pygame.time.set_timer(self.player_switch_on, 300)

                # switch on light.
                if event.type == self.player_switch_on:
                    #print("Inside player switch")
                    if self.switch_control == 0:
                        self.x_movement = True
                        self.y_movement = True
                        self.player_move = False
                        self.switch_control = 1
                    elif self.switch_control == 1:
                        self.movePlayer(None, 450, 400, "left")
                        if self.player_move:
                            self.switch_control = 2
                    elif self.switch_control == 2:
                        self.switch_display = 1
                        self.switch_control = 3
                    elif self.switch_control == 3:
                        pygame.time.set_timer(self.player_switch_on, 0)
                        self.gameLoop = True
                        self.switch_control = 0
                        self.darkroom_display = False
                        # pygame.time.set_timer(self.player_goto_knight, 300)

                # go to the knight.
                if event.type == self.player_goto_knight:
                    if self.knight_event_control == 1:
                        if self.goto_control == 0:
                            self.x_movement = True
                            self.y_movement = True
                            self.player_move = False
                            self.goto_control = 1
                        elif self.goto_control == 1:
                            self.movePlayer(None, 450, 130, "up")
                            if self.player_move:
                                self.goto_control = 2
                        elif self.goto_control == 2:
                            pygame.time.set_timer(self.player_goto_knight, 0)
                            self.gameLoop = True
                            self.goto_control = 0
                            # pygame.time.set_timer(self.player_get_sword, 300)
                    elif self.knight_event_control == 2:
                        pygame.time.set_timer(self.player_goto_knight, 0)
                        self.gameLoop = True
                        self.rock_display = 1
                        self.avatar_right2 = self.avatar_right_sword
                        # pygame.time.set_timer(self.dragon_action, 300)

                # pick up the sword.
                # if event.type == self.player_get_sword:
                #     pygame.time.set_timer(self.player_get_sword, 0)
                #     self.rock_display = 1
                #     self.avatar_right2 = self.avatar_right_sword
                #     pygame.time.set_timer(self.dragon_action, 300)

                # dragon cry movement.
                if event.type == self.dragon_action:
                    #print("Inside Dragon Movement")
                    if self.dragon_control == 0:
                        self.x_movement = True
                        self.y_movement = True
                        self.player_move = False
                        self.dragon_control = 1
                    elif self.dragon_control == 1:
                        print("In dragon control 1")
                        self.movePlayer(None, 550, 240, "right")
                        if self.player_move:
                            self.dragon_control = 2
                    elif self.dragon_control == 2:
                        print("in dragon control 2")
                        self.kapow_x = 540
                        self.kapow_y = 220
                        self.kapow_display2 = True
                        self.dragon_control = 3
                    elif self.dragon_control == 3:
                        self.kapow_display2 = False
                        self.dragon_control = 4
                    elif self.dragon_control == 4:
                        self.move_dragon()
                        if self.dragon_move:
                            pygame.time.set_timer(self.dragon_action, 0)
                            self.gameLoop = True
                            self.dragon_control = 0
                            self.key_display = True
                            self.key_event_control = 1
                            # pygame.time.set_timer(self.key_action, 300)

                if event.type == self.key_action:
                    if self.key_event_control == 1:
                        pygame.time.set_timer(self.key_action, 0)
                        self.gameLoop = True
                        self.key_display = False
                        # pygame.time.set_timer(self.treasure_action, 300)
                    elif self.key_event_control == 2:
                        pygame.time.set_timer(self.key_action, 0)
                        self.gameLoop = True
                        self.key_display = True

                if event.type == self.treasure_action:
                    if self.treasure_control == 0:
                        self.x_movement = True
                        self.y_movement = True
                        self.player_move = False
                        self.treasure_control = 1
                    elif self.treasure_control == 1:
                        self.movePlayer(None, 300, 240, "left")
                        if self.player_move:
                            self.treasure_control = 2
                    elif self.treasure_control == 2:
                        pygame.time.set_timer(self.key_action, 0)
                        self.gameLoop = True
                        self.treasure_display = 2
                        self.treasure_control = 0

                if event.type == self.text_action:
                    pygame.time.set_timer(self.text_action, 0)
                    self.gameLoop = True

            # drawing objects on the screen.
            if self.hammer_display:
                self.displayObject(self.hammer, self.hammer_x, self.hammer_y)

            if self.brokenWall_display:
                self.displayObject(self.brokenWall, self.brokenWall_x, self.brokenWall_y)
                if self.brokenWall_control > 0:
                    # print("kapow displayed", self.kapow_display1)
                    if self.kapow_display1:
                        self.displayObject(self.kapow, self.kapow_x, self.kapow_y)

            if self.switch_display == 0:
                self.displayObject(self.switchoff, self.switch_x, self.switch_y)
            elif self.switch_display == 1:
                self.displayObject(self.switchon, self.switch_x+5, self.switch_y-10)

            self.displayObject(self.knight, self.knight_x, self.knight_y)
            if self.rock_display == 0:
                self.displayObject(self.swordRock, self.rock_x, self.rock_y)
            elif self.rock_display == 1:
                self.displayObject(self.swordNorock, self.rock_x+5, self.rock_y+10)

            if not self.dragon_move:
                self.displayObject(self.dragon, self.dragon_x, self.dragon_y)
                #print("kapow", self.kapow_display2)
                if self.kapow_display2:
                    self.displayObject(self.kapow, self.kapow_x, self.kapow_y)

            if self.key_display:
                self.displayObject(self.key, self.key_x, self.key_y)

            if self.treasure_display == 1:
                self.displayObject(self.ctreasure, self.treasure_x, self.treasure_y)
            elif self.treasure_display == 2:
                self.displayObject(self.otreasure, self.treasure_x, self.treasure_y)

            if self.darkroom_display:
                self.displayObject(self.darkroom, self.darkroom_x, self.darkroom_y)

            self.displayObject(self.avatar, self.avatar_pos_x, self.avatar_pos_y)
            # refreshing the screen.
            pygame.display.flip()
            self.clock.tick(60)

        # end of game.
        # pygame.quit()
        # quit()

def start_game(buff, text_buff, buff2):
    g = GameInstance()
    while True:
        action = buff.get()
        print("action is", action)
        g.gameAction(action, text_buff)
        print("returned from game action")
        buff2.put(1)

def control_thread(buff, text_buff,buff2):
    print("In the control threadpython ")
    startDialogManager(buff, text_buff, buff2)

if __name__ == "__main__":
    print("queue created!")
    event_buff = mp.Queue()
    event_buff.put(10)

    buff2 = mp.Queue()
    # buff2.put(1)
    text_buff = mp.Queue()

    # starting game thread.
    gameThread = threading.Thread(target=control_thread, args=(event_buff,text_buff,buff2,))
    gameThread.start()

    start_game(event_buff, text_buff, buff2)
