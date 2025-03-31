from PyQt6.QtWidgets import QMainWindow, QTableWidget, QToolBar
from user_interface.menu_bar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMenuBar(MenuBar())
        self.setWindowTitle("Sheet music management program")

        table = QTableWidget(6, 4)
        toolbar = QToolBar()
        refresh_action = toolbar.addAction("Refresh")

        self.addToolBar(toolbar)
        # self.setCentralWidget(table)

        self.show()
