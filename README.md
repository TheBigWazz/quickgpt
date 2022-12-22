# quickgpt
A simple Python window to display ChatGPT, created with ChatGPT and no Python experience.

![chatgpt](https://user-images.githubusercontent.com/80355486/209186458-5966e6a4-7977-4ddb-9764-8d18660fb6b3.png)

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
