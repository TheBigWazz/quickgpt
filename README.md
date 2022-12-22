# quickgpt
A simple Python window to display ChatGPT, created with ChatGPT and no Python experience.

![image](https://user-images.githubusercontent.com/80355486/209231564-e4946280-855c-4b04-b75d-22dd5c4935f6.png)

#### Notes:
- I can't figure out how to give the website JS permission to write to the clipboard, so for now the 'Copy Code' buttons do not work, you'll need to manually highlight and right click text.

- Padding is wonky with QtWebEngine, some elements may be more cozy than others. 

- Refresh button at the top will reload the page if it gets stuck or if the ChatGPT session encounters errors.

- The Google Security Key 2fa method is not supported with QtWebEngine, if your OpenAI login is tied to a Google account with this method as the default, you'll need to wait for it to timeout on the login screen to select another method; or set a new default 2fa method in the settings of that Google Account.

## Dependencies

**PyQt5:**  
```pip install PyQt5```

**PyQtWebEngine:**  
```pip install PyQtWebEngine```  
Or download from here: https://pypi.org/project/PyQtWebEngine/#files  
Install with
```py -m pip install ./downloads/(File you downloaded)```

**PyInstaller:**  
```pip install pyinstaller```


# Creating Executable 
Navigate to where quickgpt.py is saved and run this command:  
```pyinstaller --windowed quickgpt.py -F```
  
> --windowed: Hides the Python console when running the application

> -F: Packages everything needed for the application to run into a single executable. The file is output in the 'dist' folder created in the same location as the script.

View more information about PyInstaller to further customize the executable: https://pyinstaller.org/en/stable/

# Executable Shortcuts
### Windows
- Right click the EXE created and send a shortcut to the desktop. 
- If you'd like, right click the shortcut and set the icon to chatgpt.ico (provided)
- If you'd like, right click the shortcut and rename it.

Everything should be set at this point. 

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

Everything should be set at this point.
