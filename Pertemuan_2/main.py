# Tugas 2 - Dasar OOP
# Nama: Rafan Izyan Maaz
# NIM: 462025611078
# Objek: Smartphone

class Smartphone:
    """Class untuk representasi smartphone"""
    
    def __init__(self, merk, tipe, ram, storage, harga):
        self.merk = merk
        self.tipe = tipe
        self.ram = ram
        self.storage = storage
        self.harga = harga
    
    def tampilkan_spesifikasi(self):
        """Method untuk menampilkan spesifikasi HP"""
        print(f"Merk: {self.merk}")
        print(f"Tipe: {self.tipe}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")
        print(f"Harga: Rp {self.harga:,}")


# Program utama
print("="*50)
print("DAFTAR SMARTPHONE")
print("="*50)

# Objek pertama
hp1 = Smartphone("Samsung", "Galaxy A54", 8, 256, 5500000)
print("\nSmartphone 1:")
hp1.tampilkan_spesifikasi()

# Objek kedua
hp2 = Smartphone("Xiaomi", "Redmi Note 12", 6, 128, 3200000)
print("\nSmartphone 2:")
hp2.tampilkan_spesifikasi()

print("\n" + "="*50)
print("Program selesai")
print("="*50)