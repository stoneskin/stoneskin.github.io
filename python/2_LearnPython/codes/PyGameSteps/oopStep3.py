# step 2: Create Player Class

# 1.1 - Import library
import pygame

class Player:
    img=pygame.image.load("images/player.png")
    key_up=key_down=key_left=key_right = False
    pos=[100,100]
    speed=0.3
    def __init__(self,x,y) -> None:
       self.pos=[x,y]
    def update(self,screen):
       self.move()
       screen.blit(self.img, self.pos)       
     
    def onKeyEvent(self,event:any) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                self.key_up=True
            elif event.key==pygame.K_a:
                self.key_left=True
            elif event.key==pygame.K_s:
                self.key_down=True
            elif event.key==pygame.K_d:
                self.key_right=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                self.key_up=False
            elif event.key==pygame.K_a:
                self.key_left=False
            elif event.key==pygame.K_s:
                self.key_down=False
            elif event.key==pygame.K_d:
                self.key_right=False
        
    def move(self)->None:
        if self.key_up:
            self.pos[1]-=self.speed
        elif self.key_down:
            self.pos[1]+=self.speed
        if self.key_left:
            self.pos[0]-=self.speed
        elif self.key_right:
            self.pos[0]+=self.speed
             

         
# main class of the Game
class AirForceGame:
    width, height = 640, 480
    def __init__(self,w,h) -> None:
        self.background = pygame.image.load("images/sky.jpg")
        if(w>100):
            self.width=w
        if(h>100):
            self.height=h
    def startGame(self):
        # 1.2 - Initialize the game 
        pygame.init()
       
        screen=pygame.display.set_mode((self.width, self.height))
        keep_going = True
        self.player=Player(100,100)

       
        # 1.4 - use loop to keep the game running 
        while keep_going:
            screen.fill(0)

            screen.blit(self.background,(0,0))

            self.player.update(screen)
            
            #1.7 - update the screen
            pygame.display.flip() # will update the contents of the entire display, and faster than .update()
            # 1.8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type==pygame.QUIT:
                    keep_going = False
                self.player.onKeyEvent(event) #update player for event 
   
        #1.9 exit pygame and python
        pygame.quit()

my_game=AirForceGame(500,500)

my_game.startGame()

exit(0) 