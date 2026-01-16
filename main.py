import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSlider
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import landmarks.main as movement_ai

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Morning Check-In")
        self.setGeometry(2000, 2000, 500, 700)
        
        # Create central widget and layout
        central_widget = QWidget()
        
        # Set white background
        central_widget.setStyleSheet("background-color: #ffffff; color: #000000;")

        self.setCentralWidget(central_widget)
        
        # Main layout with centered content
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 40, 20, 40)
        main_layout.setSpacing(30)
        
        # Title
        title = QLabel("Morning Check-In")
        title_font = QFont()
        title_font.setPointSize(28)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # Question and Slider Container
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(20, 20, 20, 20)
        container_layout.setSpacing(20)
        container.setStyleSheet("background-color: #f5f5f5; border-radius: 15px;")
        
        # Question
        question = QLabel("How rested do\nyou feel today?")
        question_font = QFont()
        question_font.setPointSize(20)
        question.setFont(question_font)
        question.setAlignment(Qt.AlignCenter)
        container_layout.addWidget(question)
        
        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setValue(6)
        self.slider.setMinimumHeight(40)
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background-color: #d0d0d0;
                height: 4px;
                border-radius: 2px;
                margin: 8px 0px;
            }
            QSlider::handle:horizontal {
                background-color: #ffffff;
                border: 2px solid #999999;
                width: 18px;
                height: 18px;
                margin: -7px 0px;
                border-radius: 9px;
            }
            QSlider::handle:horizontal:hover {
                background-color: #f0f0f0;
            }
        """)
        self.slider.sliderMoved.connect(self.on_slider_moved)
        self.slider.valueChanged.connect(self.on_slider_moved)
        container_layout.addWidget(self.slider)
        
        # Low and High labels
        range_layout = QHBoxLayout()
        low_label = QLabel("Low")
        low_label.setStyleSheet("color: #999999; font-size: 12px;")
        high_label = QLabel("High")
        high_label.setStyleSheet("color: #999999; font-size: 12px;")
        range_layout.addWidget(low_label)
        range_layout.addStretch()
        range_layout.addWidget(high_label)
        container_layout.addLayout(range_layout)
        
        # Sleep Quality Display
        self.sleep_quality_label = QLabel("Sleep Quality: 6,4/10")
        sleep_quality_font = QFont()
        sleep_quality_font.setPointSize(16)
        self.sleep_quality_label.setFont(sleep_quality_font)
        self.sleep_quality_label.setAlignment(Qt.AlignCenter)
        self.sleep_quality_label.setStyleSheet("color: #666666;")
        container_layout.addWidget(self.sleep_quality_label)
        
        main_layout.addWidget(container)
        
        # Advice Container
        advice_container = QWidget()
        advice_container_layout = QVBoxLayout(advice_container)
        advice_container_layout.setContentsMargins(20, 20, 20, 20)
        advice_container_layout.setSpacing(20)
        advice_container.setStyleSheet("background-color: #f5f5f5; border-radius: 15px;")
        
        # Advice Title
        advice_title = QLabel("Advice for the day:")
        advice_title_font = QFont()
        advice_title_font.setPointSize(14)
        advice_title.setFont(advice_title_font)
        advice_title.setAlignment(Qt.AlignCenter)
        advice_container_layout.addWidget(advice_title)
        
        # Advice Display
        self.advice_label = QLabel("Perform exercise to receive advice")
        advice_display_font = QFont()
        advice_display_font.setPointSize(18)
        advice_display_font.setBold(True)
        self.advice_label.setFont(advice_display_font)
        self.advice_label.setAlignment(Qt.AlignCenter)
        self.advice_label.setStyleSheet("color: #5a7d99;")
        advice_container_layout.addWidget(self.advice_label)
        
        main_layout.addWidget(advice_container)
        
        # Exercise Intensity Container
        intensity_container = QWidget()
        intensity_container_layout = QVBoxLayout(intensity_container)
        intensity_container_layout.setContentsMargins(20, 20, 20, 20)
        intensity_container_layout.setSpacing(10)
        intensity_container.setStyleSheet("background-color: #f5f5f5; border-radius: 15px;")

        intensity_title = QLabel("Exercise Intensity:")
        intensity_title_font = QFont()
        intensity_title_font.setPointSize(14)
        intensity_title.setFont(intensity_title_font)
        intensity_title.setAlignment(Qt.AlignCenter)
        intensity_container_layout.addWidget(intensity_title)

        self.intensity_label = QLabel("No exercise performed yet")
        intensity_display_font = QFont()
        intensity_display_font.setPointSize(16)
        intensity_display_font.setBold(True)
        self.intensity_label.setFont(intensity_display_font)
        self.intensity_label.setAlignment(Qt.AlignCenter)
        self.intensity_label.setStyleSheet("color: #666666;")
        self.intensity_label.setWordWrap(True)
        self.intensity_label.setMinimumHeight(60)
        intensity_container_layout.addWidget(self.intensity_label)

        main_layout.addWidget(intensity_container)
        
        # Add stretch to push button to bottom
        main_layout.addStretch()
        
        # Submit Button
        submit_button = QPushButton("Perform Exercise")
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #5a7d99;
                padding: 15px;
                border-radius: 25px;
                border: 2px solid #5a7d99;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)
        submit_button.setMinimumHeight(50)
        submit_button.clicked.connect(self.on_submit_clicked)
        main_layout.addWidget(submit_button)
    
    def on_slider_moved(self):
        value = self.slider.value()
        # Generate a random decimal between 0-1 for the decimal part
        import random
        decimal = random.randint(0, 9)
        self.sleep_quality_label.setText(f"Sleep Quality: {value},{decimal}/10")
    
    def on_submit_clicked(self):
        sleep_score = self.slider.value()
        print(f"Sleep quality submitted: {sleep_score}/10")
        movement_score:int  = movement_ai.main()
        # Determine exercise intensity from movement_score and update UI
        try:
            ms = int(movement_score)
        except Exception:
            ms = movement_score

        if ms < 50:
            intensity = "Low"
            rec = "Light activity — 10–20 min"
            color = "#2e8b57"
        elif ms < 150:
            intensity = "Moderate"
            rec = "Moderate — 20–40 min"
            color = "#f39c12"
        else:
            intensity = "High"
            rec = "High — 10–30 min or consider resting"
            color = "#c0392b"

        self.intensity_label.setText(f"{intensity} (movement score: {ms})")
        self.intensity_label.setStyleSheet(f"color: {color};")

        # Generate advice based on both sleep and exercise scores
        if sleep_score < 5 and ms >= 150:
            advice = "Have a Rest Day"
            advice_color = "#c0392b"
        elif sleep_score < 5:
            advice = "Go to Sleep Early"
            advice_color = "#c0392b"
        elif sleep_score < 7 and ms < 50:
            advice = "Train More"
            advice_color = "#f39c12"
        elif sleep_score >= 8 and ms < 50:
            advice = "Train More"
            advice_color = "#2e8b57"
        elif sleep_score < 6 and ms >= 150:
            advice = "Have a Rest Day"
            advice_color = "#c0392b"
        elif sleep_score >= 8 and ms >= 150:
            advice = "Have a Rest Day"
            advice_color = "#2e8b57"
        else:
            advice = "Maintain Your Routine"
            advice_color = "#5a7d99"
        
        self.advice_label.setText(advice)
        self.advice_label.setStyleSheet(f"color: {advice_color};")


    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
