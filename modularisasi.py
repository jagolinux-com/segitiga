"""
Menghitung luas segitiga
Alas x Tinggi  / 2
"""
print ("Menghitung luas segitiga 1")
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas = {alas} dan tinggi ={tinggi} memiliki luas {luas_segitiga}\n')

print("Menghitung luas segitiga dengan copas dari segitiga 1")
alas = 50
tinggi = 50
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas = {alas} dan tinggi ={tinggi} memiliki luas {luas_segitiga}\n')

#Membuat modul
print("Menghitung luas segitiga dengan fungsi")
def hitung_luas_segitiga (alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung Luas segitiga  dengan fungsi hasilnya={hitung_luas_segitiga(10,6)}')
print(f'Menghitung Luas segitiga  dengan fungsi hasilnya={hitung_luas_segitiga(20,34)}')

"""
dengan fungsi tidak perlu copy paste code pada segitiga 1
"""




