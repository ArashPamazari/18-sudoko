from unit_converter.converter import converts
from unittest import result

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class Convertor(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('conver.ui', None)
        self.ui.show()

        
        self.ui.ConverterSubject_Box.currentTextChanged.connect(self.comboBox)
        self.ui.ConverterSubject_Box.addItems(['Mass','Length', 'DigitalVolume', 'Temperature'])

        self.ui.calculate.clicked.connect(self.calculate)

    def comboBox(self):
        self.ui.CurrentUnit_Box.clear()
        self.ui.ResultUnit_Box.clear()

        if self.ui.ConverterSubject_Box.currentText() == 'Mass':

            self.ui.CurrentUnit_Box.addItems(['g','kg','T','P'])
            self.ui.ResultUnit_Box.addItems(['kg','g','T','P'])

        elif self.ui.ConverterSubject_Box.currentText()=='Length':

            self.ui.CurrentUnit_Box.addItems(['mm','cm','m','km','in'])
            self.ui.ResultUnit_Box.addItems(['cm','mm','m','km','in'])

        elif self.ui.ConverterSubject_Box.currentText()=='DigitalVolume':

            self.ui.CurrentUnit_Box.addItems(['bit','byte','KByte','MByte','GByte','TByte'])
            self.ui.ResultUnit_Box.addItems(['byte','bit','KByte','MByte','GByte','TByte'])

        elif self.ui.ConverterSubject_Box.currentText()=='Temperature':

            self.ui.CurrentUnit_Box.addItems(['°C','°F','°K'])
            self.ui.ResultUnit_Box.addItems(['°F','°C','°K'])


    def calculate(self):
        quantity = self.ui.input.text()
        current_unit = self.ui.CurrentUnit_Box.currentText()
        converted_unit = self.ui.ResultUnit_Box.currentText()

        result = converts(quantity= quantity + current_unit, desired_unit= converted_unit)
        self.ui.output.setText(str(round(float(result), 2)))

app = QApplication([])
window = Convertor()
app.exec()