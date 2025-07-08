import os
import tarfile
import time
from tools.status import TEXT, format_duration, print_file_info, print_result_success

def untar_file(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File .tar tidak ditemukan: {input_path}")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    file_name = os.path.basename(input_path)
    size = os.path.getsize(input_path)

    print_file_info("📦 File yang akan diekstrak:", file_name, size, output_path)

    print("📦 Membaca isi arsip TAR...\n")
    try:
        with tarfile.open(input_path, 'r') as tar:
            members = tar.getmembers()
    except Exception as e:
        print(f"❌ Gagal membuka arsip TAR: {e}")
        return

    total_files = len([m for m in members if m.isfile()])
    success = 0

    print("🚀 Memulai proses ekstraksi...\n")
    start_time = time.time()

    try:
        with tarfile.open(input_path, 'r') as tar:
            for i, member in enumerate(members, start=1):
                if member.isfile():
                    print(f"📦 [{success+1}/{total_files}] Extracting: {member.name} ... ", end="")
                    try:
                        tar.extract(member, path=output_path)
                        print("OK")
                        success += 1
                    except Exception as e:
                        print(f"GAGAL ({str(e)})")
    except Exception as e:
        print(f"❌ Gagal mengekstrak: {e}")
        return

    duration = format_duration(time.time() - start_time)

    print_result_success("Ekstraksi selesai:", file_name, size, jumlah=success, durasi=duration)
