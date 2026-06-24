class NilaiMahasiswa:
    def __init__(self, nama, nim, ipk, prodi):
        self.nama  = nama
        self.nim   = nim
        self.ipk   = ipk
        self.prodi = prodi

    def __str__(self):
        return (f"Nama  : {self.nama}\n"
                f"NIM   : {self.nim}\n"
                f"Prodi : {self.prodi}\n"
                f"IPK   : {self.ipk:.2f}")

    def __eq__(self, other):
        return self.ipk == other.ipk# ==

    def __lt__(self, other):
        return self.ipk < other.ipk# 

    def __gt__(self, other):
        return self.ipk > other.ipk# >

    def __le__(self, other):
        return self.ipk <= other.ipk# <=

    def __ge__(self, other):
        return self.ipk >= other.ipk# >=


# ── Instansiasi 3 objek mahasiswa ────────────────
mhs1 = NilaiMahasiswa("Sugeng Bapaknya Zaki",  "462025611078", 3.6, "Teknik Informatika")
mhs2 = NilaiMahasiswa("Jono Bapaknya Deri",    "462025611088", 3.5, "Teknik Informatika")
mhs3 = NilaiMahasiswa("Rahmat Bapaknya Kiki",  "462025611098", 3.8, "Teknik Informatika")

# ── Uji __str__ ──────────────────────────────────
print("=" * 35)
print("DATA MAHASISWA")
print("=" * 35)

print(mhs1)
print("-" * 35)
print(mhs2)
print("-" * 35)
print(mhs3)
print("=" * 35)

# ── Uji perbandingan ─────────────────────────────
print("\n=== HASIL PERBANDINGAN IPK ===")
print(f"Apakah Rafan  >  Sugeng?  {mhs1 > mhs2}")   
print(f"Apakah Sugeng <  Jono?    {mhs2 < mhs3}")   
print(f"Apakah Rafan  == Sugeng?  {mhs1 == mhs2}")  
print(f"Apakah Sugeng >= Jono?    {mhs2 >= mhs3}")  
print(f"Apakah Jono   <= Rafan?   {mhs3 <= mhs1}")  