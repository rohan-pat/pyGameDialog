
import pygame
from multiprocessing import Queue
import time
import threading
import random



class Image:
    def __init__(self):
        pygame.init()
        gameLoop = False
        #self.clock = pygame.time.Clock()

        # display window properties.
        display_width = 1280
        display_height = 800
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        #pygame.display.set_caption("Find The Treasure")
        self.imageBackground= pygame.image.load("gamefinalbackground.png")
        self.imageBackground=pygame.transform.scale(self.imageBackground, (900,600))
        self.herodown=pygame.image.load("herodown.png")
        self.herodown=pygame.transform.scale(self.herodown, (40,40))
        self.lightoff= pygame.image.load("lightcauldronoff.png")
        self.lighton= pygame.image.load("lightcauldronon.png")
        self.kapow= pygame.image.load("kapow.png")
        self.kapow=pygame.transform.scale(self.kapow, (60,50))
        self.ctreasure=pygame.image.load("ctreasure.png")
        self.rockwithoutsword= pygame.image.load("rockwithoutsword.png")
        self.swordrock=pygame.image.load("swordrock.png")
        self.swordrock=pygame.transform.scale(self.swordrock, (79,73))
        self.armor=pygame.image.load("armor1.png")
        self.armor=pygame.transform.scale(self.armor, (79,73))
        self.dragon=pygame.image.load("dragon.png")
        self.dragonback=pygame.image.load("dragonback.png")
        self.dragonbackback=pygame.image.load("dragonbackback.png")
        self.dragonbackfront=pygame.image.load("dragonbackfront.png")
        self.hammer=pygame.image.load("hammer.png")
        self.hammer=pygame.transform.scale(self.hammer,(100,100))
        self.key=pygame.image.load("key5.png")
        self.scratchwall=pygame.image.load("scratchwall.png")
    def displayObject(self, image, x, y):
        """This method is used to load the image on the screen."""
        self.gameDisplay.blit(image, (x,y))
    def image(self):
        gameLoop=False
        while not gameLoop:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    gameLoop = True

            self.gameDisplay.blit(self.imageBackground,(150,100))
            self.displayObject(self.herodown,500,650)
            self.displayObject(self.hammer,580,650)
            self.displayObject(self.scratchwall,565,565)
            self.displayObject(self.armor,550,155)
            self.displayObject(self.swordrock,571,206)
            self.displayObject(self.dragon,720,300)
            self.displayObject(self.ctreasure,400,350)
            self.displayObject(self.key,680,320)
            self.displayObject(self.lightoff,630,530)
            self.displayObject(self.lighton,400,470)
            self.displayObject(self.lighton,770,470)
            self.displayObject(self.lighton,770,160)
            self.displayObject(self.lighton,400,160)
            self.displayObject(self.kapow,665,330)
            pygame.display.update()

        pygame.quit()
        quit()
class GameInstance:
    def __init__(self):
        pygame.init()

        # setting clock for the game.


        # colors for the same.
        self.black = (0,0,0)
        self.white = (255,255,255)

        # game images.
        #filepath = abspath(expanduser("~/") + "/Documents/Studies/NLP/Project/pyGameDialog/images/")
        self.avatar = pygame.image.load("spritehero.png")
        self.avatar_pos_finalx = 700
        self.avatar_pos_finaly = 500
        self.avatar_pos_x = self.avatar_pos_finalx*0.4
        self.avatar_pos_y = self.avatar_pos_finaly*0.8

        # custom user events for controlling the game.
        self.player_movement = pygame.USEREVENT + 1

    def displayObject(self, image, x, y):
        """This method is used to load the image on the screen."""
        self.gameDisplay.blit(image, (x,y))

    def startGame(self):
        # setting the trigger for custom events.
        pygame.time.set_timer(self.player_movement, 300)

        x = 0
        gameLoop = False

        # setting the main event control loop.
        while not gameLoop:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    gameLoop = True

                if event.type == self.player_movement:
                    if(self.avatar_pos_x < (self.avatar_pos_finalx-8)):
                        self.avatar_pos_x = self.avatar_pos_x + 8
                    elif(self.avatar_pos_y < (self.avatar_pos_finaly-8)):
                        self.avatar_pos_y = self.avatar_pos_y + 8
                    else:
                        gameLoop = True

            # drawing objects on the screen.
            self.gameDisplay.fill(self.black)
            self.displayObject(self.avatar, self.avatar_pos_x, self.avatar_pos_y)
            x = 0

            # refreshing the screen.
            pygame.display.update()
            self.clock.tick(60)

        # end of game.
        pygame.quit()
        quit()
if __name__ == "__main__":
    g = Image()
    g.image()
