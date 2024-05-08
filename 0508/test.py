import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('주소록')

        layout = QVBoxLayout()

        self.name_label = QLabel('이름:')
        self.name_entry = QLineEdit()

        self.phone_label = QLabel('전화번호:')
        self.phone_entry = QLineEdit()

        self.add_button = QPushButton('추가')
        self.add_button.clicked.connect(self.add_contact)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_entry)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_entry.text()
        phone = self.phone_entry.text()

        if name and phone:
            messagebox = QMessageBox()
            messagebox.setWindowTitle('성공')
            messagebox.setText('주소록에 연락처가 추가되었습니다.')
            messagebox.exec_()
            self.clear_entries()
        else:
            messagebox = QMessageBox()
            messagebox.setWindowTitle('오류')
            messagebox.setText('이름과 전화번호를 모두 입력하세요.')
            messagebox.exec_()

    def clear_entries(self):
        self.name_entry.clear()
        self.phone_entry.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    address_book = AddressBook()
    address_book.show()
    sys.exit(app.exec_())