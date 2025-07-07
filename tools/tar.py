import os
import tarfile
import time
from tools.status import TEXT, format_duration, print_summary, print_result_success

def tar_folder(input_path, output_path, method="gz"):
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

    ext = ".tar.gz" if method == "gz" else ".tar.xz" if method == "xz" else ".tar"
    tar_path = f"{output_path}{ext}"
    archive_name = os.path.basename(tar_path)

    print_summary("Ringkasan File/Folder:", total_files, total_size,
                  f"{'Nama file TAR':<17}: {archive_name}", tar_path)

    print("🚀 Memulai proses kompresi...\n")
    start_time = time.time()

    mode = "w:gz" if method == "gz" else "w:xz" if method == "xz" else "w"

    success = 0
    try:
        with tarfile.open(tar_path, mode) as tarf:
            for i, (abs_path, rel_path) in enumerate(file_list, start=1):
                print(f"📦 [{i}/{total_files}] Menambahkan: {rel_path} ... ", end="")
                try:
                    tarf.add(abs_path, arcname=rel_path)
                    print("OK")
                    success += 1
                except Exception as e:
                    print(f"GAGAL ({str(e)})")
    except Exception as e:
        print(f"❌ Gagal membuat file TAR: {e}")
        return

    duration = format_duration(time.time() - start_time)

    if os.path.exists(tar_path):
        size = os.path.getsize(tar_path)
        print_result_success("Kompresi selesai:", archive_name, size, jumlah=f"{success}/{total_files}", durasi=duration)
    else:
        print("❌ File TAR tidak ditemukan setelah proses selesai.")
