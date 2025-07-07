import os
import subprocess
import time
from tools.status import (
    format_duration,
    format_size,
    print_result_success,
    print_file_info,
)

def unrar_file(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"RAR file tidak ditemukan: {input_path}")
    
    subprocess.run(["apt-get", "install", "unrar", "-y"], stdout=subprocess.DEVNULL)

    rar_file_name = os.path.basename(input_path)
    rar_file_size = os.path.getsize(input_path)

    print_file_info("Informasi File RAR:", rar_file_name, rar_file_size, output_path)

    os.makedirs(output_path, exist_ok=True)

    try:
        result = subprocess.run(["unrar", "lb", input_path], capture_output=True, text=True, check=True)
        members = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        total_files = len(members)
    except:
        print("❌ Gagal membaca isi file RAR.")
        members = []
        total_files = 0

    print("🚀 Memulai proses ekstraksi...\n")
    start_time = time.time()
    extracted_files = 0

    for i, member in enumerate(members, start=1):
        print(f"📂 [{i}/{total_files}] Extracting: {member} ... ", end="")
        try:
            subprocess.run(["unrar", "e", "-y", input_path, member, output_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print("OK")
            extracted_files += 1
        except subprocess.CalledProcessError:
            print("GAGAL")

    duration = format_duration(time.time() - start_time)
    if extracted_files > 0:
        print_result_success("Ekstraksi selesai:", rar_file_name, rar_file_size, jumlah=extracted_files, durasi=duration)
    else:
        print("❌ Tidak ada file yang berhasil diekstrak.")
