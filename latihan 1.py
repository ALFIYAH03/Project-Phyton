#Menghitung Tarif Sewa

sewa1= 200000
sewa2= 10000
jamMulai=6
jamSelesai=23
menitMulai=0
menitSelesai=50
lamaSewa= (jamSelesai - jamMulai) + int((menitSelesai - menitMulai)/60)
harga = (lamaSewa//12 * sewa1) + (lamaSewa%12 * sewa2)
print(harga)
