from data import send
from time import sleep
from random import randint
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLineEdit


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Internship Spider (Interactive Mode)')
        self.show_main()

    def show_main(self):
        layout = QVBoxLayout()
        boxes = ['company', 'image', 'description', 'name', 'apply']
        labels = ['Company Name', 'Image Link', 'Description', 'Title', 'Link']
        self.boxes = dict()
        self.labels = dict()
        for box, label in zip(boxes, labels):
            self.labels[box] = QLabel(label)
            self.boxes[box] = QLineEdit()
            layout.addWidget(self.labels[box])
            layout.addWidget(self.boxes[box])
        queue = QPushButton('Queue')
        activate = QPushButton('Send')
        activate.clicked.connect(self.send)
        queue.clicked.connect(self.queue)
        layout.addWidget(queue)
        layout.addWidget(activate)
        self.setLayout(layout)

    def send(self):
        data = dict()
        for box in self.boxes:
            data[box] = self.boxes[box].text()
        if send(**data):
            for box in self.boxes:
                self.boxes[box].clear()
        else:
            self.show_failure()

    def queue(self):
        data = dict()
        for box in self.boxes:
            data[box] = self.boxes[box].text()
            self.boxes[box].clear()
        timer = randint(5, 90)
        print(f'Sleeping for {timer}s to post {data["company"]}')
        sleep(randint(5, 90))
        send(**data)
        self.send()

    def show_failure(self):
        alert = QMessageBox()
        alert.setWindowTitle('Failure to send!')
        alert.setText(
            'Something went wrong while trying to send. Most likely you provided a bad URL or your internet connection is down.')
        alert.exec_()


def generate_app():
    return QApplication([])
