import math

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi(sisi):
    return sisi * sisi



def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def luas_persegi_panjang(p, l):
    return p * l



def keliling_segitiga(a, b, c):
    return a + b + c

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi



def keliling_jajar_genjang(a, b):
    return 2 * (a + b)

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi



def keliling_layang_layang(a, b):
    return 2 * (a + b)

def luas_layang_layang(d1, d2):
    return 0.5 * d1 * d2



def keliling_belah_ketupat(sisi):
    return 4 * sisi

def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2



def keliling_trapesium(a, b, c, d):
    return a + b + c + d

def luas_trapesium(a, b, tinggi):
    return 0.5 * (a + b) * tinggi



def keliling_lingkaran(r):
    return 2 * math.pi * r

def luas_lingkaran(r):
    return math.pi * r * r



def keliling_belah_ketupat_2(sisi):
    return 4 * sisi

def luas_belah_ketupat_2(d1, d2):
    return 0.5 * d1 * d2



def keliling_heksagon(sisi):
    return 6 * sisi

def luas_heksagon(sisi):
    return (3 * math.sqrt(3) / 2) * sisi * sisi



def keliling_pentagon(sisi):
    return 5 * sisi

def luas_pentagon(sisi):
    return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * sisi * sisi