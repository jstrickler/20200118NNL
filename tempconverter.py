#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QDoubleValidator
from ui_temperatureconverter import Ui_TemperatureConverter
from tconverters import c2f, c2k, f2c, f2k, k2c, k2f

class TemperatureConverterMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_TemperatureConverter()
        self.ui.setupUi(self)

        self.ui.le_input.setValidator(QDoubleValidator())

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

        self.ui.bt_convert.clicked.connect(self._pushed)

    def _pushed(self):
        input_value = float(self.ui.le_input.text())

        converter = self._get_converter()  # choose conversion function

        result = converter(input_value)  # do the conversion

        result = round(result, 3)  # round to 3 decimal places

        self.ui.le_result.setText(str(result))  # update the result window

    def _get_converter(self):
        if self.ui.rb_in_celsius.isChecked() and self.ui.rb_out_fahrenheit.isChecked():
            return c2f
        elif self.ui.rb_in_celsius.isChecked() and self.ui.rb_out_kelvin.isChecked():
            return c2k
        elif self.ui.rb_in_fahrenheit.isChecked() and self.ui.rb_out_celsius.isChecked():
            return f2c
        elif self.ui.rb_in_fahrenheit.isChecked() and self.ui.rb_out_kelvin.isChecked():
            return f2k
        elif self.ui.rb_in_kelvin.isChecked() and self.ui.rb_out_celsius.isChecked():
            return k2c
        elif self.ui.rb_in_kelvin.isChecked() and self.ui.rb_out_fahrenheit.isChecked():
            return k2f
        else:
            return lambda x: x  # "null" converter -- returns its input

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TemperatureConverterMain()
    main.show()
    sys.exit(app.exec_())
