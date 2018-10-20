#!/usr/bin/env python
"""
Bookdoctor GUI
"""
import os
import sys
from cure import *
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon

class DoctorWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.center()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('cross.png'))
    
        self.show()

    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoctorWindow()
    sys.exit(app.exec_())

