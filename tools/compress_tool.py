from tools.zip import zip_folder
from tools.unzip import unzip_file
from tools.rar import rar_folder
from tools.unrar import unrar_file
from tools.sevenzip import seven_zip_folder
from tools.un7zip import un7zip_file
from tools.tar import tar_folder
from tools.untar import untar_file

def run_tool(metode, input_path, output_path, tar_method="gz"):
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
    elif metode == "7z":
        seven_zip_folder(input_path, output_path)
    elif metode == "un7z":
        un7zip_file(input_path, output_path)
    elif metode == "tar":
        tar_folder(input_path, output_path, method=tar_method)
    elif metode == "untar":
        untar_file(input_path, output_path)
    else:
        raise ValueError("Metode tidak dikenal!")
