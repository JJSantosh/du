import pygame
import random
from pygame import mixer
mixer.init()

color="blue"

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        #self.image.fill(surf_colors)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,w,h))
        self.rect=self.image.get_rect() 

    def moveRight(self,pix):
        self.rect.x += pix
    def moveLeft(self,pix):
        self.rect.x -= pix
    def moveForward(self,speed):
        self.rect.y -= speed*speed/10
    def moveBackword(self,speed):
        self.rect.y += speed*speed/10

#bg=pygame.image.load("bg.jpeg")
#bg=pygame.transform.scale(bg,(500,500))

pygame.init()
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("ADD SPRITE")
all_sprites_list=pygame.sprite.Group()

sp1=Sprite(color,50,50)
sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,380)
all_sprites_list.add(sp1)

sp2=Sprite("orange",50,50)
sp2.rect.x=random.randint(0,480)
sp2.rect.y=random.randint(0,380)
all_sprites_list.add(sp2)

exit=True
clock=pygame.time.Clock()

rad = 20

while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                exit=False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        sp1.moveRight(5)
    if keys[pygame.K_UP]:
        sp1.moveForward(5)
    if keys[pygame.K_DOWN]:
        sp1.moveBackword(5)

    all_sprites_list.update()
    #screen.blit(bg,(0,0))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    
    if sp1.rect.colliderect(sp2.rect):
        all_sprites_list.remove(sp2)
        text="YOU WIN"
        font=pygame.font.SysFont("Times new Roman", 50)

        text=font.render(text,True,(158,16,16))

        screen.blit(text,(200-text.get_width()// 2, 150-text.get_height()//2))
    pygame.display.update()
    clock.tick(60)

pygame.quit()