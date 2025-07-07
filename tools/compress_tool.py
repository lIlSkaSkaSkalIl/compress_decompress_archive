from tools.zip import zip_folder
from tools.unzip import unzip_file
from tools.rar import rar_folder
from tools.unrar import unrar_file

def run_tool(metode, input_path, output_path):
    metode = metode.lower()
    print(f"\n📦 Metode yang dipilih: {metode.upper()}")
    
    if metode == "zip":
        zip_folder(input_path, output_path)
    elif metode == "unzip":
        unzip_file(input_path, output_path)
    elif metode == "rar":
        rar_folder(input_path, output_path)
    elif metode == "unrar":
        unrar_file(input_path, output_path)
    else:
        raise ValueError("Metode tidak dikenal!")
