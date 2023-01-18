from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
 
# creating main window class
class MainWindow(QMainWindow):
 
    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
 
        # creating a QWebEngineView
        self.browser = QWebEngineView()
 
        # setting default browser url as google
        self.browser.setUrl(QUrl("https://chat.openai.com/chat"))
 
        # set this browser as central widget or main window
        self.setCentralWidget(self.browser)
 
        # set clipboard permission
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
        
        # creating a status bar object
        self.status = QStatusBar()
 
        # adding status bar to the main window
        self.setStatusBar(self.status)
 
        # creating QToolBar for navigation
        navtb = QToolBar("Navigation")
        navtb.setAutoFillBackground(True);
        navtb.setStyleSheet("QToolBar { background: #202123; spacing: 5px; border-width: 1; } ");
         
        # adding this tool bar to the main window
        self.addToolBar(navtb)
 
        # adding actions to the tool bar
        # creating a action for back
        back_btn = QAction("<", self)
        
        # setting status tip
        back_btn.setStatusTip("Back to previous page")
 
        # adding action to the back button
        # making browser go back
        back_btn.triggered.connect(self.browser.back)
 
        # adding this action to tool bar
        navtb.addAction(back_btn)
        
        # similarly for forward action
        next_btn = QAction(">", self)
        next_btn.setStatusTip("Forward to next page")
        
        # adding action to the next button
        # making browser go forward
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)
 
        # adding a separator in the tool bar
        navtb.addSeparator()
 
        # similarly for reload action
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
 
        # adding action to the reload button
        # making browser to reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
 
        # similarly for home action
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
 
        # showing all the components
        self.show()
 
    # method called by the home action
    def navigate_home(self):
 
        # open the homepage
        self.browser.setUrl(QUrl("https://chat.openai.com/chat"))
 
# creating a pyQt5 application
app = QApplication(sys.argv)

app.setStyleSheet("""
    QWidget {
        color: white;
        background: #202123;
    }
""")
 
# setting name to the application
app.setApplicationName("ChatGPT")
 
# creating a main window object
window = MainWindow()
window.resize(1300, 800)  # Set the size of the window

# Get the screen resolution
screen = QDesktopWidget().screenGeometry()

# Set the window in the center of the screen
window.move(int((screen.width() - window.width()) / 2), int((screen.height() - window.height()) / 2))
 
# loop
app.exec_()
