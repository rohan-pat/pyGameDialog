import pygame
from pygame.locals import *
from os.path import abspath, expanduser

class GameInstance:
    def __init__(self):
        pygame.init()

        # setting clock for the game.
        self.clock = pygame.time.Clock()

        # display window properties.
        display_width = 800
        display_height = 600
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Find The Treasure")

        # colors for the same.
        self.black = (0,0,0)
        self.white = (255,255,255)

        # game images.
        filepath = abspath(expanduser("~/") + "/Documents/Studies/NLP/Project/pyGameDialog/images/")
        self.avatar = pygame.image.load(filepath+"/avatar.png")
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
    g = GameInstance()
    g.startGame()
