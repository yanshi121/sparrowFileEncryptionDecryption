import sys
from PyQt5.QtWidgets import QApplication
from sparrowFileEncryptionDecryption.decryption import SparrowFileDecryption
from sparrowFileEncryptionDecryption.encryption import SparrowFileEncryption


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sfd = SparrowFileDecryption()
    sfe = SparrowFileEncryption()
    sys.exit(app.exec_())
