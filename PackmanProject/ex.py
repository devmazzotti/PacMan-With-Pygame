from pygame import *
init()
screen = display.set_mode((608,609))
img = image.load("./Imgs/fmap.png").convert()
collisionPoints = []
apresentedImage = screen.blit(img,(0,0))
for i in range(608):
    for x in range(609):
        if(img.get_at((i,x)) !=(0,0,0) ):
            collisionPoints.append((i,x))
print(collisionPoints)

display.update()
