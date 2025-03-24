from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
)
import sys

app = QApplication(sys.argv)

table = QTableWidget(4, 4)

window = QMainWindow()
window.setWindowTitle("APP")
window.setCentralWidget(table)
window.show()

app.exec()
