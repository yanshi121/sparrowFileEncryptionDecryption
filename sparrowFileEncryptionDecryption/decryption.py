import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from sparrowFileEncryptionDecryption.function import DecryptionFile
from sparrowFileEncryptionDecryption.function import Tools


class SparrowFileDecryption(QWidget):
    def __init__(self):
        self.df = DecryptionFile()
        self.select_folder_button = None
        self.select_folder_text = None
        self.select_file_button = None
        self.select_file_text = None
        self.file_name_edit = None
        self.file_name_input = None
        self.key_edit = None
        self.key_input = None
        self.button_decryption = None
        self.folder_path = None
        self.file_path = None
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('麻雀解密')
        self.setGeometry(700, 300, 400, 300)
        layout = QVBoxLayout()
        self.select_folder_button = QPushButton('选择解密文件保存文件夹')
        self.select_folder_button.clicked.connect(self.choose_folder)
        layout.addWidget(self.select_folder_button)
        self.select_folder_text = QLabel('')
        layout.addWidget(self.select_folder_text)
        self.select_file_button = QPushButton('选择被解密文件')
        self.select_file_button.clicked.connect(self.choose_file)
        layout.addWidget(self.select_file_button)
        self.select_file_text = QLabel('')
        layout.addWidget(self.select_file_text)
        self.file_name_edit = QLineEdit()
        self.file_name_input = QLabel('解密文件保存名字')
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.file_name_edit)
        self.key_edit = QLineEdit()
        self.key_input = QLabel('秘钥')
        layout.addWidget(self.key_input)
        layout.addWidget(self.key_edit)
        self.button_decryption = QPushButton('解密')
        self.button_decryption.clicked.connect(self.on_ok_clicked)
        layout.addWidget(self.button_decryption)
        self.setLayout(layout)
        self.show()

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件件', '/')
        if folder_path:
            self.folder_path = folder_path
            self.select_folder_text.setText(self.folder_path.split("/")[-1])

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择解密文件', '/', 'sfed (*.sfed)')
        if file_path:
            self.file_path = file_path
            self.select_file_text.setText(self.file_path.split("/")[-1])

    def decryption(self, folder, file, key, to_file):
        file_type = file.replace(".sfed", '').split("/")[-1].split(".")[-1]
        if file_type == "xlsx":
            try:
                self.df.decryption_excel(key, folder, file, to_file)
                Tools.show_message_box("提示", "解密成功")
            except Exception as e:
                Tools.show_message_box("提示", e)
        elif file_type in ["txt", "py", "java", "js", "html", "ipynb", "less", "css", "pcss", "scss", "ts", "sass", "c",
                           "cpp", "cc", "C", "cxx", "c++", 'h', "php", "go", "kt", "cs", "rb", "pl", "pm", "swift", "sql",
                           "db", 'R', "scala"]:
            try:
                self.df.decryption_txt(key, folder, file, to_file, file_type)
                Tools.show_message_box("提示", "解密成功")
            except Exception as e:
                Tools.show_message_box("提示", e)
        else:
            Tools.show_message_box("提示", f"{file_type}格式文件暂不支持解密,如加密文件确认无误,请检查中断格式是否被更改,如:t.txt.sfed被修改为t.tx.sfed")

    def on_ok_clicked(self):
        text_input1 = self.file_name_edit.text()
        text_input2 = self.key_edit.text()
        self.decryption(self.folder_path, self.file_path, text_input2, text_input1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SparrowFileDecryption()
    sys.exit(app.exec_())
