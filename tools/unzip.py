import os
import zipfile
import time
from tools.status import (
    format_duration,
    format_size,
    print_result_success,
    print_file_info,
)

def unzip_file(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"ZIP file tidak ditemukan: {input_path}")

    zip_file_name = os.path.basename(input_path)
    zip_file_size = os.path.getsize(input_path)

    print_file_info("Informasi File ZIP:", zip_file_name, zip_file_size, output_path)

    os.makedirs(output_path, exist_ok=True)

    print("🚀 Memulai proses ekstraksi...\n")
    start_time = time.time()
    extracted_files = 0

    with zipfile.ZipFile(input_path, 'r') as zip_ref:
        members = zip_ref.namelist()
        total_files = len([m for m in members if not m.endswith("/")])
        for i, member in enumerate(members, start=1):
            if member.endswith("/"):
                continue
            print(f"📂 [{extracted_files+1}/{total_files}] Mengekstrak: {member} ... ", end="")
            try:
                zip_ref.extract(member, path=output_path)
                print("OK")
                extracted_files += 1
            except Exception as e:
                print(f"GAGAL ({str(e)})")

    duration = format_duration(time.time() - start_time)
    if extracted_files > 0:
        print_result_success("Ekstraksi selesai:", zip_file_name, zip_file_size, jumlah=extracted_files, durasi=duration)
    else:
        print(f"\n❌ Tidak ada file yang berhasil diekstrak!")
