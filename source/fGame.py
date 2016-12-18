
import pygame
from multiprocessing import Queue
import time
import threading
import random
from os.path import abspath, expanduser
import nltk


class Image:
    def __init__(self):
        pygame.init()
        gameLoop = False
        #self.clock = pygame.time.Clock()
        self.myfont = pygame.font.SysFont("Helvetica", 30)

        # display window properties.
        filepath = abspath(expanduser("~/") + "/Documents/Studies/NLP/Project/pyGameDialog/images/")
        display_width = 1265
        display_height= 550
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        #pygame.display.set_caption("Find The Treasure")
        self.imageBackground= pygame.image.load(filepath+"/backWithDialog.png")
        self.imageBackground=pygame.transform.scale(self.imageBackground, (1265,550))
        self.herodown=pygame.image.load(filepath+"/herodown.png")
        self.herodown=pygame.transform.scale(self.herodown, (40,40))
        self.lightoff= pygame.image.load(filepath+"/lightcauldronoff.png")
        self.lighton= pygame.image.load(filepath+"/lightcauldronon.png")
        self.kapow= pygame.image.load(filepath+"/kapow.png")
        self.kapow=pygame.transform.scale(self.kapow, (60,50))
        self.ctreasure=pygame.image.load(filepath+"/closedTreasure.png")
        self.rockwithoutsword= pygame.image.load(filepath+"/rockwithoutsword.png")
        self.swordrock=pygame.image.load(filepath+"/swordRock.png")
        self.swordrock=pygame.transform.scale(self.swordrock, (79,73))
        self.armor=pygame.image.load(filepath+"/armor1.png")
        self.armor=pygame.transform.scale(self.armor, (79,73))
        self.dragon=pygame.image.load(filepath+"/dragon.png")
        self.dragonback=pygame.image.load(filepath+"/dragon.png")
        self.dragonbackback=pygame.image.load(filepath+"/dragonCry1.png")
        self.dragonbackfront=pygame.image.load(filepath+"/dragonCry2.png")
        self.hammer=pygame.image.load(filepath+"/hammer.png")
        self.hammer=pygame.transform.scale(self.hammer,(100,100))
        self.key=pygame.image.load(filepath+"/key5.png")
        self.scratchwall=pygame.image.load(filepath+"/scratchwall.png")
        self.scratchwall=pygame.transform.scale(self.scratchwall,(62,71))
        self.red1 = pygame.image.load(filepath+"/red1.png")
        self.red2 = pygame.image.load(filepath+"/red2.png")
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

            self.gameDisplay.blit(self.imageBackground,(0,0))
            self.displayObject(self.herodown,320,490)
            self.displayObject(self.hammer,440,485)
            self.displayObject(self.scratchwall,432,427)
            self.displayObject(self.armor,420,40)
            self.displayObject(self.swordrock,440,90)
            self.displayObject(self.dragon,580,200)
            self.displayObject(self.ctreasure,250,220)
            self.displayObject(self.key,540,180)
            self.displayObject(self.lightoff,530,390)
            self.displayObject(self.lighton,250,330)
            self.displayObject(self.lighton,250,60)
            self.displayObject(self.lighton,640,330)
            self.displayObject(self.lighton,640,60)
            self.displayObject(self.kapow,432,437)
            self.displayObject(self.kapow,540,220)
            self.text_y1 = 0
            self.text_y2 = 0
            self.white = (255, 255, 255)
            self.text_array = ["pick up the sword", "use the hammer to break the door", "kill the dragon"]
            if True:
                for item in self.text_array:
                    word_list = nltk.word_tokenize(item)
                    word_count = 0;
                    display_text = ""
                    for word in word_list:
                        word_count = word_count + 1
                        display_text = display_text + " " + word
                        if word_count == 5:
                            text = self.myfont.render(display_text, 1, self.white)
                            self.gameDisplay.blit(text, (940, (30 + self.text_y1 + self.text_y2)))
                            word_count = 0
                            display_text = ""
                            self.text_y1 = self.text_y1 + 25
                    if word_count > 0:
                        text = self.myfont.render(display_text, 1, self.white)
                        self.gameDisplay.blit(text, (940, (30 + self.text_y1 + self.text_y2)))
                        self.text_y1 = self.text_y1 + 25
                        display_text = ""
                        word_count = 0
                    self.text_y2 = self.text_y2 + 10
            self.displayObject(self.red2, 1030, 400)
            pygame.display.update()

        pygame.quit()
        quit()

if __name__ == "__main__":
    g = Image()
    g.image()
