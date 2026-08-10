import datetime
import os
from models import KaryawanTetap, KaryawanMagang, KaryawanHarian
from database import DatabaseMySQL
from exceptions import IDKaryawanTidakValidError, validasi_id

def bersihkan_layar():
    os.system('clear')

def cetak_header():
    print("=======================================")
    print(" SISTEM ABSENSI KARYAWAN - UNIDA GONTOR")
    print("    UNIDA GONTOR - INFORMATICS DEPT    ")
    print("=======================================")

def menu_admin(db):
    while True:
        bersihkan_layar()
        cetak_header()
        print("PAGE ADMIN")
        print("1.Tambah Data Karyawan")
        print("2.Lihat Data Karyawan")
        print("3.Hapus Data Karyawan")
        print("4.Laporan Absensi Harian")
        print("5.Laporan Rekap Sepekan")
        print("6.Laporan Rekap Sebulan")
        print("7.Keluar")
        
        pilihan = input("Pilihlah Angka (1-7): ")

        if pilihan == '1':
            print(""
            "-- TAMBAH KARYAWAN BARU --")
            print("KODE TIPE: 1 (Tetap), 2 (Magang), 3 (Harian)")
            tipe = input("Pilih Tipe (1/2/3): ")
            id_input = input("Masukkan ID (Contoh K001/K002/K003-01): ")
            nama = input("Masukkan Nama: ")
            
            try:
                validasi_id(id_input, tipe) 
                if tipe == '1': kry = KaryawanTetap(id_input, nama)
                elif tipe == '2': kry = KaryawanMagang(id_input, nama)
                elif tipe == '3': kry = KaryawanHarian(id_input, nama)
                else:
                    print("Tipe tidak valid.")
                    input("Tekan Enter untuk lanjut...")
                    continue
                
                db.simpan_karyawan(kry)
            except IDKaryawanTidakValidError as e:
                print(f"[-] Sistem Terjaga: {e}")
            input("Tekan Enter untuk lanjut...")

        elif pilihan == '2':
            print("-- DATA KARYAWAN --")
            data = db.ambil_semua_data()
            if not data:
                print("Data kosong.")
            else:
                print("-" * 55)
                print(f"| {'ID':<10} | {'NAMA':<20} | {'TIPE':<15} |")
                print("-" * 55)
                for k in data:
                    print(f"| {k['id_karyawan']:<10} | {k['nama']:<20} | {k['tipe']:<15} |")
                print("-" * 55)
            input("Tekan Enter untuk lanjut...")

        elif pilihan == '3':
            print("-- HAPUS DATA KARYAWAN --")
            id_hapus = input("Masukkan ID yang akan dihapus: ")
            baris = db.hapus_karyawan(id_hapus)
            if baris > 0:
                print(f"[+] Berhasil! Data karyawan {id_hapus} beserta riwayat absennya telah dihapus.")
            else:
                print("[-] Gagal. ID Karyawan tidak ditemukan di database.")
            input("Tekan Enter untuk lanjut...")

        elif pilihan == '4':
            tanggal_hari_ini = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"-- LAPORAN ABSENSI TANGGAL {tanggal_hari_ini} --")
            
            semua_karyawan = db.ambil_semua_data()
            log_hari_ini = db.ambil_log_tanggal(tanggal_hari_ini)
            id_yg_hadir = [log["id_karyawan"] for log in log_hari_ini]

            print("-" * 70)
            print(f"| {'ID':<10} | {'NAMA':<20} | {'WAKTU':<10} | {'STATUS':<15} |")
            print("-" * 70)
            
            for k in semua_karyawan:
                if k['id_karyawan'] in id_yg_hadir:
                    waktu = str(next(log["waktu"] for log in log_hari_ini if log["id_karyawan"] == k['id_karyawan']))
                    print(f"| {k['id_karyawan']:<10} | {k['nama']:<20} | {waktu:<10} | {'HADIR':<15} |")
                else:
                    print(f"| {k['id_karyawan']:<10} | {k['nama']:<20} | {'-':<10} | {'BOLOS':<15} |")
            print("-" * 70)
            input("Tekan Enter untuk lanjut...")
            
        elif pilihan in ['5', '6']:
            hari = 7 if pilihan == '5' else 30
            teks_waktu = "SEPEKAN" if pilihan == '5' else "SEBULAN"
            print(f"-- REKAP KEHADIRAN {teks_waktu} TERAKHIR --")
            
            semua_karyawan = db.ambil_semua_data()
            if not semua_karyawan:
                print("Data kosong.")
            else:
                print("-" * 65)
                print(f"| {'ID':<10} | {'NAMA':<20} | {'TOTAL HADIR':<12} | {'KET':<10} |")
                print("-" * 65)
                for k in semua_karyawan:
                    total = db.ambil_rekap_absensi(k['id_karyawan'], hari)
                    ket = "AKTIF" if total > 0 else "PASIF/NOL"
                    print(f"| {k['id_karyawan']:<10} | {k['nama']:<20} | {total:<12} | {ket:<10} |")
                print("-" * 65)
            input("Tekan Enter untuk lanjut...")

        elif pilihan == '7':
            break

def menu_pegawai(db):
    bersihkan_layar()
    cetak_header()
    print("TERMINAL ABSENSI PEGAWAI")
    id_absen = input("Silakan tap / masukkan ID Anda: ")
    
    tanggal_sekarang = datetime.datetime.now().strftime("%Y-%m-%d")
    waktu_sekarang = datetime.datetime.now().strftime("%H:%M:%S")
    
    data_karyawan = db.ambil_semua_data()
    ditemukan = False
    
    for k_dict in data_karyawan:
        if k_dict["id_karyawan"] == id_absen:
            ditemukan = True
            
            log_hari_ini = db.ambil_log_tanggal(tanggal_sekarang)
            if any(log["id_karyawan"] == id_absen for log in log_hari_ini):
                print(f"ERROR: {k_dict['nama']} sudah melakukan absensi hari ini!")
                break

            if k_dict["tipe"] == "KaryawanTetap": kry = KaryawanTetap(k_dict["id_karyawan"], k_dict["nama"])
            elif k_dict["tipe"] == "KaryawanMagang": kry = KaryawanMagang(k_dict["id_karyawan"], k_dict["nama"])
            elif k_dict["tipe"] == "KaryawanHarian": kry = KaryawanHarian(k_dict["id_karyawan"], k_dict["nama"])
            
            db.simpan_absen(k_dict["id_karyawan"], k_dict["nama"], k_dict["tipe"], waktu_sekarang, tanggal_sekarang)
            print(f"BERHASIL: {kry.catat_absensi(waktu_sekarang)}")
            break
            
    if not ditemukan:
        print("AKSES DITOLAK: ID Karyawan tidak terdaftar.")
        
    input("Tekan Enter untuk kembali...")

def main():
    db = DatabaseMySQL()
    while True:
        bersihkan_layar()
        cetak_header()
        print("LOGIN SEBAGAI:")
        print("1.Admin")
        print("2.Pegawai")
        print("3.Keluar")
        
        akses = input("Pilih (1-3): ")
        
        if akses == '1':
            password = input("Masukkan PIN Admin: ")
            if password == "030407":
                menu_admin(db)
            else:
                print("PIN Salah!")
                input("Tekan Enter untuk kembali...")
        elif akses == '2':
            menu_pegawai(db)
        elif akses == '3':
            bersihkan_layar()
            print("Sistem dimatikan.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

if __name__ == "__main__":
    main()