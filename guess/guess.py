from random import randint
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('guess.ui', None)
        self.ui.show()

        self.randomNumber = randint(1, 999)
        
        self.ui.btn_check.clicked.connect(self.check)
        self.ui.btn_reset.clicked.connect(self.Reset)

    def Reset(self):
        self.randomNumber = randint(1, 999)
        self.ui.guide_label.setText('')
        self.ui.lineEdit.setText('')


    def check(self):
        userinput = self.ui.lineEdit.text()
        if userinput!='':
            
            if int(userinput)==self.randomNumber:
                self.ui.guide_label.setText('You Won!')
            elif int(userinput)>self.randomNumber:
                self.ui.guide_label.setText('Go Down')
            elif int(userinput)<self.randomNumber:
                self.ui.guide_label.setText('Go UP')
            else:
                self.ui.guide_label.setText('Show!')
        else:
            self.ui.guide_label.setText('')




app = QApplication([])
window = MainWindow()
app.exec()