# Final Project PBO - Sistem Absensi Karyawan CLI

Ini adalah repositori untuk tugas akhir (UAS) mata kuliah Pemrograman Berorientasi Objek. Aplikasi ini dibikin pakai Python murni dengan antarmuka CLI (Command Line) dan udah terhubung langsung ke database MySQL.

## Letak 4 Pilar OOP di Project Ini

Biar jelas, ini pemetaan konsep OOP yang dipake di dalam kode:

1. Enkapsulasi:
   Data sensitif buat koneksi database (kayak host, username, password) gw sembunyiin pakai variabel *private/protected* di dalam file `database.py`. Jadi datanya aman dan nggak bisa dimanipulasi sembarangan dari file lain.
2. Inheritance (Pewarisan):
   Ada pemisahan class di `models.py`. Gw bikin class induk `Karyawan` yang mewariskan atribut dasar ke class anaknya (contoh: class Karyawan Tetap atau Kontrak).
3. Polimorfisme:
   Ada method yang namanya persis sama di class induk dan anak, tapi cara kerjanya beda. Misalnya method buat ngitung gaji atau logika potong absen yang disesuaikan sama tipe karyawannya.
4. Abstraksi:
   Di file `main.py`, alurnya dibikin simpel. Pemanggilan fungsi ke database tinggal panggil methodnya aja, jadi kerumitan query SQL dan logika di baliknya disembunyikan dari file utama.

## Cara Jalanin Program

Kalau mau nyoba jalanin aplikasinya di lokal, ikutin step ini:

1. Pastikan server MySQL (XAMPP/MAMP) udah nyala.
2. Buka terminal dan arahin ke folder `Final_Project`.
3. Install dulu modul konektornya biar Python bisa ngobrol sama MySQL:
   `pip install mysql-connector-python`
4. Kalau udah, tinggal eksekusi file utamanya:
   `python main.py`
