import pygame
pygame.init()

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

    def update(self):
        action="bd"
        #mouse_pos = pygame.mouse.get_pos()
        #mouse_clicked = pygame.mouse.get_pressed()[0]

        if(action=="pk"):
            if self.rect.collidepoint(350, 325) :
                self.kill()
        if(action=="ph"):
            if self.rect.collidepoint(650, 325) :
                self.kill()
        if(action=="ud" or action=="bd"):
            if self.rect.collidepoint(450, 80) :
                self.kill()
class Image(object):
    def imagemov():
        action="bd"
        screen = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
        clock = pygame.time.Clock()
        imaged = pygame.image.load("Dungeon.jpg")
        imaged=pygame.transform.scale(imaged, (600,600))
        image = pygame.image.load("key.png")
        image=pygame.transform.scale(image, (50, 50))
        imagedooropen = pygame.image.load("Odoor.png")
        imagedooropen=pygame.transform.scale(imagedooropen, (100, 100))
        imagedoorclose = pygame.image.load("Cdoor.png")
        imagedoorclose=pygame.transform.scale(imagedoorclose, (100, 100))
        imagehammer = pygame.image.load("hammer.png")
        imagehammer=pygame.transform.scale(imagehammer, (50, 50))
        #image.fill((255, 0, 0))
        buttons = pygame.sprite.Group()
        buttons.add(
            Button(pos=(350, 325), image=image),
            Button(pos=(450, 80), image=imagedoorclose),
            Button(pos=(650, 325), image=imagehammer)
        )

        while True:
            clock.tick(60)
            #buttons.add(Button(pos=(350, 325), image=image))
            for event in pygame.event.get():
                #event.type=pygame.KEYDOWN
                if event.type == pygame.QUIT:
                    quit()

                    #elif event.key == pygame.K_2:
                        #buttons.add(Button(pos=(450, 80), image=imagedooropen))
                    #elif event.key == pygame.K_3:
                        #buttons.add(Button(pos=(650, 325), image=imagehammer))

            #buttons.add(Button(pos=(450, 80), image=imagedooropen))
            buttons.update()  # Calls the update method on every sprite in the group.

            #screen.fill((255, 255, 255))
            buttons.draw(screen)  # Draws  all sprites to the given Surface.
            pygame.display.update()
            screen.blit(imaged,(200,50))
            if(action=="ud" or action=="bd"):
                screen.blit(imagedooropen,(450,80))
            if(action=="rk"):
                screen.blit(image,(350,325))
            if(action=="rh"):
                screen.blit(imagehammer,(650,325))
def main():
    Image.imagemov()
if __name__ == "__main__": main()
