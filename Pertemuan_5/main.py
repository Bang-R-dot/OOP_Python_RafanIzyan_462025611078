class Saldo:
  
    def __init__(self, pemilik, id_pengguna, pin_awal, saldo_awal):
        """
        Inisialisasi objek dengan 3 Private Attributes.
        """
        self.__id_pengguna = id_pengguna
        self.__pin = pin_awal
        self.__saldo_rahasia = saldo_awal
        self.pemilik = pemilik

    def get_id_pengguna(self):
        """
        METODE GETTER:
        Mengambil ID Pengguna yang bersifat privat secara terkontrol.
        """
        return self.__id_pengguna

    def lihat_saldo(self, input_pin):
        """
        METODE VALIDASI:
        Hanya mengizinkan akses ke data __saldo_rahasia jika PIN yang dimasukkan benar.
        """
        if input_pin == self.__pin:
            print(f"Verifikasi Berhasil. Saldo {self.pemilik}: Rp{self.__saldo_rahasia}")
        else:
            print("Peringatan: PIN salah! Akses ke data saldo ditolak.")

    def tarik_tunai(self, jumlah, input_pin):
        """
        METODE VALIDASI & MODIFIKASI:
        Memeriksa keamanan sebelum mengurangi nilai pada atribut privat __saldo_rahasia.
        """
        if input_pin == self.__pin:
            if jumlah <= self.__saldo_rahasia:
                self.__saldo_rahasia -= jumlah
                print(f"Berhasil menarik Rp{jumlah}. Sisa saldo: Rp{self.__saldo_rahasia}")
            else:
                print("Saldo tidak mencukupi.")
        else:
            print("Gagal: PIN salah. Transaksi dibatalkan.")

"""
BAGIAN PENGUJIAN (INSTANSIASI OBJEK)
"""

""" Pembuatan Object Baru """
akun_rafan = Saldo("RAFAN IZYAN MAAZ", "462025611078", "090807", 1000000)

print(f"--- Sistem Keamanan Saldo: {akun_rafan.pemilik} ---")

""" 
BUKTI PROTEKSI DATA:
Jika baris di bawah ini dijalankan, maka akan terjadi AttributeError.
Data __saldo_rahasia tidak bisa dipanggil langsung dari luar kelas.
"""
# print(akun_rafan.__saldo_rahasia) 

""" Menjalankan Fungsi Validasi dengan PIN yang Salah """
print("\n[Mencoba akses dengan PIN salah]")
akun_rafan.lihat_saldo("123456")

""" Menjalankan Fungsi Validasi dengan PIN yang Benar """
print("\n[Mencoba akses dengan PIN benar]")
akun_rafan.lihat_saldo("090807")

""" Mencoba melakukan transaksi tarik tunai """
print("\n[Mencoba transaksi tarik tunai]")
akun_rafan.tarik_tunai(250000, "090807")