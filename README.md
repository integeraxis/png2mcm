# png2mcm
<img width="100%" alt="image" src="https://github.com/user-attachments/assets/c83f8744-5036-4cc3-907f-3b8266764012" />

## How to install:
### Windows and Linux:
Go to the releases tab or click [here](https://github.com/integeraxis/png2mcm/releases/latest) and install the version matching your OS.

### MacOS:
- Download python: https://www.python.org/downloads/
- Follow the instructions from the python installer.
- Go back to this page and press the green code button and click "download zip"
- unzip the .zip file.
- Open the terminal and type: ```python3 --version```. If it says something like: ```Python 3.13.2``` (the version number doesn't matter), Then you're good.
- In the same terminal type: ```python3 -m pip install --upgrade Pillow```.
- Type ```cd ~/Downloads/png2mcm-main/png2mcm-main``` to go to the unzipped folder or wherever else you unzipped the folder. To check if you are in the right folder: type ```ls```. If you see main.py, converter.py, utils.py, and some other stuff, then it's correct.
- Last step! Type python3 main.py in the terminal and the program should open. To learn how to use the program, see below:

## How to use:
- It's easiest to edit an already existing font:
- To download one of the betaflight fonts, go to: https://github.com/betaflight/betaflight-configurator/tree/master/resources/osd/1 and click on .png file you want.
- Click the download button:
<img width="1683" height="503" alt="image" src="https://github.com/user-attachments/assets/84f337f6-bae9-434d-aba4-bd7107379681" />

### Editing:
- Open the .png file in a image editor of your choice and edit the font.
- If you don't know any image editor these are some good ones: Microsoft paint, [Pixelorama](https://orama-interactive.itch.io/pixelorama) (online or download), [Piskel](https://www.piskelapp.com/p/create/sprite/) (online editor), 
- Warning: The only colors you can use are gray(#7F7F7F), black(#000000) and white(#FFFFFF) (Do not change the red lines!)

### Exporting:
- Open png2mcm and click "Open a Betaflight font .png" and open the font you just made.
- It should say it converted the file correctly. You can find your .mcm font file in the same folder as the .png file.
- Open Betaflight configurator and connect you quad.
- Go to the OSD tab and click on "font manager".
- Click "Open font file" and open the .mcm file you generated.
- Now click "Upload font", wait for it to upload and you're done!
