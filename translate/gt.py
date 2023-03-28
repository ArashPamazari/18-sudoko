from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from googletrans import Translator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('gt.ui', None)
        self.ui.show()
        
        self.ui.translate.clicked.connect(self.translate)
        self.ui.change.clicked.connect(self.Change_language)   

    def translate(self):
        if self.ui.input_text.text()!='':
            translator = Translator()
            if self.ui.change.text()=='En -> Fa':
                translate_text = translator.translate(self.ui.input_text.text(), src='en', dest='fa')
            else:
                translate_text = translator.translate(self.ui.input_text.text(), src='fa', dest='en')
            self.ui.output.setText(translate_text.text)
        else:
            self.ui.output.setText('')
            msgBox = QMessageBox()
            msgBox.setText('There is nothing to translate.')
            msgBox.exec()

    def Change_language(self):
        if self.ui.change.text()=='En -> Fa':
            self.ui.change.setText('Fa -> En')
        else:
            self.ui.change.setText('En -> Fa')

app = QApplication([])
window = MainWindow()
app.exec()