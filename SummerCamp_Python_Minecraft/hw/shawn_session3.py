from mcpi_e.minecraft import Minecraft
from mcpi_e import block
import time

serverAddress =  "localhost" # change to your minecraft server
playerName = "Epicbro90"
pythonApiPort = 4711

mc = Minecraft.create(serverAddress,pythonApiPort,playerName)

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
def pixel_art():
    x = pos.x
    y = pos.y
    z = pos.z
    print("Making pixel art...")
    #Create a double List with a pixel arts
    pixelArtList  = [
                    [0,0,1,0,0],
                    [0,1,1,1,0],
                    [1,1,1,1,1],
                    [0,1,1,1,0],
                    [0,0,1,0,0]
                    ]

    x=x+1  #shift x by 1
    for row in reversed(pixelArtList): # we need reverse the list
        for color in row:
            mc.setBlock(x,y,z,35,color)
            z=z+1 #add 1 to z so it put next as a row
        z=pos.z #reset the z to starting z
        y+=1
    print("Pixel art created!")
    mc.postToChat("Pixel art created")
def house():
    print("Creating house...")
    pos = mc.player.getPos()
    import random
    randomlist = [1,2,3]
    x = pos.x
    y = pos.y
    z = pos.z
    for e in range(0,6):
       id = 4
       for f in range(0,6):
          mc.setBlock(x+f,y,z,id)
          if random.choice(randomlist) == 1:
             id = 48
             print("List randomization worked")
             randomlist.append("1")
          else:
             id = 4
       z = z + 1
       x = pos.x
    for o in range(0,4):
       x = pos.x
       z = pos.z
       print("o=",o)
       y = y + 1
       for w in range (0,2):
          print("w=",w)
          for i in range(0,6):
             print("i=",i)
             if i == 0 or i == 5:
                id = 17
             elif i == 2 or i == 3:
                if w == 0:
                   id = 20
                else:
                   id = 0
             else:
                id = 5
             if id != 0:
                mc.setBlock(x+i,y,z,id)
          for i in range(0,6):
             print("i=",i)
             if w == 1:
                x = pos.x+5
                z = pos.z
             if i == 0 or i == 5:
                id = 17
             elif i == 2 or i == 3:
                id = 20
             else:
                id = 5
             mc.setBlock(x,y,z+i,id)
          z = z+5
       mc.setBlock(pos.x+1,pos.y+1,pos.z+1,58)
       mc.setBlock(pos.x+1,pos.y+2,pos.z+1,50)
       mc.setBlock(pos.x+4,pos.y+1,pos.z+4,61)
       mc.setBlock(pos.x+1,pos.y+2,pos.z+4,50)
       mc.setBlock(pos.x+3,pos.y+1,pos.z+1,171)
       mc.setBlock(pos.x+4,pos.y+1,pos.z+1,171)
    x = pos.x-1
    y = pos.y+5
    z = pos.z-1
    for e in range(0,8):
       id = 98
       for f in range(0,8):
          mc.setBlock(x+f,y,z,id)
       z = z + 1
    mc.postToChat("A beautiful house has just been made!")
def cube():
    print("Creating cube...")
    x = pos.x
    y = pos.y
    z = pos.z
    cube = [[[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 0, 0, 57], [0, 0, 0, 0], [0, 0, 0, 0], [57, 0, 0, 57]],
        [[57, 57, 57, 57], [57, 0, 0, 57], [57, 0, 0, 57], [57, 57, 57, 57]]]
    startingX = x
    startingY = y
    for depth in reversed(cube):
        x=x+1
        y=startingY
        for column in depth:
            for row in column:
                mc.setBlock(x,y,z,row)
                z=z+1
            y+=1
            z=pos.z
    x=pos.x
    y=pos.y
    z=pos.z
    mc.postToChat("A diamond cube was just created!")
choice = input("What would you like to make? Pixel Art (1) House (2) or a Cube? (3)")
if int(choice) == 1:
    pixel_art()
if int(choice) == 2:
    house()
if int(choice) == 3:
    cube()