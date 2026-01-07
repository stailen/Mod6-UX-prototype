import sys
from PySide6.QtWidgets import QApplication, QFormLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Health & Fitness Tracker")
        self.setGeometry(2000, 2000, 500, 700)
        
        # Create central widget and layout
        central_widget = QWidget()
        
        # Set blue background
        central_widget.setStyleSheet("background-color: #1e3a8a; color: white;")

        self.setCentralWidget(central_widget)
        
        # Main layout with centered content
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(15)
        
        # Title
        title = QLabel("💪 Health & Fitness Tracker")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Stats form layout (centered)
        stats = QFormLayout()
        stats.setSpacing(10)
        
        # Heart Rate
        hr_label = QLabel("❤️ Heart Rate:")
        hr_value = QLabel("72 BPM")
        hr_value.setStyleSheet("font-weight: bold; font-size: 14px;")
        stats.addRow(hr_label, hr_value)
        
        # Steps
        steps_label = QLabel("👟 Steps Today:")
        steps_value = QLabel("8,542 / 10,000")
        steps_value.setStyleSheet("font-weight: bold; font-size: 14px;")
        stats.addRow(steps_label, steps_value)
        
        # Calories Burned
        cal_label = QLabel("🔥 Calories Burned:")
        cal_value = QLabel("524 kcal")
        cal_value.setStyleSheet("font-weight: bold; font-size: 14px;")
        stats.addRow(cal_label, cal_value)
        
        # Sleep
        sleep_label = QLabel("😴 Sleep:")
        sleep_value = QLabel("7h 30m")
        sleep_value.setStyleSheet("font-weight: bold; font-size: 14px;")
        stats.addRow(sleep_label, sleep_value)
        
        # Exercise State
        exercise_label = QLabel("Exercise State:")
        exercise_value = QLabel("Active")
        exercise_value.setStyleSheet("font-weight: bold; font-size: 14px; color: #4ade80;")
        stats.addRow(exercise_label, exercise_value)

        main_layout.addLayout(stats)
        
        # Buttons
        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(10)
        
        # AI Recommendations button
        ai_button = QPushButton("🤖 Start Exercise Video")
        ai_button.setStyleSheet("background-color: #3b82f6; color: white; padding: 10px; border-radius: 5px; font-weight: bold;")
        ai_button.clicked.connect(self.on_ai_button_clicked)
        button_layout.addWidget(ai_button)
        
        # Log Workout button
        workout_button = QPushButton("📝 Log Workout")
        workout_button.setStyleSheet("background-color: #10b981; color: white; padding: 10px; border-radius: 5px; font-weight: bold;")
        workout_button.clicked.connect(self.on_workout_button_clicked)
        button_layout.addWidget(workout_button)
        
        # View Progress button
        progress_button = QPushButton("📊 View Progress")
        progress_button.setStyleSheet("background-color: #f59e0b; color: white; padding: 10px; border-radius: 5px; font-weight: bold;")
        progress_button.clicked.connect(self.on_progress_button_clicked)
        button_layout.addWidget(progress_button)
        
        main_layout.addLayout(button_layout)
    
    def on_ai_button_clicked(self):
        print("Getting AI recommendations...")
    
    def on_workout_button_clicked(self):
        print("Logging workout...")
    
    def on_progress_button_clicked(self):
        print("Viewing progress...")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
