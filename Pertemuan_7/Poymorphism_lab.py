# --- PARENT CLASS ---
class AlatPembayaran:

    def proses_bayar(self, nominal):
        print(f"[Base] Memproses pembayaran (Generic): Rp {nominal}")

# --- CHILD CLASS 1 (Method Overriding) ---
class KartuKredit(AlatPembayaran):
    """
    Child Class 1: KartuKredit.
    Meng-override method proses_bayar dengan logika spesifik banking.
    """
    def proses_bayar(self, nominal):
        print(f"[Kartu Kredit] - Memasukkan kartu ke mesin...")
        print(f"[Kartu Kredit] - Validasi PIN & Limit...")
        print(f"*** TRANSAKSI BERHASIL *** via Kartu Kredit: Rp {nominal}")

# --- CHILD CLASS 2 (Method Overriding) ---
class EWallet(AlatPembayaran):
    """
    Child Class 2: EWallet.
    Meng-override method proses_bayar dengan logika spesifik QR Code.
    """
    def proses_bayar(self, nominal):
        print(f"[EWallet] - Membuka aplikasi...")
        print(f"[EWallet] - Scan QR Code Merchant...")
        print(f"*** TRANSAKSI BERHASIL *** via Dompet Digital (EWallet): Rp {nominal}")
def jalankan_transaksi(objek_pembayaran, nominal):
    """
    Fungsi standalone untuk mendemonstrasikan Duck Typing.
    Fungsi ini tidak peduli objek_pembayaran itu turunan dari class apa.
    Asalkan objek tersebut memiliki method 'proses_bayar', maka fungsi ini akan menjalankannya.
    
    "If it walks like a duck and quacks like a duck, it's a duck."
    """
    print("--- Memulai Transaksi via Fungsi Universal ---")
    objek_pembayaran.proses_bayar(nominal)
    print("--- Transaksi Selesai ---\n")

# --- MAIN DEMONSTRATION ---
if __name__ == "__main__":
    # 1. Membuat objek dari class yang berbeda
    alat_generic = AlatPembayaran()
    kartu_saya = KartuKredit()
    dompet_digital = EWallet()

    # 2. Memanggil method secara langsung (Polymorphism via Inheritance)
    print(">>> Pemanggilan Langsung (.proses_bayar):")
    print("Dengan Objek Generic:")
    alat_generic.proses_bayar(50000)
    
    print("\nDengan Objek Kartu Kredit (Override):")
    kartu_saya.proses_bayar(150000)
    
    print("\nDengan Objek EWallet (Override):")
    dompet_digital.proses_bayar(75000)

    # 3. Memanggil fungsi Duck Typing (Jalan polymorphism tanpa herediter)
    print("\n" + "="*50)
    print(">>> Pemanggilan Menggunakan Fungsi Duck Typing:")
    
    # Kita passing semua object ke fungsi yang sama
    jalankan_transaksi(alat_generic, 10000)
    jalankan_transaksi(kartu_saya, 200000)
    jalankan_transaksi(dompet_digital, 5000)