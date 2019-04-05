from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta1 = QLabel("Browse:", self)
        etykieta2 = QLabel("Run Time:", self)
        etykieta3 = QLabel("Cmax:", self)
        etykieta3.setAlignment(QtCore.Qt.AlignCenter)
        etykieta4 = QLabel("0", self)
        etykieta4.setAlignment(QtCore.Qt.AlignCenter)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 1, 0)
        ukladT.addWidget(etykieta3, 0, 4)
        ukladT.addWidget(etykieta4, 1, 4)

        # przyciski
        RunBtn = QPushButton("&Run", self)

        # 1-liniowe pola edycyjne
        self.Browse = QLineEdit()
        self.RunTime = QLineEdit()

        ukladT.addWidget(self.Browse, 0, 1)
        ukladT.addWidget(self.RunTime, 1, 1)
        ukladT.addWidget(RunBtn, 2, 1)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)



        self.resize(400, 150)
        self.setWindowTitle("Flow Shop Algoritm")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
