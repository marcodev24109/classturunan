class Tempat:
    def Rumah1(self):
        print("Rumah yang sangat besar, Lantai 1.")
    def Rumah2(self):
        print("Rumah yang sangat besar, Lantai 2.")

class Lantai1(Tempat):
    def Ruang1(self):
        print("Ruang Tamu")

    def Ruang2(self):
        print("Ruang Keluarga")

    def Ruang3(self):
        print("Ruang Makan dan Dapur")

    def Ruang4(self):
        print("Kamar Utama")

    def Ruang5(self):
        print("Kamar Pembantu")

class Lantai2(Tempat):
    def Ruang1(self):
        print("Teras")

    def Ruang2(self):
        print("Kamar Tamu")

    def Ruang3(self):
        print("Kamar Anak Perempuan")

    def Ruang4(self):
        print("Kamar Anak Laki-laki")

    def Ruang5(self):
        print("Kamar Pembantu")


L1 = Lantai1()
L1.Rumah1()
L1.Ruang1()
L1.Ruang2()
L1.Ruang3()
L1.Ruang4()
L1.Ruang5()

L2 = Lantai2()
L2.Rumah2()
L2.Ruang1()
L2.Ruang2()
L2.Ruang3()
L2.Ruang4()
L2.Ruang5()