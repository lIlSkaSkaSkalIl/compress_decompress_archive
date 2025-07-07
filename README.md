# 📦 compress_decompress_archive

Alat bantu untuk kompresi dan dekompresi file/folder di Google Colab menggunakan format ZIP dan RAR.

Mendukung:
- ✅ ZIP (kompres)
- ✅ UNZIP (ekstrak)
- ✅ RAR (kompres)
- ✅ UNRAR (ekstrak)

---

## 🚀 Cara Penggunaan di Google Colab

### 1️⃣ Cell Pertama: Clone Repo & Setup

```python
# @title 🔧 Setup Tools

# Clone repo (jika belum)
!git clone https://github.com/lIlSkaSkaSkalIl/compress_decompress_archive.git || echo "Repo sudah ada"

# Tambahkan folder tools ke sys.path agar bisa di-import
import sys
sys.path.append("/content/compress_decompress_archive/tools")

# Import fungsi utama
from compress_tool import run_tool
```

---

### 2️⃣ Cell Kedua: Pilih Metode & Jalankan

```python
# @title ⚙️ Jalankan Kompres / Ekstrak

# 👉 Pilihan metode: zip, unzip, rar, unrar
metode = "zip"  # @param ["zip", "unzip", "rar", "unrar"]

# 👉 Masukkan path file/folder input & output
input_path = "/content/drive/MyDrive/contoh_folder"  # @param {type:"string"}
output_path = "/content/drive/MyDrive/hasil_kompres"  # @param {type:"string"}

# 🚀 Jalankan
run_tool(metode, input_path, output_path)
```

---

## 📂 Struktur Direktori

```
compress_decompress_archive/
├── tools/
│   ├── compress_tool.py
│   ├── rar.py
│   ├── unrar.py
│   ├── zip.py
│   ├── unzip.py
│   └── status.py
└── README.md
```

---

## ✅ Fitur

- Tampilan progres setiap file [✔]
- Ringkasan sebelum & sesudah proses [✔]
- Output format rapi dan informatif [✔]
- Tanpa library eksternal tambahan [✔]

---

## 💡 Contoh Output di Colab

```
📦 Metode yang dipilih: ZIP
📊 Ringkasan File/Folder:
╭📁 Jumlah file      : 12
├💾 Total ukuran     : 534.25 MB
├📦 Nama file ZIP    : hasil.zip
╰🎯 Lokasi output    : /content/hasil.zip

📦 [1/12] Menambahkan: file1.mkv ... OK
📦 [2/12] Menambahkan: file2.mkv ... OK
...

✅ Kompresi selesai:
╭📦 Nama file         : hasil.zip
├📏 Ukuran file       : 517.88 MB
╰⏱️ Durasi proses     : 13 detik
```

---

## 📬 Kontak

Dibuat oleh: [Ska RegGae](https://github.com/lIlSkaSkaSkalIl)

Silakan gunakan dan modifikasi sesuai kebutuhan.
