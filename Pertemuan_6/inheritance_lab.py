# Tugas 6 - Inheritance dan Diamond Problem
# Nama: Rafan Izyan Maaz
# NIM: 462025611078
# Tema: Sistem Manajemen Karyawan Universitas

# ===== DEMONSTRASI DIAMOND PROBLEM DENGAN MRO =====

# Kelas Parent/Base (Puncak Diamond)
class Karyawan:
    """Kelas dasar untuk semua karyawan universitas"""
    
    def __init__(self, nama, nik, gaji_pokok):
        self.nama = nama
        self.nik = nik
        self.gaji_pokok = gaji_pokok
        print(f"[Karyawan] Inisialisasi: {nama}")
    
    def hitung_gaji(self):
        return self.gaji_pokok
    
    def daftar_kehadiran(self):
        return f"{self.nama} telah absen hari ini"
    
    def info_karyawan(self):
        return f"Nama: {self.nama}\nNIK: {self.nik}\nGaji: Rp {self.hitung_gaji():,}"


# Kelas Left Parent (Sisi Kiri Diamond)
class Pengajar(Karyawan):
    """Kelas untuk karyawan yang mengajar"""
    
    def __init__(self, nama, nik, gaji_pokok, matkul_diampu, jam_mengajar):
        super().__init__(nama, nik, gaji_pokok)
        self.matkul_diampu = matkul_diampu
        self.jam_mengajar = jam_mengajar
        print(f"[Pengajar] Inisialisasi: {nama}")
    
    def hitung_gaji(self):
        # Gaji dasar + tunjangan mengajar (Rp 100,000 per jam)
        tunjangan = self.jam_mengajar * 100000
        return super().hitung_gaji() + tunjangan
    
    def siapkan_materi(self):
        return f"{self.nama} sedang menyiapkan materi untuk {self.matkul_diampu}"


# Kelas Right Parent (Sisi Kanan Diamond)
class Administrator(Karyawan):
    """Kelas untuk karyawan administratif"""
    
    def __init__(self, nama, nik, gaji_pokok, departemen, tanggung_jawab):
        super().__init__(nama, nik, gaji_pokok)
        self.departemen = departemen
        self.tanggung_jawab = tanggung_jawab
        print(f"[Administrator] Inisialisasi: {nama}")
    
    def hitung_gaji(self):
        # Gaji dasar + tunjangan administratif (Rp 500,000)
        tunjangan = 500000
        return super().hitung_gaji() + tunjangan
    
    def proses_dokumen(self):
        return f"{self.nama} memproses dokumen untuk {self.departemen}"


# Kelas Child (Bawah Diamond) - DEMONSTRASI DIAMOND PROBLEM
class KaryawanMultitalenta(Pengajar, Administrator):
    """
    Kelas yang mewarisi dari dua parent sekaligus (Multiple Inheritance)
    Ini menciptakan DIAMOND PROBLEM!
    
    Diamond Pattern:
                Karyawan
               /        \
          Pengajar    Administrator
               \        /
           KaryawanMultitalenta
    
    Python mengatasi ini dengan MRO (Method Resolution Order)
    """
    
    def __init__(self, nama, nik, gaji_pokok, matkul_diampu, jam_mengajar, 
                 departemen, tanggung_jawab, spesialisasi):
        # Menggunakan super() untuk memanggil kedua parent secara berurutan
        super().__init__(nama, nik, gaji_pokok, matkul_diampu, jam_mengajar)
        # Inisialisasi atribut spesifik dari Administrator (yang tidak dipanggil super sebelumnya)
        self.departemen = departemen
        self.tanggung_jawab = tanggung_jawab
        self.spesialisasi = spesialisasi
        print(f"[KaryawanMultitalenta] Inisialisasi: {nama}\n")
    
    def hitung_gaji(self):
        """
        Hitung gaji dengan menggabungkan tunjangan dari kedua parent
        - Tunjangan mengajar: jam_mengajar * 100,000
        - Tunjangan administratif: 500,000
        - Tunjangan spesialisasi: 200,000
        """
        gaji_base = Karyawan.hitung_gaji(self)
        tunjangan_mengajar = self.jam_mengajar * 100000
        tunjangan_admin = 500000
        tunjangan_spesialisasi = 200000
        
        total = gaji_base + tunjangan_mengajar + tunjangan_admin + tunjangan_spesialisasi
        return total
    
    def pekerjaan_dual_role(self):
        """Menggabungkan pekerjaan dari kedua parent"""
        pekerjaan1 = self.siapkan_materi()
        pekerjaan2 = self.proses_dokumen()
        return f"{pekerjaan1}\n{pekerjaan2}"
    
    def info_karyawan(self):
        """Override metode parent untuk menampilkan info lengkap"""
        info_dasar = super().info_karyawan()
        info_tambahan = f"\nMata Kuliah: {self.matkul_diampu}\nDepartemen: {self.departemen}\nSpesialisasi: {self.spesialisasi}\nGaji Total: Rp {self.hitung_gaji():,}"
        return info_dasar + info_tambahan


