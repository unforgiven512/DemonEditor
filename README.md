# <img src="app/ui/icons/hicolor/96x96/apps/demon-editor.png" width="32" /> DemonEditor

## Enigma2 channel and satellites list editor for macOS (experimental).
This version is only for users those who wish to try running this program on **macOS**.                                
The functionality and performance of this version may be very different from the main version!                                                     
**Not all features are supported and tested!**    

#### Keyboard shortcuts:                                                                                                                                                                                            
* **&#8984; + X** - only in bouquet list.
* **&#8984; + C** - only in services list.                                                                                                                                                    
Clipboard is **"rubber"**. There is an accumulation before the insertion!                                                              
* **&#8984; + E** - edit. 
* **&#8984; + R, F2** - rename.
* **&#8984; + S, T** in Satellites edit tool for create satellite or transponder.
* **&#8984; + L** - parental lock.
* **&#8984; + H** - hide/skip.                                                                                                                                                                                                 
* **&#8984; + P** - start play IPTV or other stream in the bouquet list.
* **&#8984; + Z** - switch(**zap**) the channel(works when the HTTP API is enabled, Enigma2 only).                         
* **&#8984; + W** - switch to the channel and watch in the program.
* **&#8984; + Up/Down** - move selected items in the list. 
* **&#8984; + O** - (re)load user data from current dir. 
* **&#8984; + D** - load data from receiver. 
* **&#8984; + U/B** - upload data/bouquets to receiver.
* **&#8984; + F** - show/hide search bar.
* **&#8679; + &#8984; + F** - show/hide filter bar.
* **Left/Right** - remove selection.

### Minimum requirements:
Python >= **3.5**, GTK+ >= **3.16**, pygobject3, adwaita-icon-theme, python3-requests.                                  
#### Installation:                                                                             
```brew install python3 gtk+3 pygobject3 adwaita-icon-theme```                                                                  
```pip3 install requests```                                                                                                                                                                                          
#### Optional:                                                                                                          
```brew install wget imagemagick```                                                                                                                                                                                                                                                                                                      
```pip3 install pyobjc```                                                                                                
#### Launching:                                                                                                                                                                                                                     
To start the program, just download the archive, unpack and run it from the terminal with the command: ```./start.py``` 

### Building standalone application:                                                                                     
Install [PyInstaller](https://www.pyinstaller.org/) with the command from the terminal:                                                                    
```pip3 install pyinstaller```                                                                                          
and in th root dir run command:                                                                                         
```pyinstaller DemonEditor.spec``` 
                                                                                                                                              
Users of the **64-bit version of the OS** can download a ready-made package from [here](https://github.com/DYefremov/DemonEditor/raw/experimental-mac/dist/DemonEditor.app.zip).                                     
Just unpack and run. Recommended copy the bundle to the **Application** directory.                                      
Perhaps in the security settings it will be necessary to allow the launch of this application!

**Note. The package may not contain all the latest changes!**                                                            
                                                                       
                                                                                                                                                                                                                                            
