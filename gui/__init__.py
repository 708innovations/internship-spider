from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit

class UI(QWidget):
    def __init__(self):
        super().__init__()
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
        activate = QPushButton('Send')
        activate.clicked.connect(self.send)
        layout.addWidget(activate)
        self.setLayout(layout)

    def send(self):
        pass

def generate_app():
    return QApplication([])
