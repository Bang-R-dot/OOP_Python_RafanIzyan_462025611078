# Final Project PBO - Sistem Absensi Karyawan CLI

Ini adalah repositori untuk tugas akhir (UAS) mata kuliah Pemrograman Berorientasi Objek. Aplikasi ini dibuat menggunakan Bahasa Pemrograman Python murni dengan antarmuka CLI (Command Line) yang sudah terhubung langsung ke database MySQL.

## Letak 4 Pilar OOP di Project Ini

Supaya lebih jelas,Berikut pemetaan konsep OOP yang digunakan di dalam kode:

1. Enkapsulasi:
   Data sensitif buat koneksi database (Seperti host, username, password) Saya sembunyiin pakai variabel *private/protected* di dalam file `database.py`. Jadi datanya aman dan nggak bisa dimanipulasi sembarangan dari file lain.
2. Inheritance (Pewarisan):
   Ada pemisahan class di `models.py`.Saya bikin class induk `Karyawan` yang mewariskan atribut dasar ke class anaknya (contoh: class Karyawan Tetap atau Kontrak).
3. Polimorfisme:
   Ada method yang namanya persis sama di class induk dan anak, tapi cara kerjanya beda. Misalnya method buat ngitung gaji atau logika potong absen yang disesuaikan sama tipe karyawannya.
4. Abstraksi:
   Di file `main.py`, alurnya dibikin simpel. Pemanggilan fungsi ke database tinggal panggil methodnya aja, jadi kerumitan query SQL dan logika di baliknya disembunyikan dari file utama.

## Cara Jalanin Program

Jika mau nyoba jalanin aplikasinya di lokal, ikutin step berikut:

1. Pastikan server MySQL (XAMPP/MAMP) sudah nyala.
2. Buka terminal dan arahin ke folder `Final_Project`.
3. Install terlebih dahulu modul konektornya supaya Python bisa ngobrol dengan database (MySQL) ketikan perintah berikut:
   `pip install mysql-connector-python`
4. Kalau sudah,tinggal eksekusi file utamanya:
   `python main.py`
