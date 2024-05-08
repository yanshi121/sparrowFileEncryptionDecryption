import os
import pandas as pd
from sparrowEncryptionDecryption import SparrowEncryptionDecryption


class EncryptionFile:
    def __init__(self):
        self.sed = SparrowEncryptionDecryption()

    def encryption_excel(self, file_path, key, effective_duration, is_compression, mode, folder, to_file):
        xls = pd.ExcelFile(file_path)
        dfs = {sheet_name: xls.parse(sheet_name).to_json(orient='records', force_ascii=False) for sheet_name in xls.sheet_names}
        encrypted_data = self.sed.order_encryption(str(dfs), key, effective_duration=effective_duration, is_compression=is_compression, mode=mode)
        path = os.path.join(folder, f"{to_file}.xlsx.sfed")
        with open(path, 'w', encoding='utf-8') as file:
            file.write(str(encrypted_data))

    def encryption_txt(self, file_path, key, effective_duration, is_compression, mode, folder, to_file, file_type):
        with open(rf'{file_path}', 'r', encoding='utf-8') as file:
            data = file.read()
        encrypted_data = self.sed.order_encryption(data, key, effective_duration=effective_duration, is_compression=is_compression, mode=mode)
        path = os.path.join(folder, f"{to_file}.{file_type}.sfed")
        with open(path, 'w', encoding='utf-8') as file:
            file.write(str(encrypted_data))
