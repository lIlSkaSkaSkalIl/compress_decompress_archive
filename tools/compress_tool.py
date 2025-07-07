import os
import zipfile
import subprocess
import time

def format_size(size_bytes): for unit in ['B', 'KB', 'MB', 'GB', 'TB']: if size_bytes < 1024: return f"{size_bytes:.2f} {unit}" size_bytes /= 1024 return f"{size_bytes:.2f} PB"

def format_duration(seconds): minutes, sec = divmod(int(seconds), 60) return f"{minutes} menit {sec} detik" if minutes else f"{sec} detik"

def run_tool(metode, input_path, output_path): print(f"\n📦 Metode yang dipilih: {metode.upper()}")

if metode == "zip":
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Path tidak ditemukan: {input_path}")

    total_files = 0
    total_size = 0
    file_list = []

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

    print("📊 Ringkasan File/Folder:")
    print(f"╭📁 Jumlah file      : {total_files}")
    print(f"├💾 Total ukuran     : {format_size(total_size)}")
    print(f"├📦 Nama file ZIP    : {zip_file_name}")
    print(f"╰🎯 Lokasi output    : {zip_file_path}\n")

    print("🚀 Memulai proses kompresi...\n")
    start_time = time.time()

    with zipfile.ZipFile(zip_file_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
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
        print(f"\n✅ Kompresi selesai:")
        print(f"╭📦 Nama file ZIP    : {zip_file_name}")
        print(f"├📏 Ukuran file ZIP  : {format_size(zip_size)}")
        print(f"╰⏱️ Durasi proses    : {duration}")
    else:
        print("❌ Gagal membuat file ZIP!")

elif metode == "unzip":
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"ZIP file tidak ditemukan: {input_path}")

    zip_file_name = os.path.basename(input_path)
    zip_file_size = os.path.getsize(input_path)
    print("📊 Informasi File ZIP:")
    print(f"╭📦 Nama file ZIP     : {zip_file_name}")
    print(f"├📏 Ukuran file ZIP   : {format_size(zip_file_size)}")
    print(f"╰📂 Lokasi output     : {output_path}\n")

    os.makedirs(output_path, exist_ok=True)

    print("🚀 Memulai proses ekstraksi...\n")
    start_time = time.time()
    extracted_files = 0

    with zipfile.ZipFile(input_path, 'r') as zip_ref:
        members = zip_ref.namelist()
        total_files = len([m for m in members if not m.endswith("/")])
        for i, member in enumerate(members, start=1):
            if member.endswith("/"): continue
            print(f"📂 [{extracted_files+1}/{total_files}] Mengekstrak: {member} ... ", end="")
            try:
                zip_ref.extract(member, path=output_path)
                print("OK")
                extracted_files += 1
            except Exception as e:
                print(f"GAGAL ({str(e)})")

    duration = format_duration(time.time() - start_time)
    if extracted_files > 0:
        print(f"\n✅ Ekstraksi selesai:")
        print(f"╭📂 Jumlah file       : {extracted_files}")
        print(f"╰⏱️ Durasi proses     : {duration}")
    else:
        print(f"\n❌ Tidak ada file yang berhasil diekstrak!")

elif metode == "rar":
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Path tidak ditemukan: {input_path}")
    subprocess.run(["apt-get", "install", "rar", "-y"], stdout=subprocess.DEVNULL)

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

    print("📊 Ringkasan File/Folder:")
    print(f"╭📁 Jumlah file      : {total_files}")
    print(f"├💾 Total ukuran     : {format_size(total_size)}")
    print(f"├📦 Nama file RAR    : {rar_file_name}")
    print(f"╰🎯 Lokasi output    : {rar_file_path}\n")

    os.chdir(os.path.dirname(input_path))
    start_time = time.time()
    success = 0
    for i, (abs_path, rel_path) in enumerate(file_list, start=1):
        print(f"📦 [{i}/{total_files}] Menambahkan: {rel_path} ... ", end="")
        try:
            subprocess.run(["rar", "a", "-ep1", rar_file_path, rel_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print("OK")
            success += 1
        except subprocess.CalledProcessError:
            print("GAGAL")
    os.chdir("/content")

    duration = format_duration(time.time() - start_time)
    if os.path.exists(rar_file_path):
        rar_size = os.path.getsize(rar_file_path)
        print(f"\n✅ Kompresi selesai:")
        print(f"╭📦 Nama file RAR    : {rar_file_name}")
        print(f"├📏 Ukuran file RAR  : {format_size(rar_size)}")
        print(f"├📄 Jumlah sukses    : {success}/{total_files}")
        print(f"╰⏱️ Durasi proses    : {duration}")
    else:
        print("❌ Gagal membuat file RAR!")

elif metode == "unrar":
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"RAR file tidak ditemukan: {input_path}")
    subprocess.run(["apt-get", "install", "unrar", "-y"], stdout=subprocess.DEVNULL)

    rar_file_name = os.path.basename(input_path)
    rar_file_size = os.path.getsize(input_path)
    print("📊 Informasi File RAR:")
    print(f"╭📦 Nama file RAR     : {rar_file_name}")
    print(f"├📏 Ukuran file RAR   : {format_size(rar_file_size)}")
    print(f"╰📂 Lokasi output     : {output_path}\n")

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
        print(f"\n✅ Ekstraksi selesai:")
        print(f"╭📂 Jumlah file       : {extracted_files}")
        print(f"╰⏱️ Durasi proses     : {duration}")
    else:
        print("❌ Tidak ada file yang berhasil diekstrak.")

