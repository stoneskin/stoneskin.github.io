import mcpi_e.minecraft as minecraft
import mcpi_e.block as block
from math import *

address="127.0.0.1" # change to address of your minecraft server
name ="CozmicGaming01"
mc = minecraft.Minecraft.create(address,4711,name)
pos=mc.player.getTilePos()

(x, y, z) = pos = mc.player.getTilePos()

pixelArtList  = [
         [2, 2, 2, 2, 15, 15, 15, 15, 2, 2, 2, 2, 2, 2, 2, 2, 2, 15, 2, 2, 2],
         [2, 2, 2, 15, 1, 1, 1, 1, 15, 2, 2, 2, 2, 2, 2, 2, 15, 14, 15, 2, 2],
         [2, 2, 15, 1, 1, 1, 1, 1, 1, 15, 2, 2, 2, 2, 2, 2, 15, 14, 14, 15, 2],
         [2, 2, 15, 1, 1, 1, 1, 1, 1, 15, 2, 2, 2, 2, 2, 2, 15, 14, 14, 15, 2],
         [2, 15, 1, 1, 1, 1, 1, 1, 1, 1, 15, 2, 2, 2, 2, 15, 14, 14, 14, 14, 15],
         [15, 1, 1, 1, 1, 0, 15, 1, 1, 1, 15, 2, 2, 2, 2, 15, 14, 14, 4, 14, 15],
         [15, 1, 1, 1, 1, 15, 15, 1, 1, 1, 1, 15, 2, 2, 2, 15, 14, 4, 4, 14, 15],
         [15, 1, 1, 1, 1, 15, 15, 1, 1, 1, 1, 15, 2, 2, 2, 2, 15, 4, 15, 15, 2],
         [2, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15, 2, 2, 2, 15, 1, 15, 2, 2],
         [2, 2, 15, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15, 2, 15, 1, 1, 15, 2, 2],
         [2, 2, 2, 2, 15, 15, 15, 1, 1, 15, 1, 1, 1, 15, 15, 1, 1, 15, 2, 2, 2],
         [2, 2, 2, 2, 2, 15, 4, 4, 15, 1, 1, 1, 1, 1, 15, 1, 1, 15, 2, 2, 2],
         [2, 2, 2, 2, 2, 15, 4, 4, 4, 15, 15, 1, 1, 1, 15, 1, 15, 2, 2, 2, 2],
         [2, 2, 2, 2, 15, 0, 15, 4, 4, 4, 1, 1, 1, 1, 15, 15, 2, 2, 2, 2, 2],
         [2, 2, 2, 2, 2, 15, 15, 15, 4, 4, 1, 1, 1, 15, 15, 2, 2, 2, 2, 2, 2],
         [2, 2, 2, 2, 2, 2, 2, 2, 15, 15, 15, 1, 15, 15, 2, 2, 2, 2, 2, 2, 2],
         [2, 2, 2, 2, 2, 2, 2, 2, 2, 15, 0, 1, 0, 15, 2, 2, 2, 2, 2, 2, 2],
         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 15, 15, 15, 15, 2, 2, 2, 2, 2, 2, 2],
         ]

x += 1  #shift x by 1
for row in reversed(pixelArtList ):
    for color in row:
        mc.setBlock(x, y, z, 35, color)
        if color == 2:
            mc.setBlock(x, y, z, 0)
        z = z + 1
    z = pos.z
    y += 1