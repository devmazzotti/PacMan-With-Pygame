from pygame import *
from threading import Thread
class Game(object):

    def __init__(self):


        ##SCREEN SET'S##
        self.backgroundColor = "40,56,150"


        ##MAP SET'S##
        self.xMap=608
        self.yMap=609
        self.screen = display.set_mode((self.xMap, self.yMap))

        self._map = image.load("./Imgs/fmap.png").convert()


        self.pacManConfig()
        self.ghostConfig()


        display.init()

        display.set_caption("Pacman")
        self.runGame()

    def ghostConfig(self):
        self._ghostImg0 = "./Imgs/Ghost/ghost0.png"
        self._ghostImg1 = "./Imgs/Ghost/ghost1.png"





    def pacManConfig(self):
        self._pacManImg0 = image.load("./Imgs/PacMan/pac0.png")
        self._pacManImg0 = transform.scale(self._pacManImg0, (27, 27))
        self._pacManImg1 = image.load("./Imgs/PacMan/pac1.png")
        self._pacManImg1 = transform.scale(self._pacManImg1, (27, 27))
        self._pacManImg2 = image.load("./Imgs/PacMan/pac2.png")
        self._pacManImg2 = transform.scale(self._pacManImg2, (27, 27))
        self._pacManImg3 = image.load("./Imgs/PacMan/pac3.png")
        self._pacManImg3 = transform.scale(self._pacManImg3, (27, 27))
        self._pacManImg4 = image.load("./Imgs/PacMan/pac4.png")
        self._pacManImg4 = transform.scale(self._pacManImg4, (27, 27))

            #FLIPPED
        self.f_pacManImg0 = transform.scale(transform.flip(image.load("./Imgs/PacMan/pac0.png"), True, False), (27, 27))
        self.f_pacManImg1 = transform.scale(transform.flip(image.load("./Imgs/PacMan/pac1.png"), True, False), (27, 27))
        self.f_pacManImg2 = transform.scale(transform.flip(image.load("./Imgs/PacMan/pac2.png"), True, False), (27, 27))
        self.f_pacManImg3 = transform.scale(transform.flip(image.load("./Imgs/PacMan/pac3.png"), True, False), (27, 27))
        self.f_pacManImg4 = transform.scale(transform.flip(image.load("./Imgs/PacMan/pac4.png"), True, False), (27, 27))

            # CURRENT #

        self.pacManimgCurrent0 = self._pacManImg0
        self.pacManimgCurrent1 = self._pacManImg1
        self.pacManimgCurrent2 = self._pacManImg2
        self.pacManimgCurrent3 = self._pacManImg3
        self.pacManimgCurrent4 = self._pacManImg4






        self.pacManDirection = "Right"
        self.canPacManTurnPosition = True

        self.pacManAngle = 0
        self.pacManSpeedCount = 0

        self._pacManX=170 - int(25/2)
        self._pacManY=305 - int(25/2)


        self.pacManCount=0 # It's for speed purposes...




    def runGame(self):
        while True: ## we'r in infinite Loop <3

            #self.screen.fill((0, 0, 0))
            self.screen.blit(self._map, (0,0))


            #UPDATE COUNT'S#
            self.pacManCount+=1 ## It's for speed purposes..
            self.pacManSpeedCount+=1
            ###############
            self.keyboards_detects()
            self.draw_pacman()


            display.flip()

            #ALL COUNT'S
            if (self.pacManCount >= 1000): ## It represents animation's speed..
                self.pacManCount = 0
            if(self.pacManSpeedCount >= 30):  ## It represents pacman walk's speed..
                self.pacManSpeedCount = 0

    def keyboards_detects(self):
        self._kbEvent = event.poll()
        self.kbEvent = key.get_pressed()
        if(self._kbEvent.type == QUIT):
            quit()
        if(self.kbEvent[K_a]):
            if (self._map.get_at((self._pacManX - 7, self._pacManY)) != (0, 0, 255)):
                if (self._map.get_at((self._pacManX - 7, self._pacManY + 27)) != (0, 0, 255)):
                    self.pacManDirection="Left"
        elif(self.kbEvent[K_d]):
            if (self._map.get_at((self._pacManX + 29, self._pacManY)) != (0, 0, 255)):
                if (self._map.get_at((self._pacManX + 29, self._pacManY + 27)) != (0, 0, 255)):
                    self.pacManDirection = "Right"
        elif(self.kbEvent[K_w]):
            if (self._map.get_at((self._pacManX + 25, self._pacManY - 5)) != (0, 0, 255)):
                if (self._map.get_at((self._pacManX - 5, self._pacManY - 5)) != (0, 0, 255)):
                    self.pacManDirection = "Up"
        elif(self.kbEvent[K_s]):
            if (self._map.get_at((self._pacManX - 5, self._pacManY+30)) != (0, 0, 255)):
                if (self._map.get_at((self._pacManX + 25, self._pacManY + 30)) != (0, 0, 255)):
                    self.pacManDirection = "Down"

    def draw_ghost(self):
        pass


    def draw_pacman(self):
        # WALKING AND COLLISION DETECT
        if(self.pacManSpeedCount>=30):
            if(self.pacManDirection == "Right"):
                if(self._map.get_at((self._pacManX+27,self._pacManY)) !=(0,0,255)):
                    if (self._map.get_at((self._pacManX+27, self._pacManY + 25)) != (0, 0, 255)):
                        self._pacManX+=1
                        self.pacManAngle=0
                        self.pacManimgCurrent0 = self._pacManImg0
                        self.pacManimgCurrent1 = self._pacManImg1
                        self.pacManimgCurrent2 = self._pacManImg2
                        self.pacManimgCurrent3 = self._pacManImg3
                        self.pacManimgCurrent4 = self._pacManImg4
            if (self.pacManDirection == "Left"):
                if (self._map.get_at((self._pacManX - 5, self._pacManY)) != (0, 0, 255)):
                    if (self._map.get_at((self._pacManX - 5, self._pacManY + 25)) != (0, 0, 255)):
                        self._pacManX -= 1
                        self.pacManAngle = 0
                        self.pacManimgCurrent0 = self.f_pacManImg0
                        self.pacManimgCurrent1 = self.f_pacManImg1
                        self.pacManimgCurrent2 = self.f_pacManImg2
                        self.pacManimgCurrent3 = self.f_pacManImg3
                        self.pacManimgCurrent4 = self.f_pacManImg4
            if (self.pacManDirection == "Up"):
                if (self._map.get_at((self._pacManX + 25, self._pacManY - 5)) != (0, 0, 255)):
                    if (self._map.get_at((self._pacManX, self._pacManY - 5)) != (0, 0, 255)):
                        self._pacManY -= 1
                        self.pacManAngle = 90
                        self.pacManimgCurrent0 = self._pacManImg0
                        self.pacManimgCurrent1 = self._pacManImg1
                        self.pacManimgCurrent2 = self._pacManImg2
                        self.pacManimgCurrent3 = self._pacManImg3
                        self.pacManimgCurrent4 = self._pacManImg4

            if (self.pacManDirection == "Down"):
                if (self._map.get_at((self._pacManX, self._pacManY+30)) != (0, 0, 255)):
                    if (self._map.get_at((self._pacManX + 25, self._pacManY + 30)) != (0, 0, 255)):
                        self._pacManY += 1
                        self.pacManAngle = -90
                        self.pacManimgCurrent0 = self._pacManImg0
                        self.pacManimgCurrent1 = self._pacManImg1
                        self.pacManimgCurrent2 = self._pacManImg2
                        self.pacManimgCurrent3 = self._pacManImg3
                        self.pacManimgCurrent4 = self._pacManImg4





        if(self.pacManCount >= 0 and self.pacManCount <100):
            self.screen.blit(transform.rotate(self.pacManimgCurrent0,self.pacManAngle) , (self._pacManX,self._pacManY))
        elif(self.pacManCount >= 100 and self.pacManCount <200):
            self.screen.blit(transform.rotate(self.pacManimgCurrent1,self.pacManAngle), (self._pacManX,self._pacManY))
        elif (self.pacManCount >= 200 and self.pacManCount <300):
            self.screen.blit(transform.rotate(self.pacManimgCurrent2,self.pacManAngle), (self._pacManX,self._pacManY))
        elif (self.pacManCount >= 300 and self.pacManCount <400):
            self.screen.blit(transform.rotate(self.pacManimgCurrent3,self.pacManAngle), (self._pacManX,self._pacManY))
        elif (self.pacManCount >= 400 and self.pacManCount <500):
            self.screen.blit(transform.rotate(self.pacManimgCurrent4,self.pacManAngle), (self._pacManX,self._pacManY))
        elif (self.pacManCount >= 500 and self.pacManCount <600):
            self.screen.blit(transform.rotate(self.pacManimgCurrent4,self.pacManAngle), (self._pacManX,self._pacManY))
        elif (self.pacManCount >= 600 and self.pacManCount <700):
            self.screen.blit(transform.rotate(self.pacManimgCurrent3,self.pacManAngle), (self._pacManX,self._pacManY))
        elif (self.pacManCount >= 700 and self.pacManCount <800):
            self.screen.blit(transform.rotate(self.pacManimgCurrent2,self.pacManAngle), (self._pacManX,self._pacManY))
        elif (self.pacManCount >= 800 and self.pacManCount < 900):
            self.screen.blit(transform.rotate(self.pacManimgCurrent1,self.pacManAngle), (self._pacManX,self._pacManY))
        if (self.pacManCount >= 900 or self.pacManCount == 0):
            self.screen.blit(transform.rotate(self.pacManimgCurrent0,self.pacManAngle), (self._pacManX,self._pacManY))

        # RUN CONFIGURATION #







Game()