# Tugas 3 - OOP Advanced Methods
# Nama: Rafan Izyan Maaz
# NIM: 462025611078
# Tema: Sistem Manajemen Warung Kopi

class WarungKopi:
    """Class untuk mengelola data warung kopi"""
    
    total_warung = 0  # class variable
    
    def __init__(self, nama_warung, lokasi, jumlah_menu):
        self.nama_warung = nama_warung
        self.lokasi = lokasi
        self.jumlah_menu = jumlah_menu
        WarungKopi.total_warung += 1
    
    # Instance Method 1: menampilkan info warung
    def tampilkan_info(self):
        print("=" * 50)
        print(f"Nama Warung: {self.nama_warung}")
        print(f"Lokasi: {self.lokasi}")
        print(f"Jumlah Menu: {self.jumlah_menu}")
        print("=" * 50)
    
    # Instance Method 2: hitung estimasi pendapatan
    def hitung_pendapatan(self, harga_rata, tamu_per_hari):
        pendapatan = harga_rata * tamu_per_hari * 30  # per bulan
        print(f"Estimasi pendapatan bulanan {self.nama_warung}:")
        print(f"Rp {pendapatan:,.0f}")
        return pendapatan
    
    # Static Method: konversi rupiah ke dollar
    @staticmethod
    def konversi_rupiah_dollar(rupiah):
        kurs = 15000  # asumsi 1 USD = 15000 IDR
        dollar = rupiah / kurs
        print(f"Rp {rupiah:,.0f} = USD {dollar:,.2f}")
        return dollar
    
    # Static Method tambahan: cek jam operasional
    @staticmethod
    def cek_jam_buka(jam):
        if 6 <= jam <= 22:
            return "Warung sedang buka"
        else:
            return "Warung sedang tutup"


# Program utama
if __name__ == "__main__":
    print("\n>>> SISTEM MANAJEMEN WARUNG KOPI <<<\n")
    
    # Membuat objek warung pertama
    warung1 = WarungKopi("Kopi Mantap", "Siman", 15)
    warung1.tampilkan_info()
    pendapatan1 = warung1.hitung_pendapatan(20000, 50)
    
    print()
    
    # Membuat objek warung kedua
    warung2 = WarungKopi("Ngopi Yuk", "Mlarak", 20)
    warung2.tampilkan_info()
    pendapatan2 = warung2.hitung_pendapatan(25000, 40)
    
    print("\n" + "=" * 50)
    print("TESTING STATIC METHOD")
    print("=" * 50)
    
    # Memanggil static method lewat class
    print("\n1. Konversi lewat nama Class:")
    WarungKopi.konversi_rupiah_dollar(pendapatan1)
    
    # Memanggil static method lewat objek
    print("\n2. Konversi lewat objek:")
    warung2.konversi_rupiah_dollar(pendapatan2)
    
    # Testing static method lainnya
    print("\n3. Cek jam operasional:")
    print(f"Jam 10: {WarungKopi.cek_jam_buka(10)}")
    print(f"Jam 23: {warung1.cek_jam_buka(23)}")
    
    print(f"\nTotal warung yang terdaftar: {WarungKopi.total_warung}")
    print("\nProgram selesai.")