import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mod6 UX prototype")
        self.setGeometry(100, 100, 400, 300)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create button
        button = QPushButton("I WANT AI")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)
    
    def on_button_clicked(self):
        print("Button clicked!") #TODO  STEFANO CONNECTS THIS TO HIS SHIT


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
