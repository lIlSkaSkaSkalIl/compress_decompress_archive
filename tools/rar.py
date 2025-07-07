import os
import subprocess
import time
from tools.status import TEXT, format_duration, print_summary, print_result_success

def rar_folder(input_path, output_path):
    subprocess.run(["apt-get", "install", "rar", "-y"], stdout=subprocess.DEVNULL)
    
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

    rar_file_path = f"{output_path}.rar"
    rar_file_name = os.path.basename(rar_file_path)

    print_summary("Ringkasan File/Folder:", total_files, total_size,
                  f"{TEXT['nama_file_rar']:<17}: {rar_file_name}", rar_file_path)

    os.chdir(os.path.dirname(input_path))
    print("🚀 Memulai proses kompresi...\n")
    start_time = time.time()
    success = 0

    for i, (_, rel_path) in enumerate(file_list, start=1):
        print(f"📦 [{i}/{total_files}] Menambahkan: {rel_path} ... ", end="")
        try:
            subprocess.run(["rar", "a", "-m5", "-ep1", rar_file_path, rel_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print("OK")
            success += 1
        except subprocess.CalledProcessError:
            print("GAGAL")

    os.chdir("/content")
    duration = format_duration(time.time() - start_time)

    if os.path.exists(rar_file_path):
        rar_size = os.path.getsize(rar_file_path)
        print_result_success("Kompresi selesai:", rar_file_name, rar_size, jumlah=f"{success}/{total_files}", durasi=duration)
    else:
        print("❌ Gagal membuat file RAR!")
