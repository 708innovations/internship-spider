from data import send
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLineEdit
from random import randint
from time import sleep


class Worker(QThread):
    def __init__(self, data: dict):
        QThread.__init__(self)
        self.data = data

    def run(self):
        send(**self.data)

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
        queue.clicked.connect(self.start_queue)
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

    def start_queue(self):
        data = dict()
        for box in self.boxes:
            data[box] = self.boxes[box].text()
            self.boxes[box].clear()
        thread = Worker(data)
        # thread.started.connect(self.queue)
        timer = randint(5, 90)
        print(f'Sleeping for {timer}s to post {data["company"]}')
        thread.sleep(timer)
        thread.start()

    def queue(self, data: dict):
        send(**data)

    def show_failure(self):
        alert = QMessageBox()
        alert.setWindowTitle('Failure to send!')
        alert.setText(
            'Something went wrong while trying to send. Most likely you provided a bad URL or your internet connection is down.')
        alert.exec_()


def generate_app():
    return QApplication([])
