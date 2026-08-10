import mysql.connector

class DatabaseMySQL:
    def __init__(self):
        self._host = "localhost"
        self._user = "rafan"
        self._password = "rafan030407"
        self._database = "db_absensi"
        self._conn = self._koneksi_db()
    

    def _koneksi_db(self):
        return mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database
        )

    def _buat_tabel_jika_belum_ada(self):
        cursor = self._conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS karyawan (
                id_karyawan VARCHAR(10) PRIMARY KEY,
                nama VARCHAR(100) NOT NULL,
                tipe VARCHAR(50) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS log_absensi (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tanggal DATE NOT NULL,
                waktu TIME NOT NULL,
                id_karyawan VARCHAR(10),
                nama VARCHAR(100),
                tipe VARCHAR(50),
                FOREIGN KEY (id_karyawan) REFERENCES karyawan(id_karyawan)
            )
        """)
        self._conn.commit()
        cursor.close()

    def simpan_karyawan(self, objek_karyawan):
        data = objek_karyawan.to_dict()
        cursor = self._conn.cursor()
        sql = "INSERT INTO karyawan (id_karyawan, nama, tipe) VALUES (%s, %s, %s)"
        val = (data['id_karyawan'], data['nama'], data['tipe'])
        try:
            cursor.execute(sql, val)
            self._conn.commit()
            print("Data Karyawan berhasil disimpan ke Database!")
        except mysql.connector.IntegrityError:
            print("ERROR: ID Karyawan sudah terdaftar di database!")
        finally:
            cursor.close()

    def ambil_semua_data(self):
        cursor = self._conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM karyawan")
        hasil = cursor.fetchall()
        cursor.close()
        return hasil
        
    def hapus_karyawan(self, id_karyawan):
        """Menghapus data karyawan beserta riwayat absennya dari Database"""
        cursor = self._conn.cursor()
        try:
            cursor.execute("DELETE FROM log_absensi WHERE id_karyawan = %s", (id_karyawan,))
            cursor.execute("DELETE FROM karyawan WHERE id_karyawan = %s", (id_karyawan,))
            self._conn.commit()
            return cursor.rowcount 
        except Exception as e:
            print(f"[-] ERROR DB: {e}")
            return 0
        finally:
            cursor.close()

    def simpan_absen(self, id_karyawan, nama, tipe, waktu, tanggal):
        cursor = self._conn.cursor()
        sql = "INSERT INTO log_absensi (tanggal, waktu, id_karyawan, nama, tipe) VALUES (%s, %s, %s, %s, %s)"
        val = (tanggal, waktu, id_karyawan, nama, tipe)
        cursor.execute(sql, val)
        self._conn.commit()
        cursor.close()

    def ambil_log_tanggal(self, tanggal):
        cursor = self._conn.cursor(dictionary=True)
        sql = "SELECT * FROM log_absensi WHERE tanggal = %s"
        cursor.execute(sql, (tanggal,))
        hasil = cursor.fetchall()
        cursor.close()
        return hasil
        
    def ambil_rekap_absensi(self, id_karyawan, hari_mundur):
        """Menghitung total kehadiran Dari Database"""
        cursor = self._conn.cursor(dictionary=True)
        sql = """
            SELECT COUNT(*) as total_hadir 
            FROM log_absensi 
            WHERE id_karyawan = %s AND tanggal >= DATE_SUB(CURDATE(), INTERVAL %s DAY)
        """
        cursor.execute(sql, (id_karyawan, hari_mundur))
        hasil = cursor.fetchone()
        cursor.close()
        return hasil['total_hadir']