import os
import zipfile
import time
from tools.status import TEXT, format_duration, print_summary, print_result_success

def zip_folder(input_path, output_path):
    total_files, total_size, file_list = 0, 0, []

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Path tidak ditemukan: {input_path}")

    if os.path.isfile(input_path):
        total_files = 1
        total_size = os.path.getsize(input_path)
        file_list.append((input_path, os.path.basename(input_path)))
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

    zip_file_path = f"{output_path}.zip"
    zip_file_name = os.path.basename(zip_file_path)

    print_summary("Ringkasan File/Folder:", total_files, total_size,
                  f"{TEXT['nama_file_zip']:<17}: {zip_file_name}", zip_file_path)

    print("🚀 Memulai proses kompresi...\n")
    start_time = time.time()

    with zipfile.ZipFile(zip_file_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for i, (abs_path, rel_path) in enumerate(file_list, start=1):
            print(f"📦 [{i}/{total_files}] Menambahkan: {rel_path} ... ", end="")
            try:
                zipf.write(abs_path, arcname=rel_path)
                print("OK")
            except Exception as e:
                print(f"GAGAL ({str(e)})")

    duration = format_duration(time.time() - start_time)
    if os.path.exists(zip_file_path):
        zip_size = os.path.getsize(zip_file_path)
        print_result_success("Kompresi selesai:", zip_file_name, zip_size, durasi=duration)
    else:
        print("❌ Gagal membuat file ZIP!")
