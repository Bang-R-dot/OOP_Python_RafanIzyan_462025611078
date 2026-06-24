class universitas:
    name = "Rafan Izyan Maaz"
    daerah = "Palembang"
    
    def perkenalan(self):
        print(f" Welcome To {self.nama} yang berada di daerah {self.daerah}")

    def muqaddimah(self, nama):
        print(f"Hallo {nama}! Welcome To {self.nama} yang berada di daerah {self.daerah}")
                      
class Mahasantri:
    pass

kampusA = universitas()
kampusB = universitas()

print(kampusA)
print(kampusB)

Mahasantri1 = Mahasantri()
Mahasantri1.name = "Rafan Izyan Maaz"
Mahasantri1.major = "Teknik Informatika"
Mahasantri1.nim = "462025611078" 

Mahasantri2 = Mahasantri()
Mahasantri2.name = "Sugeng"
Mahasantri2.major = "Manajemen"
Mahasantri2.nim = "462025123456" 

print(Mahasantri1.nim)
print(Mahasantri1.name)
print(Mahasantri1.major)

print(Mahasantri2.nim)
print(Mahasantri2.name)
print(Mahasantri2.major)

kampusA.nama = "UNIDA GONTOR"
kampusA.daerah = "Siman"

kampusB.nama = "UNIDA GONTOR"
kampusB.daerah = "Mlarak"

print(kampusA.nama)
print(kampusA.daerah)
print(kampusB.nama)
print(kampusB.daerah)

kampus= universitas()
kampus.nama = "Universitas Darussalam Gontor"
kampus.daerah = "Mlarak,Ponorogo"
kampus.perkenalan()

informasi= universitas()
informasi.nama = "Universitas Darussalam Gontor"
informasi.daerah = "Siman, Ponorogo"
informasi.muqaddimah("Rafan Izyan Maaz")