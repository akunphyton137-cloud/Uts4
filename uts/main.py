from utils import *
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear()

    print("=== MENU BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Layang-Layang")
    print("6. Belah Ketupat")
    print("7. Trapesium")
    print("8. Lingkaran")
    print("9. Belah Ketupat")
    print("10. Heksagon")
    print("11. Pentagon")
    print("12. Keluar")

    pilih = input("Pilih bangun datar: ")

    if pilih == "12":
        clear()
        print("Program selesai. Terima kasih 🙏")
        break

    elif pilih == "1":
        s = float(input("Masukkan sisi: "))
        print("\nKeliling persegi:", keliling_persegi(s))
        print("Luas persegi:", luas_persegi(s))

    elif pilih == "2":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("\nKeliling persegi panjang:", keliling_persegi_panjang(p, l))
        print("Luas persegi panjang:", luas_persegi_panjang(p, l))

    elif pilih == "3":
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        c = float(input("Sisi c: "))
        alas = float(input("Alas: "))
        tinggi = float(input("Tinggi: "))
        print("\nKeliling segitiga:", keliling_segitiga(a, b, c))
        print("Luas segitiga:", luas_segitiga(alas, tinggi))

    elif pilih == "4":
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        alas = float(input("Alas: "))
        tinggi = float(input("Tinggi: "))
        print("\nKeliling jajar genjang:", keliling_jajar_genjang(a, b))
        print("Luas jajar genjang:", luas_jajar_genjang(alas, tinggi))

    elif pilih == "5":
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        print("\nKeliling layang-layang:", keliling_layang_layang(a, b))
        print("Luas layang-layang:", luas_layang_layang(d1, d2))

    elif pilih == "6":
        s = float(input("Masukkan sisi: "))
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        print("\nKeliling belah ketupat:", keliling_belah_ketupat(s))
        print("Luas belah ketupat:", luas_belah_ketupat(d1, d2))

    elif pilih == "7":
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        c = float(input("Sisi c: "))
        d = float(input("Sisi d: "))
        t = float(input("Tinggi: "))
        print("\nKeliling trapesium:", keliling_trapesium(a, b, c, d))
        print("Luas trapesium:", luas_trapesium(a, b, t))

    elif pilih == "8":
        r = float(input("Masukkan jari-jari: "))
        print("\nKeliling lingkaran:", keliling_lingkaran(r))
        print("Luas lingkaran:", luas_lingkaran(r))

    elif pilih == "9":
        s = float(input("Masukkan sisi: "))
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        print("\nKeliling belah ketupat:", keliling_belah_ketupat_2(s))
        print("Luas belah ketupat:", luas_belah_ketupat_2(d1, d2))

    elif pilih == "10":
        s = float(input("Masukkan sisi: "))
        print("\nKeliling heksagon:", keliling_heksagon(s))
        print("Luas heksagon:", luas_heksagon(s))

    elif pilih == "11":
        s = float(input("Masukkan sisi: "))
        print("\nKeliling pentagon:", keliling_pentagon(s))
        print("Luas pentagon:", luas_pentagon(s))

    else:
        print("\nPilihan tidak tersedia!")

    input("\nTekan Enter untuk kembali ke menu...")