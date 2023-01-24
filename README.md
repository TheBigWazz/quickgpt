# quickgpt
A simple Python window to display ChatGPT, created with ChatGPT and no Python experience.

![Untitled](https://user-images.githubusercontent.com/80355486/214434526-6f278aea-36c3-406f-9e12-e67825714250.png)


#### Notes:
- Copy Code button now works! ~~I can't figure out how to give the website JS permission to write to the clipboard, so for now the 'Copy Code' buttons do not work, you'll need to manually highlight and right click text.~~

- Padding is wonky with QtWebEngine, some elements may be more cozy than others. 

- Reload button will reload the current page, Home will reload the inital "https://chat.openai.com/chat"

- The Google Security Key 2fa method is not supported with QtWebEngine, if your OpenAI login is tied to a Google account with this method as the default, you'll need to wait for it to timeout on the login screen to select another method; or set a new default 2fa method in the settings of that Google Account.

## Dependencies

### Python: ### 

#### Windows ####
 
https://www.python.org/downloads/  
**Make sure to check the box that adds Python to your PATH before installing*  

#### Debian ####

```sudo apt install python3```  
___

### PyQt5: ###  
```pip install PyQt5```

### PyQtWebEngine: ###  
```pip install PyQtWebEngine```  
Or download from here: https://pypi.org/project/PyQtWebEngine/#files  
Install with
```py -m pip install ./downloads/(File you downloaded)```

### QtCore ###
```pip install QtCore```

### QtWidgets ###
```pip install QtWidgets```

### QtGui ###
```pip install QtGui```

### PyInstaller: ###  
```pip install pyinstaller```


# Creating Executable 
Navigate to where quickgpt.py is saved and run this command:  
```pyinstaller -w -F -i=chatgpt.ico --add-data="chatgpt.ico;img" quickgpt.py```
  
> -w: Hides the Python console when running the application

> -F: Packages everything needed for the application to run into a single executable. The file is output in the 'dist' folder created in the same location as the script.

> -i: Sets the program icon

> --add-data: Adds the .ico to the \img\ output for the .exe

View more information about PyInstaller to further customize the executable: https://pyinstaller.org/en/stable/

# Executable Shortcuts
### Windows
- Right click the EXE created and send a shortcut to the desktop. 
- If you'd like, right click the shortcut and rename it.

At this point you can pin the shortcut to the taskbar or start menu, or leave it on the desktop.

### Debian
- Update the quickgpt.desktop file with the correct paths to the executable and icon. Lines 4 and 5:
```
[Desktop Entry]
Type=Application
Name=quickgpt
Exec=/(Location to executable)
Icon=/(Location to)/chatgpt.ico
```

- Move quickgpt.desktop to this location:
> ~/.local/share/applications

At this point you should be able to find 'quickgpt' with your preferred application launcher and move it various places depending on your Desktop Enviorment. 
