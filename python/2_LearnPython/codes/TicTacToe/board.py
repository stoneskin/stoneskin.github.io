import pygame

class Board:
    img:any=pygame.image.load("board.jpg")
    def __init__(self,x:float,y:float,width:int,height:int) -> None:
        self.pos:list[float]=[x,y]
        self.img=pygame.transform.scale(self.img, (width, height))
        
    def display(self,screen) ->None:
        screen.blit(self.img, self.pos)