# ===== PROGRAM UTAMA =====
if __name__ == "__main__":
    print("="*70)
    print("     SISTEM MANAJEMEN KARYAWAN UNIVERSITAS - INHERITANCE LAB")
    print("="*70)
    
    print("\n>>> TEST 1: SINGLE INHERITANCE (Pengajar) <<<\n")
    
    # Buat objek Pengajar
    pengajar1 = Pengajar(
        nama="Dr. Budi Santoso",
        nik="12345",
        gaji_pokok=5000000,
        matkul_diampu="Algoritma dan Struktur Data",
        jam_mengajar=12
    )
    
    print(pengajar1.info_karyawan())
    print(f"\nAktivitas: {pengajar1.siapkan_materi()}")
    print(f"Absensi: {pengajar1.daftar_kehadiran()}\n")
    
    print("\n" + "="*70)
    print("\n>>> TEST 2: SINGLE INHERITANCE (Administrator) <<<\n")
    
    # Buat objek Administrator
    admin1 = Administrator(
        nama="Siti Aminah",
        nik="12346",
        gaji_pokok=3500000,
        departemen="Akademik",
        tanggung_jawab="Pengelolaan KRS Mahasiswa"
    )
    
    print(admin1.info_karyawan())
    print(f"\nAktivitas: {admin1.proses_dokumen()}")
    print(f"Absensi: {admin1.daftar_kehadiran()}\n")
    
    print("\n" + "="*70)
    print("\n>>> TEST 3: MULTIPLE INHERITANCE (Diamond Problem) <<<\n")
    print("Demonstrasi Diamond Problem - Satu karyawan dengan dua peran:\n")
    
    # Buat objek KaryawanMultitalenta (Multiple Inheritance)
    multitalenta = KaryawanMultitalenta(
        nama="Ahmad Fauzi",
        nik="12347",
        gaji_pokok=4000000,
        matkul_diampu="Basis Data",
        jam_mengajar=8,
        departemen="Teknologi Informasi",
        tanggung_jawab="Koordinasi Lab Komputer",
        spesialisasi="Database Engineering"
    )
    
    print(multitalenta.info_karyawan())
    print(f"\nDual Role:\n{multitalenta.pekerjaan_dual_role()}")
    print(f"\nAbsensi: {multitalenta.daftar_kehadiran()}\n")
    
    print("\n" + "="*70)
    print("\n>>> TEST 4: METHOD RESOLUTION ORDER (MRO) <<<\n")
    print("MRO adalah urutan pencarian metode dalam Multiple Inheritance:")
    print(f"\nMRO untuk KaryawanMultitalenta:\n{KaryawanMultitalenta.__mro__}\n")
    
    # Tampilkan detail MRO
    print("Urutan MRO yang dapat dibaca:")
    for i, kelas in enumerate(KaryawanMultitalenta.__mro__, 1):
        print(f"{i}. {kelas.__name__}")
    
    print("\n" + "="*70)
    print("\n>>> TEST 5: PERBANDINGAN GAJI <<<\n")
    
    # Hitung dan tampilkan perbandingan gaji
    print(f"Gaji Pengajar: Rp {pengajar1.hitung_gaji():,}")
    print(f"Gaji Administrator: Rp {admin1.hitung_gaji():,}")
    print(f"Gaji Karyawan Multitalenta: Rp {multitalenta.hitung_gaji():,}")
    print(f"\nSelisih gaji multitalenta vs pengajar: Rp {(multitalenta.hitung_gaji() - pengajar1.hitung_gaji()):,}")
    print(f"Selisih gaji multitalenta vs administrator: Rp {(multitalenta.hitung_gaji() - admin1.hitung_gaji()):,}")
    
    print("\n" + "="*70)
    print("\n>>> TEST 6: DEMONSTRASI SUPER() DALAM MULTIPLE INHERITANCE <<<\n")
    print("super() dalam Multiple Inheritance mengikuti urutan MRO:")
    print(f"1. KaryawanMultitalenta.hitung_gaji() menggabungkan tunjangan dari:")
    print(f"   - Pengajar: jam_mengajar ({multitalenta.jam_mengajar}) × Rp 100,000 = Rp {multitalenta.jam_mengajar * 100000:,}")
    print(f"   - Administrator: tunjangan tetap = Rp 500,000")
    print(f"   - Spesialisasi: tunjangan = Rp 200,000")
    print(f"   - Gaji Pokok (dari Karyawan): Rp {multitalenta.gaji_pokok:,}")
    print(f"   - TOTAL: Rp {multitalenta.hitung_gaji():,}")
    
    print("\n" + "="*70)
    print("\nProgram selesai. Demonstrasi Diamond Problem berhasil! ✓")
    print("="*70)