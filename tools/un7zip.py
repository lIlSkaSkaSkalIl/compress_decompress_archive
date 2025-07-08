import os
import subprocess
import time
from tools.status import TEXT, format_duration, print_file_info, print_result_success

def un7zip_file(input_path, output_path):
    subprocess.run(["apt-get", "install", "p7zip-full", "-y"], stdout=subprocess.DEVNULL)

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File .7z tidak ditemukan: {input_path}")

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    file_name = os.path.basename(input_path)
    size = os.path.getsize(input_path)

    print_file_info("📦 File yang akan diekstrak:", file_name, size, output_path)

    print("📦 Membaca isi arsip...")
    try:
        result = subprocess.run(
            ["7z", "l", "-ba", input_path],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.splitlines()
        file_list = [line.strip().split()[-1] for line in lines if not line.endswith('/') and len(line.strip().split()) >= 6]
    except:
        file_list = []

    total_files = len(file_list)
    for i, name in enumerate(file_list, start=1):
        print(f"📦 [{i}/{total_files}] Extracting: {name} ... OK")

    print("\n🚀 Memulai proses ekstraksi 7z...\n")
    start_time = time.time()

    try:
        subprocess.run(
            ["7z", "x", input_path, f"-o{output_path}", "-y"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
    except subprocess.CalledProcessError:
        print("❌ Gagal mengekstrak file 7z!")
        return

    duration = format_duration(time.time() - start_time)

    extracted_count = 0
    for _, _, files in os.walk(output_path):
        extracted_count += len(files)

    print_result_success("Ekstraksi selesai:", file_name, size, jumlah=extracted_count, durasi=duration)
