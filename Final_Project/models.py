from abc import ABC, abstractmethod

#Encapsulation#
class Karyawan(ABC):
    # Constructor/Titik awal sistem mengenali karyawan dengan id dan nama 
    def __init__(self, id_karyawan, nama):
        #Atribut protacted dengan tanda underscore (_) agar tidak bisa diakses langsung dari luar class
        self._id_karyawan = id_karyawan 
        self._nama = nama

    #Getter
    @property
    def id_karyawan(self):
        return self._id_karyawan
        
    @property
    def nama(self):
        return self._nama

#Abstraction#
    @abstractmethod
    def catat_absensi(self, jam_masuk):
        pass

    def to_dict(self):
        return {
            "id_karyawan": self._id_karyawan,
            "nama": self._nama,
            "tipe": self.__class__.__name__
        }

class KaryawanTetap(Karyawan):
    def catat_absensi(self, jam_masuk):
        return f"[{self._id_karyawan}] {self._nama} (TETAP) absen pukul {jam_masuk}.Data Sudah Masuk"

class KaryawanMagang(Karyawan):
    def catat_absensi(self, jam_masuk):
        return f"[{self._id_karyawan}] {self._nama} (MAGANG) absen pukul {jam_masuk}.Data Sudah Masuk"

class KaryawanHarian(Karyawan):
    def catat_absensi(self, jam_masuk):
        return f"[{self._id_karyawan}] {self._nama} (HARIAN) absen pukul {jam_masuk}.Data Sudah Masuk"