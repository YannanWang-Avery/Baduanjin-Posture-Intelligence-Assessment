import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QTimer

class VideoPlayer(QMainWindow):
    def __init__(self, video_file):
        super().__init__()

        # Load video file
        self.cap = cv2.VideoCapture(video_file)

        # Get video properties
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.video_length = int(total_frames / fps)

        # Create slider widget
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(total_frames)
        self.slider.sliderMoved.connect(self.set_position)

        # Create label widget to display current frame
        self.frame_label = QLabel(self)

        # Create input widgets
        self.start_frame_edit = QLineEdit()
        self.end_frame_edit = QLineEdit()
        self.save_path_edit = QLineEdit()
        self.browse_button = QPushButton('Browse')
        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_frames)
        # 创建一个用于暂停和恢复播放的按钮
        
        self.pause_button = QPushButton('Pause', self)
        self.pause_button.clicked.connect(self.toggle_pause)

        
        # Create layout for input widgets
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('Start Frame'))
        input_layout.addWidget(self.start_frame_edit)
        input_layout.addWidget(QLabel('End Frame'))
        input_layout.addWidget(self.end_frame_edit)
        input_layout.addWidget(QLabel('Save Path'))
        input_layout.addWidget(self.save_path_edit)
        input_layout.addWidget(self.save_button)
        input_layout.addWidget(self.pause_button)
        input_widget = QWidget()
        input_widget.setLayout(input_layout)

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.slider)
        main_layout.addWidget(self.frame_label)
        main_layout.addWidget(input_widget)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        # Set main widget
        self.setCentralWidget(main_widget)
        self.save_path_edit.setText('./image/')
        # Create window
        self.setWindowTitle('Video Player')
        self.setGeometry(100, 100, 640, 360)

        # Create timer to update video frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(25)

    def set_position(self, position):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, position)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imshow('Video', frame)
            position = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            self.slider.setValue(position)
            self.frame_label.setText('Frame: {}'.format(position))
        else:
            self.timer.stop()

    def toggle_pause(self):
        self.start_frame_edit.setText(str(int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))))

    def save_frames(self):
        start_frame = int(self.start_frame_edit.text())
        # 如果空格按下
        
        # end_frame = int(self.end_frame_edit.text())
        save_path = self.save_path_edit.text()
        for frame_num in range(start_frame, start_frame+50):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = self.cap.read()
            if ret:
                if self.cap.get(cv2.CAP_PROP_POS_FRAMES)%5 == 0:
                    path_s = '{}w{:04}.jpg'.format(save_path, frame_num)
                    print(self.cap.get(cv2.CAP_PROP_POS_FRAMES),path_s)
                    cv2.imwrite('{}w{:04}.jpg'.format(save_path, frame_num), frame)
        # self.start_frame_edit.setText(str(end_frame))
        self.end_frame_edit.setText('')
        self.save_path_edit.setText(str(save_path))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer('./video/28.mp4')
    player.show()
    sys.exit(app.exec_())