#SOAL NOMOR 4
jarakAB= 125
jarakBC= 256
kecepatanAB= 62
kecepatanBC= 70
jamBerangkat=6
menitIstirahat=45
menitBerangkat=0

waktuPerjalanan = int(((jarakAB/kecepatanAB)+(jarakBC/kecepatanBC))*60)+(menitIstirahat)
print(round(waktuPerjalanan/60, 2) + jamBerangkat)
