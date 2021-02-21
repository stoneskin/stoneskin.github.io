import pygame  

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Happy Face")
keep_going = True
pic = pygame.image.load("happyface.png")
color_key = pic.get_at((0,0))  
pic.set_colorkey(color_key) #Set the transparent colorkey
pic_x = 0
pic_y = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
timer = pygame.time.Clock()
speed_x = 5
speed_y = 5

pic_w = pic.get_width()
pic_h = pic.get_height()

points = 0
lives = 5
font = pygame.font.SysFont("Times", 24)


# Game loop
while keep_going:    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keep_going = False
        
                
    pic_x += speed_x
    pic_y += speed_y
    
    if pic_x <= 0 or (pic_x + pic_w) >= 800:
        speed_x = -speed_x
        print("pic_x+pic_w>800: "+str(pic_x + pic_w))
    if pic_y <= 0 or (pic_y + pic_h) >= 600:
        speed_y = -speed_y
        print("pic_y+pic_h>600: "+str(pic_y + pic_h))
        
   
    
    screen.fill(BLACK)    
    screen.blit(pic, (pic_x, pic_y))  #draw the picture on the screen
    
       
    pygame.display.update()
    timer.tick(60)  # howmany frame every sec, https://www.pygame.org/docs/ref/time.html

# Exit    
pygame.quit() 
