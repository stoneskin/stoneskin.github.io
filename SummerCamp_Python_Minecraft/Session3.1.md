# Session 3: Python Function, Pixel Art and Minecraft Server

## Session 3.1 Python use functions & Make Pixel Art

### 1. Use function to organize your scripts

#### - [Mission-3.1] Define your first Python function

Below is example of a function, for more info, please check [python function](https://www.w3schools.com/python/python_functions.asp)
![definefunction](./define_function.jpg)

please try below function:

```python

from mcpi_e.minecraft import Minecraft
serverAddress="server-address" # change to your Minecraft server
playerName ="yourname"
pythonApiPort=4711

mc=Minecraft.create(serverAddress,pythonApiPort,playerName)

#define a function
def SayHello():
    mc.postToChat("hello minecraft!")

# call the function
SayHello()
```

#### - [Mission-3.2] Define a Python function with arguments

Function could take parameters, for example, you could pass the name to the `SayHello` function:
the name call argument.

```python
def SayHello(name);
    mc.postToChat("*************************")
    mc.postToChat(" Hello "+name+"!")
    mc.postToChat("*************************")

SayHello("Smith")
```

And you could define a function to take more arguments,
and you could call another function in you function.

```python
import time

#define a function
def makeMelon(shiftX, shiftY, shiftZ):
    pos = mc.player.getPos()
    x = pos.x+shiftX
    y = pos.y+shiftY
    z = pos.z+shiftZ
    mc.setBlock(x, y, z, 103)
    time.sleep(10)

def makeMelonCross()
    #call your function by change the number little bit
    makeMelon(0, 1, 0)
    makeMelon(0, 2, 0)
    makeMelon(0, 3, 0)
    makeMelon(1, 3, 0)
    makeMelon(-1, 3, 0)
    makeMelon(2, 3, 0)
    makeMelon(-2, 3, 0)
    makeMelon(0, 4, 0)
    makeMelon(0, 5 ,0)

makeMelonCross()

```

#### [homework] [Mission-3.3] Refactor: Improve the function in Mission3.2

Many time we don't want hardcoded to 103 for melon only,
change the function to MakeBlock and MakeCrossWithBock,  so you could pass any blockId to function
`makeCrossWithBlock(blockId)`


#### [Mission-3.4] return value in the function

many time we need function return values, for example you call getTilePos()

```python
pos = mc.player.getTilePos()
```

Below is a example of how to define a function return a result.

```python
def my_function(x):
  return 5 * x

result=my_function(3)
print(result)

print(my_function(5))

```

#### [Mission-3.5] Define function in a different file and import as package

Some time we defined a function, we want it could be reused in many different script.
for example, almost all your code will need get the Minecraft api object `mc`, let's put it in separate files cal mc.py

So we will save  below python code a file call `createmc.py`

```python
#save below code as createMc.py
from mcpi_e.minecraft import Minecraft

def createMc():
    serverAddress="server-address" # change to your minecraft server
    playerName ="yourname"
    pythonApiPort=4711

    mc=Minecraft.create(serverAddress,pythonApiPort,playerName)
    return mc  #return the result back to caller

```

Then create another python file example, testMc.py, save in same folder as createMc.py

```python
# another py file, same folder as createMc.py
from createmc import *

mc=createMc()

mc.postToChat("Your Minecraft api created!")

```

#### [Challenge][Mission-3.6] What happen if two function call each other or call itself

It's call recursion, similar like while loop, it need a break point to avoid infinite loop.

```python

from createmc import *

mc=createMc()
pos = mc.player.getTilePos()
high=10
blockId=103

def BuildTower(count=0):
    if(count>high):
        return #this is very important, otherwise the code will never stop running.
    mc.setBlock(pos.x+1,pos.y+count,pos.z,blockId)
    BuildTower(count+1)

BuildTower()

```

Your Challenge,  write two functions, make them call each other. Make sure give a condition you code could stop.  Try it in your own computer.

if your script didn't stop, close the windows or use `Ctrl + C` force to close the window.

### 2. Pixel Art with blocks
