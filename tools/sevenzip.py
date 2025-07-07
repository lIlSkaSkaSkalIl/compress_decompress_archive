import os
import subprocess
import time
from tools.status import TEXT, format_duration, print_summary, print_result_success

def seven_zip_folder(input_path, output_path):
    subprocess.run(["apt-get", "install", "p7zip-full", "-y"], stdout=subprocess.DEVNULL)

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Path tidak ditemukan: {input_path}")

    file_list = []
    total_size = 0
    total_files = 0

    if os.path.isfile(input_path):
        file_list.append((input_path, os.path.basename(input_path)))
        total_size = os.path.getsize(input_path)
        total_files = 1
    else:
        for root, _, files in os.walk(input_path):
            for f in files:
                abs_path = os.path.join(root, f)
                rel_path = os.path.relpath(abs_path, os.path.dirname(input_path))
                file_list.append((abs_path, rel_path))
                total_files += 1
                try:
                    total_size += os.path.getsize(abs_path)
                except:
                    pass

    output_7z = f"{output_path}.7z"
    archive_name = os.path.basename(output_7z)

    print_summary("Ringkasan File/Folder:", total_files, total_size,
                  f"{'Nama file 7Z':<17}: {archive_name}", output_7z)

    os.chdir(os.path.dirname(input_path))
    print("🚀 Memulai proses kompresi...\n")
    start_time = time.time()

    try:
        result = subprocess.run(
            ["7z", "a", "-t7z", "-mx=9", output_7z, os.path.basename(input_path)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
    except subprocess.CalledProcessError:
        print("❌ Gagal membuat file 7z!")
        return

    os.chdir("/content")
    duration = format_duration(time.time() - start_time)

    if os.path.exists(output_7z):
        size = os.path.getsize(output_7z)
        print_result_success("Kompresi selesai:", archive_name, size, jumlah=total_files, durasi=duration)
    else:
        print("❌ File 7z tidak ditemukan setelah proses selesai.")
