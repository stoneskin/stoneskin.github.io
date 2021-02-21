# example of snake game
import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))

keep_going = True

while keep_going:  # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    # blit() method will load the image from hard disk.  position will be (x,y)
    #screen.blit(pic, (100, 100))

    pygame.display.update()

pygame.quit()  # Exit