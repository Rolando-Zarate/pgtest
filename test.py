import pygame
import sys
pygame.init()
window = pygame.display.set_mode(((500,400)))
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("Arial",20)
x = 0
loopc = True
itern = 1
def draw():
    global x
    pygame.draw.rect(window,(20,20,20),pygame.Rect(x,150,60,60))
    if x >= 500:
        x = 0
    else:
        x += itern
def screen():
    window.fill((50,50,50))
    window.blit(font.render("pgtest",True,(255,255,255)),(10,10))
    window.blit(font.render("fps: "+str(fps),True,(255,255,255)),(10,30))
    window.blit(font.render("teps per update: "+str(itern),True,(255,255,255)),(10,45))
    draw()
def update():
    clock.tick(fps)
    screen()
    pygame.display.update()
def loop():
    global loopc
    while loopc:
        update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loopc = False
                #sys.exit()
def main():
    loop()
    
