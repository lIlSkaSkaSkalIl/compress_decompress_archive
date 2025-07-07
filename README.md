
# 📦 Compress Decompress Archive

Alat sederhana untuk melakukan kompresi dan dekompresi file/folder dengan dukungan untuk format `.zip` dan `.rar`. Didesain untuk digunakan langsung di Google Colab.

---

## 🧪 Fitur

- ✅ Kompres folder/file ke `.zip` dan `.rar`
- ✅ Ekstrak file `.zip` dan `.rar`
- ✅ Progress ditampilkan (misal: `[3/20]`)
- ✅ Ringkasan jumlah file, ukuran, durasi
- ✅ Tidak perlu upload file `.ipynb`, cukup clone repo dan jalankan!

---

## 🧑‍💻 Penggunaan di Google Colab

### 📥 Cell 1: Clone Repo & Setup
```python
# @title 📦 Setup Project
!git clone https://github.com/lIlSkaSkaSkalIl/compress_decompress_archive.git || echo "Repo sudah ada"

import sys
sys.path.append("/content/compress_decompress_archive/tools")
```

### 🚀 Cell 2: Jalankan Alat
```python
# @title 🛠️ Jalankan Kompresi/Dekompresi
from compress_tool import run_tool

# Pilihan metode: "zip", "unzip", "rar", "unrar"
metode = "zip"  # @param ["zip", "unzip", "rar", "unrar"]

# Path input dan output
input_path = "/content/drive/MyDrive/folder_sumber"  # @param {type:"string"}
output_path = "/content/drive/MyDrive/folder_hasil/final"  # @param {type:"string"}

run_tool(metode, input_path, output_path)
```

---

## ⚠️ Penjelasan output_path

| Metode     | nama file? | Contoh output_path                                |
|------------|-------------------------------|----------------------------------------------------|
| `zip`      | ✅                          | `/content/drive/MyDrive/folder_hasil/arsip_final` |
| `rar`      | ✅                          | `/content/drive/MyDrive/folder_hasil/arsip_final` |
| `unzip`    | ❌                       | `/content/drive/MyDrive/folder_ekstrak`           |
| `unrar`    | ❌                       | `/content/drive/MyDrive/folder_ekstrak`           |

> Untuk metode `zip` dan `rar`, sistem akan menambahkan `.zip` atau `.rar` secara otomatis di belakang nama output yang Anda berikan.

---

## 🖨️ Contoh Output

```
📦 Metode yang dipilih: ZIP

📊 Ringkasan File/Folder:
╭📁 Jumlah file      : 15
├💾 Total ukuran     : 1.45 GB
├📦 Nama file ZIP    : arsip_final.zip
╰🎯 Lokasi output    : /content/drive/MyDrive/folder_hasil/arsip_final.zip

🚀 Memulai proses kompresi...

📦 [1/15] Menambahkan: file1.mkv ... OK
📦 [2/15] Menambahkan: file2.srt ... OK
...

✅ Kompresi selesai:
╭📦 Nama file         : arsip_final.zip
├📏 Ukuran file       : 1.12 GB
╰⏱️ Durasi proses     : 2 menit 45 detik
```

---

## 📁 Struktur Proyek

```
compress_decompress_archive/
│
├── tools/
│   ├── compress_tool.py
│   ├── zip.py
│   ├── unzip.py
│   ├── rar.py
│   ├── unrar.py
│   └── status.py
│
└── README.md
```

---

## 🙋 Kontak

> Dibuat oleh Ska RegGae  
GitHub: [@lIlSkaSkaSkalIl](https://github.com/lIlSkaSkaSkalIl)
