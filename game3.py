import pygame
from multiprocessing import Queue
import time
import threading
#pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size=(32, 32), image=None):
        super(Button, self).__init__()
        if image is None:
            self.rect = pygame.Rect(pos, size)
            self.image = pygame.Surface(size)
        else:
            self.image = image
        #    pygame.transform.scale(self.image, (5, 5))
            self.rect = image.get_rect(topleft=pos)
        self.pressed = False

    def update(self, action,key,hammer,door):
        #action="bd"
        #mouse_pos = pygame.mouse.get_pos()
        #mouse_clicked = pygame.mouse.get_pressed()[0]
        key1=key
        hammer1=hammer
        door1=door
        if(action=="pk" or key1==0):
            key1=0
            if self.rect.collidepoint(350, 325) :
                print("key picked up")
                self.kill()
        if(action=="ph"or hammer==0):
            hammer1=0
            if self.rect.collidepoint(650, 325) :
                print("hammer picked up")
                self.kill()
        if(action=="ud" or action=="bd"):
            print("outer loop")

            if self.rect.collidepoint(450, 80) :
                print("inner loop")
                self.door=1
                print("closed door is hidden")
                self.kill()

        return key1,hammer1,door1

class Image:

    def __init__(self):
        pygame.init()
        self.hammer=2
        self.key=2
        self.door=0
        self.firstRun = True
        self.screen = pygame.display.set_mode((860,640))
        #clock = pygame.time.Clock()
        self.imaged = pygame.image.load("Dungeon.jpg")
        self.imaged=pygame.transform.scale(self.imaged, (600,600))
        self.image = pygame.image.load("key.png")
        self.image=pygame.transform.scale(self.image, (50, 50))
        self.imagedooropen = pygame.image.load("Odoor.png")
        self.imagedooropen=pygame.transform.scale(self.imagedooropen, (100, 100))
        self.imagedoorclose = pygame.image.load("Cdoor.png")
        self.imagedoorclose=pygame.transform.scale(self.imagedoorclose, (100, 100))
        self.imagehammer = pygame.image.load("hammer.png")
        self.imagehammer=pygame.transform.scale(self.imagehammer, (50, 50))
        #image.fill((255, 0, 0))
        self.buttons = pygame.sprite.Group()
        self.buttons.add(
            Button(pos=(350, 325), image=self.image),
            Button(pos=(450, 80), image=self.imagedoorclose),
            Button(pos=(650, 325), image=self.imagehammer)
        )

    def imagemov(self, action):
        #action="bd"

        while True:
            #clock.tick(60)
            #buttons.add(Button(pos=(350, 325), image=image))
            #for event in pygame.event.get():
                #event.type=pygame.KEYDOWN
                #if event.type == pygame.QUIT:
                    #quit()

                    #elif event.key == pygame.K_2:
                        #buttons.add(Button(pos=(450, 80), image=imagedooropen))
                    #elif event.key == pygame.K_3:
                        #buttons.add(Button(pos=(650, 325), image=imagehammer))

            #buttons.add(Button(pos=(450, 80), image=imagedooropen))
              # Calls the update method on every sprite in the group.

            self.screen.blit(self.imaged,(200,50))
            if(action=="ud" or action=="bd" or self.door==0):
                print("open door is displayed")
                self.screen.blit(self.imagedooropen,(450,80))
            if(action=="rk"):
                print("key is dropped")
                self.key=1
                self.screen.blit(self.image,(350,325))
            if(action=="rh"):
                print("hammer is dropped")
                self.hammer=1
                self.screen.blit(self.imagehammer,(650,325))
            self.buttons.update(action,self.key,self.hammer,self.door)
            #screen.fill((255, 255, 255))
            self.buttons.draw(self.screen)  # Draws  all sprites to the given Surface.
            pygame.display.update()
            break

    def start_thread(buff):
        img = Image()
        while True:
            action = buff.get()
            print(action)
            img.imagemov(action)

if __name__ == "__main__":
    buff = Queue()
    buff.put("pka")

    gameThread = threading.Thread(
    target=Image.start_thread, args=(buff,))
    gameThread.start()

    time.sleep(3)
    buff.put("pk")
    time.sleep(3)
    buff.put("rk")
    time.sleep(3)
    buff.put("ph")
    time.sleep(3)
    buff.put("rh")
    #buff.join()
