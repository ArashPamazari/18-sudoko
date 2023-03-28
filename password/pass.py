import string
import secrets
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('pass.ui', None)
        self.ui.show()

        self.ui.generate_btn.clicked.connect(self.generate)

    def generate(self):
        if self.ui.btn_Check.isChecked():
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for i in range(12))
        self.ui.lineEdit.setText(password)

app = QApplication([])
window = MainWindow()
app.exec()