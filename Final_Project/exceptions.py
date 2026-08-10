import re
# Memanggil library bawaan python (Regular Expression) untuk mengecek pola teks

class IDKaryawanTidakValidError(Exception): # Class error yang di warisi (inheritance) sifat dari Exception
    def __init__(self, message="Format ID salah!"):
        self.message = message
        super().__init__(self.message)

def validasi_id(id_input, tipe):
# Mengecek apakah sesuai pilihan tipe yg dipilih
    if tipe == '1' and not re.match(r"^K001-\d{2}$", id_input):
        raise IDKaryawanTidakValidError("Pegawai TETAP wajib pakai awalan K001- (contoh: K001-01)")
    elif tipe == '2' and not re.match(r"^K002-\d{2}$", id_input):
        raise IDKaryawanTidakValidError("Pegawai MAGANG wajib pakai awalan K002- (contoh: K002-01)")
    elif tipe == '3' and not re.match(r"^K003-\d{2}$", id_input):
        raise IDKaryawanTidakValidError("Pegawai HARIAN wajib pakai awalan K003- (contoh: K003-01)")