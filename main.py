import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl, pyqtSlot, QObject, pyqtSignal, QSize
from PyQt5.QtWebChannel import QWebChannel

class Communicator(QObject):
    close_window = pyqtSignal()
    terminate_app = pyqtSignal()

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        # Set the mobile phone ratio (e.g., 9:16)
        self.setFixedSize(400, 500)
        
        # Position the window in the lower right corner above the taskbar
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = screen_geometry.width() - self.width() - 10  # 10 pixels margin from the right edge
        y = screen_geometry.height() - self.height() - 10  # 10 pixels margin from the bottom edge
        self.move(x, y)

        # Create a QWebEngineView to display the webpage
        self.browser = QWebEngineView(self)
        self.browser.loadFinished.connect(self.adjustSizeToContent)

        # Create a communicator object
        self.communicator = Communicator()
        self.communicator.close_window.connect(self.close)  # Connect the signal to the close method
        self.communicator.terminate_app.connect(self.terminate)  # Connect the signal to the terminate method

        # Set up the web channel
        channel = QWebChannel(self.browser.page())
        channel.registerObject("pyqt", self.communicator)  # Register the communicator object
        self.browser.page().setWebChannel(channel)  # Set the web channel for the page

        # Load the local HTML file
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
        html_file_path = os.path.join(current_dir, "index.html")  # Path to the HTML file
        # self.browser.setUrl(QUrl.fromLocalFile(html_file_path))  # Use QUrl to load the local file
        self.browser.setUrl(QUrl("http://localhost:8080"))  # Use QUrl here
        self.setCentralWidget(self.browser)

        # Show the window
        self.show()

    @pyqtSlot()
    def close(self):
        print("Close signal received")  # Debug statement
        super().close()  # Close the window

    @pyqtSlot()
    def terminate(self):
        print("Terminate signal received")  # Debug statement
        QApplication.quit()  # Terminate the application

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()  # Close the window when Esc is pressed

    @pyqtSlot()
    def adjustSizeToContent(self):
        self.browser.page().runJavaScript("document.documentElement.scrollWidth", self.setWidth)
        self.browser.page().runJavaScript("document.documentElement.scrollHeight", self.setHeight)

    def setWidth(self, width):
        self.setFixedWidth(width)  # Remove padding to avoid scrollbars

    def setHeight(self, height):
        self.setFixedHeight(height)  # Remove padding to avoid scrollbars

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverlayWindow()
    sys.exit(app.exec_())