import pygame
from pygame.locals import *
from os.path import abspath, expanduser

class AvatarData:
    def __init__(self):
        self.avatar_xm = pygame.image.load()
        self.avatar_x1 = pygame.image.load()

class GameInstance:
    def __init__(self):
        pygame.init()

        # setting clock for the game.
        self.clock = pygame.time.Clock()

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
        self.avatar_down = pygame.image.load(filepath+"/herodown.png")
        self.avatar_down1 = pygame.image.load(filepath+"/herodown1.png")
        self.avatar_down2 = pygame.image.load(filepath+"/herodown2.png")
        self.avatar_left = pygame.image.load(filepath+"/heroleft.png")
        self.avatar_left1 = pygame.image.load(filepath+"/heroleft1.png")
        self.avatar_left2 = pygame.image.load(filepath+"/heroleft2.png")
        self.avatar_right = pygame.image.load(filepath+"/heroright.png")
        self.avatar_right1 = pygame.image.load(filepath+"/heroright1.png")
        self.avatar_right2 = pygame.image.load(filepath+"/heroright2.png")
        self.avatar_up = pygame.image.load(filepath+"/heroup.png")
        self.avatar_up1 = pygame.image.load(filepath+"/heroup1.png")
        self.avatar_up2 = pygame.image.load(filepath+"/heroup2.png")

        # initial ava
        self.avatar_pos_x = 100
        self.avatar_pos_y = 100
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

        self.dragon_x = 700;
        self.dragon_y = 300;
        self.dragon_move = False

        # text positions.
        self.text_position_x = 1000
        self.text_position_y = 10

        # custom user events for controlling the game.
        self.player_movement = pygame.USEREVENT + 1
        self.dragon_movement = pygame.USEREVENT + 2

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
                    print("right")
                    self.avatar = self.avatar_right1
                    self.x_image = 1
                elif(self.x_image == 1):
                    print("right1")
                    self.avatar = self.avatar_right
                    self.x_image = 2
                elif(self.x_image == 2):
                    print("right2")
                    self.avatar = self.avatar_right2
                    self.x_image = 0
            # movement to negative x-direction.
            elif (self.avatar_pos_x > (final_x-10)):
                self.avatar_pos_x = self.avatar_pos_x - 10
                if(self.x_image == 0):
                    print("left")
                    self.avatar = self.avatar_left1
                    self.x_image = 1
                elif(self.x_image == 1):
                    print("left1")
                    self.avatar = self.avatar_left
                    self.x_image = 2
                elif(self.x_image == 2):
                    print("left2")
                    self.avatar = self.avatar_left2
                    self.x_image = 0
            else:
                print("x movement done")
                self.x_movement = False
        elif self.y_movement:
            if (self.avatar_pos_y < (final_y-10)):
                self.avatar_pos_y = self.avatar_pos_y + 10
                if(self.y_image == 0):
                    print("down")
                    self.avatar = self.avatar_down1
                    self.y_image = 1
                elif(self.y_image == 1):
                    print("down1")
                    self.avatar = self.avatar_down
                    self.y_image = 2
                elif(self.y_image == 2):
                    print("down2")
                    self.avatar = self.avatar_down2
                    self.y_image = 0
            # movement to negative y-direction.
            elif (self.avatar_pos_y > (final_y-10)):
                self.avatar_pos_y = self.avatar_pos_y - 10
                if(self.y_image == 0):
                    print("left")
                    self.avatar = self.avatar_up1
                    self.y_image = 1
                elif(self.y_image == 1):
                    print("left1")
                    self.avatar = self.avatar_up
                    self.y_image = 2
                elif(self.y_image == 2):
                    print("left2")
                    self.avatar = self.avatar_up2
                    self.y_image = 0
            else:
                print("y movement done")
                self.y_movement = False

        # setting the final direction of the character.
        if ((not self.x_movement) and (not self.y_movement) and (not self.player_move)):
            print("setting the final image")
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
        if (self.dragon_y > (100)):
            self.dragon_y = self.dragon_y - 10
            if(self.y_image == 0):
                print("left")
                self.dragon = self.dragonc1
                self.y_image = 1
            elif(self.y_image == 1):
                print("left1")
                self.dragon = self.dragonc2
                self.y_image = 2
            elif(self.y_image == 2):
                print("left2")
                self.dragon = self.dragonc3
                self.y_image = 0
        else:
            print("Dragon movement complete")
            self.dragon_move = True
            pygame.time.set_timer(self.dragon_movement, 0)

    # text related function.
    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.white)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf',16)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (self.text_position_x,self.text_position_y)
        self.gameDisplay.blit(TextSurf, TextRect)

    def startGame(self):
        # setting the trigger for custom events.
        pygame.time.set_timer(self.player_movement, 300)

        count = 0
        gameLoop = False
        alternate = 0

        # setting the main event control loop.
        while not gameLoop:
            # clearing the game screen.
            # print("count is",count)
            self.gameDisplay.fill(self.black, rect=None)
            self.displayObject(self.background, 0, 0)
            self.text_position_x = 1000
            self.text_position_y = 10
            self.message_display("Hi, Welcome to Find")
            self.text_position_x = 1000
            self.text_position_y = 30
            self.message_display(" The Treasure!")

            self.text_position_x = 1200
            self.text_position_y = 40
            self.message_display("Thank you!")

            # main event handling loop.
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    gameLoop = True

                if event.type == self.player_movement:
                    self.movePlayer(None, 600, 300, "right")
                    if self.player_move:
                        print("changing player events")
                        pygame.time.set_timer(self.dragon_movement, 300)
                        pygame.time.set_timer(self.player_movement, 0)

                if event.type == self.dragon_movement:
                    print("Inside Dragon Movement")
                    self.move_dragon()

            # drawing objects on the screen.
            self.displayObject(self.avatar, self.avatar_pos_x, self.avatar_pos_y)

            if not self.dragon_move:
                self.displayObject(self.dragon, self.dragon_x, self.dragon_y)

            count += 1
            # refreshing the screen.
            pygame.display.flip()
            self.clock.tick(60)

        # end of game.
        pygame.quit()
        quit()

if __name__ == "__main__":
    g = GameInstance()
    g.startGame()
