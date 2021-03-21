from checker import CheckerO,CheckerX
import pygame

class Board:
    img:any=pygame.image.load("board.jpg")
    def __init__(self,x:float,y:float,width:int,height:int) -> None:
        self.pos:list[float]=[x,y]
        self.img=pygame.transform.scale(self.img, (width, height))
        self.checker1=CheckerO(100,100)
        self.checker2=CheckerX(300,100)
        
    def display(self,screen) ->None:
        screen.blit(self.img, self.pos)
        self.checker1.display(screen)
        self.checker2.display(screen)
    