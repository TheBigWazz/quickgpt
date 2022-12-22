import sys
from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSlot
from PyQt5.QtGui import QClipboard
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton

# Create the QApplication 
app = QApplication(sys.argv)

# Set the Qt::AA_UseHighDpiPixmaps attribute
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

# Set the Qt::AA_UseStyleSheetPropagationInWidgetStyles attribute
QApplication.setAttribute(Qt.AA_UseStyleSheetPropagationInWidgetStyles, True)

# Set the style sheet to a dark theme
app.setStyleSheet("""
    QWidget {
        background-color: #333333;
        color: white;
    }
    QPushButton {
        background-color: #555555;
        color: white;
    }
""")

# console
app.setApplicationName("ChatGPT")
app.setApplicationDisplayName("ChatGPT")
app.setQuitOnLastWindowClosed(True)

# Create a QWebEngineView and set the URL to load
view = QWebEngineView()
view.setUrl(QUrl("https://chat.openai.com/chat"))

# Create a QPushButton to go back to the original webpage
back_button = QPushButton("Refresh")

# Set the style sheet for the button
back_button.setStyleSheet("""
    QPushButton {
        background-color: #555555;
        color: white;
        font-size: 13px;
        font-weight: bold;
        border: 2px solid #333333;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #777777;
    }
""")

# Create a QPushButton to go back to the original webpage
back_button = QPushButton("Refresh")

# Set the style sheet for the button
back_button.setStyleSheet("""
    QPushButton {
        background-color: #555555;
        color: white;
        font-size: 13px;
        font-weight: bold;
        border: 2px solid #333333;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #777777;
    }
""")

# Define a function to go back to the original webpage
def go_back():
    view.setUrl(QUrl("https://chat.openai.com/chat"))

# Connect the button's clicked signal to the go_back function
back_button.clicked.connect(go_back)

# Create a vertical layout and add the view and button to it
layout = QVBoxLayout()
layout.addWidget(back_button)
layout.addWidget(view)

# Create a window and set the layout as its central layout
window = QWidget()
window.setWindowTitle("ChatGPT")
window.setLayout(layout)
window.resize(1300, 800)  # Set the size of the window
window.show()

# Run the application loop
sys.exit(app.exec_())
