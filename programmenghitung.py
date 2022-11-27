

def lingkaran():
    print("\n---------------------------")
    print(" Menghitung Luas Lingkaran")
    print("---------------------------")
    r = int(input("Masukkan jari-jari : "))
    luas = 22/7 * r * r
    print("Luas Lingkaran : ", luas)
    tanya()

def persegi():
    print("\n---------------------------")
    print(" Menghitung Luas Persegi")
    print("---------------------------")
    s = int(input("Masukkan panjang sisi : "))
    luas = s * s
    print("Luas Persegi : ", luas)
    tanya()

def segitiga():
    print("\n---------------------------")
    print(" Menghitung Luas Segitiga")
    print("---------------------------")
    a = int(input("Masukkan alas : "))
    t = int(input("Masukkan tinggi : "))
    luas = 0.5 * a * t
    print("Luas Segitiga : ", luas)
    tanya()



def menu():
    print("Haryati_D0220412")
    print("TUGAS 3 PBO KELAS H")
    print("PROGRAM MENGHITUNG LUAS")
    print("\nPilih Program :")
    print("	1. Menghitung Luas Lingkaran")
    print("	2. Menghitung Luas Persegi")
    print("	3. Menghitung Luas Segitiga")
    print("	4. Exit")

    pilih = int(input("Masukkan pilihan [1-4] : "))

    if pilih == 1:
        lingkaran()
    elif pilih == 2:
        persegi()
    elif pilih == 3:
        segitiga()
    elif pilih == 4:
        print("Terima kasih sudah menggunakan aplikasi ini!")
        sys.exit()
    else:
        print("\nPilihan yang anda masukkan salah!")
        menu()

def tanya():
    print("\n-----------------------------------------")
    tanya = input(" Ingin mengulang aplikasi lagi? [y/t] : ")
    print("-----------------------------------------")
    if tanya == "y":
        menu()
    elif tanya == "t":
        sys.exit()
    else:
        print("Pilihan yang anda masukan salah!")

menu()