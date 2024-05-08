import os
from io import StringIO
import pandas as pd
from sparrowEncryptionDecryption import SparrowEncryptionDecryption


class DecryptionFile:
    def __init__(self):
        self.sed = SparrowEncryptionDecryption()

    def decryption_excel(self, key, folder, file, to_file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
        dfs = eval(self.sed.order_decryption(data, key))
        to_file_path = os.path.join(folder, f"{to_file}.xlsx")
        with pd.ExcelWriter(to_file_path) as writer:
            for i in dfs.keys():
                df = pd.read_json(StringIO(dfs[i]), orient='records')
                df.to_excel(writer, sheet_name=i, index=False)

    def decryption_txt(self, key, folder, file, to_file, file_type):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()
        data = self.sed.order_decryption(data, key)
        to_file_path = os.path.join(folder, f"{to_file}.{file_type}")
        with open(to_file_path, 'w', encoding='utf-8') as writer:
            writer.write(data)
