import os

TEXT = {
    "jumlah_file": "Jumlah file",
    "ukuran_total": "Total ukuran",
    "nama_file_zip": "Nama file ZIP",
    "nama_file_rar": "Nama file RAR",
    "lokasi_output": "Lokasi output",
    "durasi_proses": "Durasi proses",
    "jumlah_sukses": "Jumlah sukses",
    "jumlah_ekstrak": "Jumlah file",
    "nama_file": "Nama file",
    "ukuran_file": "Ukuran file",
}

def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def format_duration(seconds):
    minutes, sec = divmod(int(seconds), 60)
    return f"{minutes} menit {sec} detik" if minutes else f"{sec} detik"

def print_summary(title, jumlah_file, total_size, nama_file_line, output_path):
    print(f"📊 {title}")
    print(f"╭📁 {TEXT['jumlah_file']:<17}: {jumlah_file}")
    print(f"├💾 {TEXT['ukuran_total']:<17}: {format_size(total_size)}")
    print(f"├📦 {nama_file_line}")
    print(f"╰🎯 {TEXT['lokasi_output']:<17}: {output_path}\n")

def print_result_success(title, file_name, ukuran, jumlah=None, durasi=None):
    print(f"\n✅ {title}")
    print(f"╭📦 {TEXT['nama_file']:<17}: {file_name}")
    print(f"├📏 {TEXT['ukuran_file']:<17}: {format_size(ukuran)}")
    if jumlah is not None:
        print(f"├📄 {TEXT['jumlah_sukses']:<17}: {jumlah}")
    if durasi:
        print(f"╰⏱️ {TEXT['durasi_proses']:<17}: {durasi}")

def print_file_info(title, file_name, ukuran, output_path):
    print(f"📊 {title}")
    print(f"╭📦 {TEXT['nama_file']:<17}: {file_name}")
    print(f"├📏 {TEXT['ukuran_file']:<17}: {format_size(ukuran)}")
    print(f"╰📂 {TEXT['lokasi_output']:<17}: {output_path}\n")
