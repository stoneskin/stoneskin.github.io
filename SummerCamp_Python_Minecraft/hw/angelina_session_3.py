from createMc import *



mc=createMc()
pos = mc.player.getTilePos()
x,y,z=pos=mc.player.getTilePos()
pixelArtList  = [
         [13,13,13,13,13],
         [13,15,13,15,13],
         [13,13,15,13,13],
         [13,15,15,15,13],
         [13,15,13,15,13],
         [13,13,13,13,13]
         ]

x=x+1  #shift x by 1
for row in reversed(pixelArtList ): # we need reverse the list
    for color in row:
        mc.setBlock(x,y,z,35,color)
        z=z+1 #add 1 to z so it put next as a row
    z=pos.z #reset the z to starting z
    y+=1