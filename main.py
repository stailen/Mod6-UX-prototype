import sys
from PySide6.QtWidgets import QApplication, QFormLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Mod6 UX prototype")
        self.setGeometry(5000, 5000, 700,1000)
        
        # Create central widget and layout
        central_widget = QWidget()

        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        stats = QFormLayout()

        layout.addLayout(stats)
        stats.addRow("Exercise State:", QLabel("Ur sleepy"))

        # Create button
        button = QPushButton("I WANT AI")
        button.clicked.connect(self.on_button_clicked)
        stats.addRow("Do you want AI?:",button)
    
    def on_button_clicked(self):
        print("HE WANTS AI!!!!!!!!!!!!!!!!!!!!!!!!!!") #TODO  STEFANO CONNECTS THIS TO HIS SHIT


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
