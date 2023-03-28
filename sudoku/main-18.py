import random
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QStyleFactory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('main.ui')

        self.game = [[None for i in range(9)] for j in range(9)] # araye lineEditHa

        #create table 
        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setAlignment(Qt.AlignCenter) # وسط چین کردن متن
                tb.setStyleSheet('font-size: 32px')
                tb.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
                self.game[i][j] = tb  #back-end
                self.ui.gridLayout_2.addWidget(tb, i, j) # i , j shomare satr va soton ast #front-end

        self.ui.show()
        self.ui.btn_newgame.clicked.connect(self.newGame)
        self.ui.btn_check.clicked.connect(self.checkGame)
        self.win = 1 
        self.ui.btn_darkmode.clicked.connect(self.darkmode)
#---------------------------------------------------------------------------------------------------------#
    def darkmode(self, dark_mode: bool):
        if dark_mode:
            qApp.setStyle(QStyleFactory.create('Fusion'))
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, Qt.white)
            palette.setColor(QPalette.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.white)
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, Qt.white)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, Qt.black)
            qApp.setPalette(palette)
        else:
            qApp.setStyle(QStyleFactory.create('Fusion'))
            qApp.setPalette(qApp.style().standardPalette())

#---------------------------------------------------------------------------------------------------------#
    def checkGame(self):

        self.win = 1

        #check rows
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() !='' :
                        self.game[row][i].setStyleSheet('font-size: 32px ; color:Green ; background-color : red ')
                        self.win = 0

        #check colums
        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() !='' :
                        self.game[i][col].setStyleSheet('font-size: 32px ; color:Green ; background-color : red ')
                        self.win = 0

        # check 3x3
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = set()
                for i in range(3):
                    for j in range(3):
                        SeDarSe = self.game[r+i][c+j].text()
                        if SeDarSe.isdigit():
                            if SeDarSe in nums:
                                self.game[r+i][c+j].setStyleSheet('font-size: 32px; color:Green; background-color : red ')
                                self.win = 0
                            else:
                                nums.add(SeDarSe)


        if self.win == 1:
            msgBox = QMessageBox()
            msgBox.setText('You are Winner!')
            msgBox.exec()

#---------------------------------------------------------------------------------------------------------#
    def newGame(self):
        # clear table
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')

        # read file
        try:
            r = random.randint(1,6)
            file_path = f"data/s{r}.txt"
            f = open(file_path,'r')
        except: 
            msgBox = QMessageBox()
            msgBox.setText('Press New Game again Please')
            msgBox.exec()

        big_text = f.read()
        rows = big_text.split('\n')

        for i in range(9):
            numbers = rows[i].split(' ')
            for j in range(9):
                if numbers[j] != '0':
                    self.game[i][j].setStyleSheet('font-size: 32px;color:Green')
                    self.game[i][j].setText(numbers[j])
                else:
                    self.game[i][j].setStyleSheet('font-size: 32px;color:blue')
#---------------------------------------------------------------------------------------------------------#
app = QApplication([])
window = MainWindow()
app.exec()
