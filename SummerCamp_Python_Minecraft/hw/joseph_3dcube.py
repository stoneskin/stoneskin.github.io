from mcpi_e.minecraft import Minecraft

serverAddress="127.0.0.1" # my server
pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="NightShade9182" # change to your username
mc = Minecraft.create(serverAddress,pythonApiPort,playerName)

pos=mc.player.getTilePos()

x=pos.x
y=pos.y
z=pos.z
for c in range(0,4):
    for a in range(0,4):
        for b in range(0,4):
            if c==0:
                if b==1 or b==2:
                    if a==0 or a==3:
                        mc.setBlock(x+a,y+b,z+c,57)
                    else:
                        continue
                else:
                    mc.setBlock(x+a,y+b,z+c,57)
            elif c==1:
                if b==0 or b==3:
                    if a==0 or a==3:
                        mc.setBlock(x+a,y+b,z+c,57)
                    elif b==1 or b==2:
                        if a==1 or a==2:
                            mc.setBlock(x+a,y+b,z+c,0)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

            elif c==2:
                if b==0 or b==3:
                    if a==0 or a==3:
                        mc.setBlock(x+a,y+b,z+c,57)
                    elif b==1 or b==2:
                        if a==1 or a==2:
                            mc.setBlock(x+a,y+b,z+c,0)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

            elif c==3:
                if b==1 or b==2:
                    if a==0 or a==3:
                        mc.setBlock(x+a,y+b,z+c,57)
                    else:
                        continue
                else:
                    mc.setBlock(x+a,y+b,z+c,57)