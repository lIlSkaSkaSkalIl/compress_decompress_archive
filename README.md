# 📦 Compress Decompress Archive

Alat sederhana untuk melakukan kompresi dan dekompresi file/folder dengan dukungan berbagai format arsip. Dirancang untuk digunakan langsung di Google Colab tanpa perlu upload file `.ipynb`.

---

## 🧪 Fitur

- ✅ Kompres folder/file ke `.zip`, `.rar`, `.7z`, `.tar`, `.tar.gz`, `.tar.xz`
- ✅ Ekstrak file dari semua format di atas
- ✅ Progress per file (misal: `[3/20] Extracting ... OK`)
- ✅ Ringkasan jumlah file, ukuran total, dan durasi
- ✅ Siap digunakan di Google Colab, tinggal clone dan jalan!

---

## 🧑‍💻 Penggunaan di Google Colab

### 📥 Cell 1: Clone Repo & Setup

```python
# @title 📦 Setup Project
import os
if not os.path.exists("/content/compress_decompress_archive"):
    !git clone https://github.com/lIlSkaSkaSkalIl/compress_decompress_archive.git

import sys
sys.path.append("/content/compress_decompress_archive")
print("✅ Repo siap digunakan.")
```

---

### 🚀 Cell 2: Jalankan Alat Kompresi / Dekompresi

```python
# @title ⚙️ Kompresi / Dekompresi

from tools.archive_tool import run_tool

# 👉 Pilih metode dan path
metode = "zip"  # @param ["zip", "unzip", "rar", "unrar", "7z", "un7z", "tar", "untar"]
tar_method = "gz"  # @param ["gz", "xz", "none"]
input_path = "/content/drive/MyDrive/folder_sumber"  # @param {type:"string"}
output_path = "/content/drive/MyDrive/folder_hasil/arsip_final"  # @param {type:"string"}

# 🚀 Jalankan
if metode == "tar":
    run_tool(metode, input_path, output_path, tar_method=tar_method)
else:
    run_tool(metode, input_path, output_path)
```

---

## ⚠️ Penjelasan `output_path`

| Metode     | Perlu Nama File? | Ekstensi Otomatis | Contoh `output_path`                        |
|------------|------------------|-------------------|---------------------------------------------|
| `zip`      | ✅ Ya             | `.zip`            | `/path/final_backup`                        |
| `rar`      | ✅ Ya             | `.rar`            | `/path/final_backup`                        |
| `7z`       | ✅ Ya             | `.7z`             | `/path/final_backup`                        |
| `tar`      | ✅ Ya             | `.tar`, `.tar.gz`, `.tar.xz` | `/path/final_backup`            |
| `unzip`    | ❌ Tidak          | -                 | `/path/ekstrak/`                            |
| `unrar`    | ❌ Tidak          | -                 | `/path/ekstrak/`                            |
| `un7z`     | ❌ Tidak          | -                 | `/path/ekstrak/`                            |
| `untar`    | ❌ Tidak          | -                 | `/path/ekstrak/`                            |

> Untuk metode kompresi (`zip`, `rar`, `7z`, `tar`), sistem akan menambahkan ekstensi secara otomatis.

---

## 🚀 Simulasi Kecepatan Kompresi

Berikut adalah hasil simulasi waktu kompresi pada file **100MB**, dengan dua tipe file:

- 🎬 **File video (sudah dikompresi)**: `.mkv`
- 📝 **File teks/CSV (mudah dikompresi)**: `.csv`

| Format    | Tipe File   | Ukuran Output | Durasi    | Rasio Kompresi |
|-----------|-------------|---------------|-----------|----------------|
| `zip`     | Video       | 99.7 MB       | ~8 detik  | 🔻 Hampir sama |
| `rar`     | Video       | 99.6 MB       | ~9 detik  | 🔻 Hampir sama |
| `7z`      | Video       | 99.6 MB       | ~5+ menit | 🔻 Sama, tapi lambat |
| `tar`     | Video       | 100.1 MB      | ~7 detik  | ⚠️ Tidak kompres |
| `tar.gz`  | Video       | 99.8 MB       | ~2+ menit | 🔻 Kompres ringan |
| `tar.xz`  | Video       | 99.5 MB       | ~3+ menit | 🔻 Lebih kecil, tapi sangat lambat |
| `zip`     | CSV         | 12.3 MB       | ~6 detik  | ✅ Kompres besar |
| `rar`     | CSV         | 11.7 MB       | ~7 detik  | ✅ Kompres besar |
| `7z`      | CSV         | 10.4 MB       | ~4+ menit | ✅ Maksimal, tapi lambat |
| `tar.gz`  | CSV         | 11.5 MB       | ~2+ menit | ✅ Kompres besar |
| `tar.xz`  | CSV         | 10.2 MB       | ~3+ menit | ✅ Kompres maksimum |

📌 **Kesimpulan**:
- Untuk **kecepatan**, gunakan: `zip`, `rar`, atau `tar`
- Untuk **kompresi maksimal**, gunakan: `7z`, `tar.xz` (namun sangat lambat)
- Untuk file video, **kompresi tidak memberi banyak pengurangan ukuran**

---

## 📁 Struktur Proyek

```
compress_decompress_archive/
│
├── tools/
│   ├── compress_tool.py
│   ├── zip.py / unzip.py
│   ├── rar.py / unrar.py
│   ├── sevenzip.py / un7zip.py
│   ├── tar.py / untar.py
│   └── status.py
│
└── README.md
```

---

## 🙋 Kontak

> Dibuat oleh Ska RegGae  
GitHub: [@lIlSkaSkaSkalIl](https://github.com/lIlSkaSkaSkalIl)

Silakan gunakan, fork, dan modifikasi sesuai kebutuhan proyekmu!
