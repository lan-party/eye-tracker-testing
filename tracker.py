import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QColor, QBitmap, QCursor
from PyQt5.QtCore import Qt, QTimer
import pyautogui

app = QApplication(sys.argv)


window = QMainWindow()

window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_TranslucentBackground)

label = QLabel(window)
label.setPixmap(QPixmap('C:\\Users\\dell\\Pictures\\cursor.png'))

def update_position():
    mouse_x, mouse_y = pyautogui.position()
    label.setGeometry(mouse_x-125, mouse_y-125, label.pixmap().width(), label.pixmap().height())
    label.update()
    window.update()
    app.processEvents()

window.showFullScreen()
window.activateWindow()

timer = QTimer(app)
timer.setInterval(16)
timer.timeout.connect(update_position)
timer.start()

sys.exit(app.exec_())
