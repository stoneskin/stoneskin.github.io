# Session 1: Get Started With Python and Minecraft

## Session 1.1 Setup your Python-minecraft programming Environment

### 1. What python could do with Minecraft game

* A different way to play Minecraft
* Let Python do the boring tasks for you
* Change the Minecraft world by put or clear blocks
* Find the location resource underground
* Build small game in the Minecraft

### 2. Setup Minecraft Client and Server

#### 2.1 Install Minecraft Java edtion Client

Go to minecraft website download the Java Edition

* [Link to download Minecraft java edition](https://www.minecraft.net/en-us/download/)

#### 2.2 Setup Minecraft Server

* Install Minecraft Server:
  * Download Java and install it. ([link to download Java](https://java.com/en/download/))
  * Download the [spigot minecraft server](https://stoneskin.github.io/python-minecraft/documents/1_SetUpMineCraftServer/minecraft_spigot-1.15.2.zip) and unzip it.
  * Run it by double click the "StartMineCraftServer.bat" file.
* To understand how it works
  - <a target="_blank" href="https://stoneskin.github.io/python-minecraft/documents/1_SetUpMineCraftServer/1.1_HowToSetUpMineCraftServer.html">How to setup a minecraft server (spigot)</a>
  
  - <a target="_blank" href="https://stoneskin.github.io/python-minecraft/documents/1_SetUpMineCraftServer/1.2_HowToEnablePythonForMineCraftServer.html">How to enable Python on the Minecraft server by installing the RaspberryJuice plugin</a>
* Connect to your server
  * <a target="_blank" href="https://stoneskin.github.io/python-minecraft/documents/1_SetUpMineCraftServer/1.3_HowToConnectToYouMinecraftServer.html">How to connect to your server</a>

### 3. Install Python and mcpi-e Modules
* **Install Python**
  * Go to <a target="_blank" href="https://www.python.org/downloads/">Python download page</a>, download and install **Python 3.8** and up
  * <a href="https://onedrive.live.com/?authkey=%21ABw%2DLzmG9zyRWFA&cid=61E2F373B0D0BEF9&id=61E2F373B0D0BEF9%2150723&parId=61E2F373B0D0BEF9%2150531&o=OneUp" target="_blank">How to Install Python</a>
 
* **Install Python-Minecraft API module `mcpi-e`** 
  * Window

    >*input below script in the command line. (from start, search "cmd")*

    - use `pip3`
    
    ```bash
    pip3 install mcpi-e
    ```

    - or use `py` or `python -m`
    
    ```bash
    py -m pip install mcpi-e
    ```
  * Linux / MacOS
    - sudo pip3 install mcpi-e

* **Install a Python  Editor**
 
  - Python IDLE
    - [IDLE](https://en.wikipedia.org/wiki/IDLE) is commine with Python, Open it by in Start->Search, Input "IDLE"
    - For how to [use IDLE](https://realpython.com/python-idle/)
    
  - PyCharm
    - **PyCharm Edu** is a python editor help you learn Python
    - Click to download [pyCharm Edu](https://www.jetbrains.com/edu-products/download)

  - VsCode
    - **VsCode** is a editor for many different programming langurage.
    - Click to download [VsCode](https://code.visualstudio.com/)
    - [How to install VsCode for python](https://onedrive.live.com/?authkey=%21ABw%2DLzmG9zyRWFA&cid=61E2F373B0D0BEF9&id=61E2F373B0D0BEF9%2150724&parId=61E2F373B0D0BEF9%2150531&o=OneUp)

### 4. Run your first python code in Minecraft world
Create a Python project folder, Download and save the sample1.py file to  your python project folder
   >[sample1.py](https://stoneskin.github.io/python-minecraft/0.1-Sample1.py)

```python
from mcpi_e.minecraft import Minecraft

serverAddress="127.0.0.1" # change to your minecraft server
pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="stoneskin" # change to your username

mc = Minecraft.create(serverAddress,pythonApiPort,playerName)
pos = mc.player.getPos()

print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))
```

Use your favorite python editor to open the sample1.py file.
When you install python, it come with a python editor call IDLE.