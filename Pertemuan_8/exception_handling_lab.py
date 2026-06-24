class NilaiTidakValidError(Exception):
    """Custom exception untuk nilai di luar rentang 0-100."""
    def __init__(self, nilai):
        super().__init__(f"Validasi gagal: Nilai {nilai} tidak masuk akal.Wajib antara 0 - 100.")

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai = 0

    def input_nilai(self, nilai_baru):
        if nilai_baru < 0 or nilai_baru > 100:
            raise NilaiTidakValidError(nilai_baru)
        self.nilai = nilai_baru
        print(f"Data valid. Nilai {self.nilai} berhasil diinput untuk {self.nama} ({self.nim}).")


if __name__ == "__main__":
    mhs = Mahasiswa("RAFAN IZYAN MAAZ", "462025611078")
    
    try:
        mhs.input_nilai(115) 
    except NilaiTidakValidError as e:
        print(f"Error Tertangkap: {e}")
    finally:
        print("Proses pemeriksaan data nilai telah selesai dilakukan.")