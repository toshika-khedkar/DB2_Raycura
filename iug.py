from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QToolBox,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.toolBox = QToolBox(self.centralWidget)
        self.toolBox.setStyleSheet(
            "QToolBox { background-color: rgb(255, 255, 255); font-size: 20px;}"
        )

        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 348, 63))
        self.horizontalLayout_4 = QVBoxLayout(self.page)

        # Create QLabel at the top of the page
        self.label = QLabel("Neck", self.page)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 18px;")

        self.horizontalLayout_4.addWidget(self.label)

        self.widget_12 = QWidget(self.page)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.pushButton_5 = QPushButton(self.widget_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(16777215, 369))
        self.pushButton_5.setStyleSheet(
            "background-color:rgb(255, 192, 193); border-radius:10px;"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        # Connect the button click to the updateLabel method
        self.pushButton_5.clicked.connect(lambda: self.updateLabel("Neck", "PushButton 5"))

        self.horizontalLayout_4.addWidget(self.widget_12)

        self.toolBox.addItem(self.page, u"Neck")

        # Add more pages similarly with their buttons

        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.centralLayout.addWidget(self.toolBox)

    def updateLabel(self, category, button_name):
        # Update the label text when a button is clicked
        self.label.setText(f"{category} >> {button_name}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
