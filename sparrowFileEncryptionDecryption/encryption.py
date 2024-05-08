import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from sparrowFileEncryptionDecryption.function import EncryptionFile
from sparrowFileEncryptionDecryption.function import Tools


class SparrowFileEncryption(QWidget):
    def __init__(self):
        self.ef = EncryptionFile()
        self.select_folder_button = None
        self.select_folder_text = None
        self.select_file_button = None
        self.select_file_text = None
        self.file_name_edit = None
        self.file_name_input = None
        self.key_edit = None
        self.key_input = None
        self.button_encryption = None
        self.folder_path = None
        self.file_path = None
        self.choose_compress = None
        self.chose_mode = None
        self.buttons_compress = []
        self.button_mode = []
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('麻雀加密')
        self.setGeometry(300, 300, 400, 300)
        layout = QVBoxLayout()
        self.select_folder_button = QPushButton('选择加密文件保存文件夹')
        self.select_folder_button.clicked.connect(self.choose_folder)
        layout.addWidget(self.select_folder_button)
        self.select_folder_text = QLabel('')
        layout.addWidget(self.select_folder_text)
        self.select_file_button = QPushButton('选择被加密文件')
        self.select_file_button.clicked.connect(self.choose_file)
        layout.addWidget(self.select_file_button)
        self.select_file_text = QLabel('')
        layout.addWidget(self.select_file_text)
        radio_group1 = QGroupBox('压缩次数')
        radio_layout1 = QHBoxLayout()
        self.choose_compress = ['二次压缩', '一次压缩', '不压缩']
        for option in self.choose_compress:
            radio_btn = QRadioButton(option)
            radio_layout1.addWidget(radio_btn)
            self.buttons_compress.append(radio_btn)
        self.buttons_compress[0].setChecked(True)
        radio_group1.setLayout(radio_layout1)
        layout.addWidget(radio_group1)
        radio_group2 = QGroupBox('加密模式')
        radio_layout2 = QHBoxLayout()
        self.chose_mode = ['二进制加密', '四进制加密']
        for option in self.chose_mode:
            radio_btn = QRadioButton(option)
            radio_layout2.addWidget(radio_btn)
            self.button_mode.append(radio_btn)
        self.button_mode[0].setChecked(True)
        radio_group2.setLayout(radio_layout2)
        layout.addWidget(radio_group2)
        self.file_name_edit = QLineEdit()
        self.file_name_input = QLabel('加密文件保存名字')
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.file_name_edit)
        self.key_edit = QLineEdit()
        self.key_input = QLabel('秘钥')
        layout.addWidget(self.key_input)
        layout.addWidget(self.key_edit)
        self.button_encryption = QPushButton('加密')
        self.button_encryption.clicked.connect(self.on_ok_clicked)
        layout.addWidget(self.button_encryption)
        self.setLayout(layout)
        self.show()

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, '选择文件件', '/')
        if folder_path:
            self.folder_path = folder_path
            self.select_folder_text.setText(self.folder_path.split("/")[-1])

    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择加密文件', '/',
                                                   'Excel (*.xlsx; *.xls);;'
                                                   '文本文件 (*.txt);;'
                                                   'Python (*.py; *.ipynb; *.py3);;'
                                                   'Java (*.java; *.scala);;'
                                                   'JavaScript (*.js; *.ts);;'
                                                   'HTML (*.html; *htm);;'
                                                   '样式表 (*.css; *.less; *.pcss; *.scss; *.sass);;'
                                                   'C/C++ (*.c; *.cpp; *.cc; *.C; *.cxx; *.c++; *.h);;'
                                                   'PHP (*.php);;'
                                                   'Go (*.go);;'
                                                   'Kotlin (*.kt);;'
                                                   'C# (*.cs);;'
                                                   'Ruby (*.rb);;'
                                                   'Perl (*.pl; *.pm);;'
                                                   'Swift (*.swift);;'
                                                   'sql (*.sql; *.db);;'
                                                   'R (*.R)')
        if file_path:
            self.file_path = file_path
            self.select_file_text.setText(self.file_path.split("/")[-1])

    def encryption(self, folder, file, times, function, key, to_file):
        if function == '二进制加密':
            function = 0
        else:
            function = 1
        if times == "二次压缩":
            times = 2
        elif times == "一次压缩":
            times = 1
        else:
            times = 0
        file_type = file.split("/")[-1].split(".")[-1]
        if file_type in ["xls", "xlsx"]:
            try:
                self.ef.encryption_excel(file, key, -1, times, function, folder, to_file)
                Tools.show_message_box("提示", "加密成功")
            except Exception as e:
                Tools.show_message_box("提示", e)
        elif file_type in ["txt", "py", "java", "js", "html", "ipynb", "less", "css", "pcss", "scss", "ts", "sass", "c",
                           "cpp", "cc", "C", "cxx", "c++", 'h', "php", "go", "kt", "cs", "rb", "pl", "pm", "swift", "sql",
                           "db", 'R', "scala"]:
            try:
                self.ef.encryption_txt(file, key, -1, times, function, folder, to_file, file_type)
                Tools.show_message_box("提示", "加密成功")
            except Exception as e:
                Tools.show_message_box("提示", e)
        else:
            Tools.show_message_box("提示", f"{file_type}格式文件暂不支持加密")

    def on_ok_clicked(self):
        for radio_btn in self.buttons_compress:
            if radio_btn.isChecked():
                radio_selection1 = radio_btn.text()
                break
        else:
            radio_selection1 = "No option selected"
        for radio_btn in self.button_mode:
            if radio_btn.isChecked():
                radio_selection2 = radio_btn.text()
                break
        else:
            radio_selection2 = "No option selected"
        text_input1 = self.file_name_edit.text()
        text_input2 = self.key_edit.text()
        self.encryption(self.folder_path, self.file_path, radio_selection1, radio_selection2, text_input2, text_input1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SparrowFileEncryption()
    sys.exit(app.exec_())
